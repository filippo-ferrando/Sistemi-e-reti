from os import truncate
import socket as sck
import threading as thr

lstConnection = []
lstThread = []

class Client_Manager(thr.Thread):
    def __init__(self, conn, addr):
        thr.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.running = True

    def isRunning(self):
        return self.running

    def run(self):
        while self.running:
            received_msg = self.conn.recv(4096)
            print(f"<{thr.current_thread()}> Messaggio ricevuto da {self.addr}: {received_msg.decode()}")
            
            for conn in lstConnection:
                conn.send(received_msg)

            if received_msg.decode().startswith("exit"):
                self.running = False
                self.conn.close()

class uccidiThread(thr.Thread):
    def __init__(self):
        thr.Thread.__init__(self)
        self.running = True

    def run(self):
        while self.running:
            for i in lstThread:
                if not i.isRunning:
                    i.join()
                    lstThread.remove(i)
                    lstConnection.remove(i)
                    print("thread ucciso")



def main():
    print(f"Io sono <{thr.current_thread()}>")
    s = sck.socket(sck.AF_INET ,sck.SOCK_STREAM)
    s.bind(("127.0.0.1", 5006))
    s.listen()

    uccidi = uccidiThread()
    uccidi.start()

    while True:
        conn, addr = s.accept()
        lstConnection.append(conn)
        client = Client_Manager(conn, addr)
        lstThread.append(client)
        client.start()

        

        '''
        for client in lstThread:
            #print(client.running)
            if client.running == False:
                #print("chiuso")
                client.join()
                lstThread.remove(client)
        '''

        


if __name__ == "__main__":
    main()