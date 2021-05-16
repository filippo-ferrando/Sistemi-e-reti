from os import truncate
import socket as sck
import threading as thr

lstConnection = {}
counterThread = 0

class Client_Manager(thr.Thread):
    def __init__(self, conn, addr, nome):
        thr.Thread.__init__(self)
        self.nome = nome
        self.conn = conn
        self.addr = addr
        self.running = True

    def run(self):
        while self.running:
            received_msg = self.conn.recv(4096)
            print(f"<{thr.current_thread()}> Messaggio ricevuto da {self.addr}: {received_msg.decode()}")
            for k in lstConnection.keys():
                print(k)
                print(self.nome)
                if k != self.nome:
                    lstConnection[k].send(received_msg)
          
                    



def main():
    global counterThread
    print(f"Io sono <{thr.current_thread()}>")
    s = sck.socket(sck.AF_INET ,sck.SOCK_STREAM)
    s.bind(("127.0.0.1", 5008))
    s.listen()

    while True:
        conn, addr = s.accept()
        client = Client_Manager(conn, addr, counterThread)
        counterThread += 1

        lstConnection[counterThread] = conn
        #print(lstConnection.keys())

        client.start()

        


if __name__ == "__main__":
    main()