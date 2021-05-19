from os import truncate
import socket as sck
import threading as thr

lstThread = []
lstConnection = []
user = {}

class Client_Manager(thr.Thread):
    def __init__(self, conn, addr):
        thr.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.running = True

    def getNick(self):
        for key, value in user.items():
            if value == self.addr:
                return key
        return None

    def run(self):
        while self.running:
            received_msg = self.conn.recv(4096)
            
            #print(received_msg.decode())

            if received_msg.decode().startswith("exit"):
                self.running = False
                self.conn.close()
            else:
                print(f"<{thr.current_thread()}> Messaggio ricevuto da {user[self.conn]}: {received_msg.decode()}")


            for connection in lstConnection:
                if connection == self.conn:
                    pass
                else:
                    connection.send(received_msg)

class AcceptConnection(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s

    def run(self):
        while True:
            conn, addr = self.s.accept()
            client = Client_Manager(addr, conn)
            conn.sendall("insert you nick --> ".encode())
            nick = conn.recv(4096)
            user[nick.decode()] = addr
            print("saved new user: " + nick.decode())
            lstConnection.append(client)
            client.start()
    


def main():
    print(f"Io sono <{thr.current_thread()}>")
    s = sck.socket(sck.AF_INET ,sck.SOCK_STREAM)
    s.bind(("127.0.0.1", 5009))
    s.listen()

    connetti = AcceptConnection(s)
    connetti.start()

    while True:

        for client in lstThread:
            #print(client.running)
            if client.running == False:
                #print("chiuso")
                client.join()
                lstThread.remove(client)
                lstConnection.remove(client)
                del user[client]
                

        


if __name__ == "__main__":
    main()

