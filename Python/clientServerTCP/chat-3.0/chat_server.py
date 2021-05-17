'''
Simple chat in python using TCP socket and multithreading
'''
import socket as sck
import threading as thr


lstClient = []

class MyStringProtocol():
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)

    def encode_msg(self):
        return self.outputString.encode()


class Client_Manager(thr.Thread):
    def __init__(self, addr, conn):
        thr.Thread.__init__(self)
        self.addr = addr
        self.conn = conn
        self.nickname = ''
        self.running = True
    
    def run(self):
        while self.running:
            msg_received = self.conn.recv(4096)
            msg_received = msg_received.decode().split('浤')
            if msg_received[-1].startswith('exit') and self.running: 
                self.running = False
            else:
                print(f'<{thr.current_thread()}>messaggio spedito da {self.nickname} a {msg_received[0]}: {msg_received[-1]}')
                for client in lstClient:
                    if client.nickname == msg_received[0] or (msg_received[0] == 'all' and self != client):
                        msg_send = MyStringProtocol(self.nickname, msg_received[-1])
                        client.conn.sendall(msg_send.encode_msg())
    

class Accettazione(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
    
    def run(self):
        while True:
            conn, addr = self.s.accept()
            client = Client_Manager(addr, conn)
            nick = client.conn.recv(4096)
            client.nickname = nick.decode()
            print('saved new user: ' + nick.decode())
            lstClient.append(client)
            client.start()


def main():
    print(thr.current_thread())
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(('127.0.0.1', 5003))
    s.listen()

    acc = Accettazione(s)
    acc.start()

    while True:
        for c in lstClient:
            if not c.running:
                c.conn.close()
                c.join()
                lstClient.remove(c)


if __name__ == "__main__":
    main()