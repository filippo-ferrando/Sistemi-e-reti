'''
Simple chat in python using TCP socket and multithreading
'''
import socket as sck
import threading as thr


connessioni = []
users = {}


class Client_Manager(thr.Thread):
    def __init__(self, addr, conn):
        thr.Thread.__init__(self)
        self.addr = addr
        self.conn = conn
        self.running = True

    def getNick(self):
        for key, value in users.items():
            if value == self.addr:
                return key
        return None
    
    def run(self):
        while self.running:
            msg_received = self.conn.recv(4096)
            if msg_received.decode()[:-1] == 'exit': 
                self.running = False
            else:
                print(f'<{thr.current_thread()}>messaggio ricevuto da {self.getNick()}: {msg_received.decode()}')
                for connection in connessioni:
                    connection.conn.sendall((self.getNick() + ' : ' + msg_received.decode()).encode())
    

class Accettazione(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
    
    def run(self):
        while True:
            conn, addr = self.s.accept()
            client = Client_Manager(addr, conn)
            client.conn.sendall('tell me your nickname: '.encode())
            nick = client.conn.recv(4096)
            users[nick.decode()] = addr
            print('saved new user: ' + nick.decode())
            connessioni.append(client)
            client.start()


def main():
    print(thr.current_thread())
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen()

    acc = Accettazione(s)
    acc.start()

    while True:
        for c in connessioni:
            if not c.running:
                c.conn.close()
                c.join()
                connessioni.remove(c)


if __name__ == "__main__":
    main()