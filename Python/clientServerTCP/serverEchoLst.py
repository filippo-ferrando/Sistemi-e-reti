from os import truncate
import socket as sck
import threading as thr

lstConnection = []

class Client_Manager(thr.Thread):
    def __init__(self, conn, addr):
        thr.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.running = True

    def run(self):
        while self.running:
            received_msg = self.conn.recv(4096)
            print(f"<{thr.current_thread()}> Messaggio ricevuto da {self.addr}: {received_msg.decode()}")
            for conn in lstConnection:
                conn.send(received_msg)



def main():
    print(f"Io sono <{thr.current_thread()}>")
    s = sck.socket(sck.AF_INET ,sck.SOCK_STREAM)
    s.bind(("127.0.0.1", 5004))
    s.listen()

    while True:
        conn, addr = s.accept()
        lstConnection.append(conn)
        client = Client_Manager(conn, addr)
        client.start()

        


if __name__ == "__main__":
    main()