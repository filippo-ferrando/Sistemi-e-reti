'''
Simple chat in python using TCP socket and multithreading
'''
import socket as sck
import threading as thr

LOCAL = ('localhost', 5000)

class Connection(thr.Thread):
    def __init__(self, port, s):
        thr.Thread.__init__(self)
        self.port = port
        self.s = s
        self.running = True
    def run(self):
        while self.running:
            data, addr = self.s.recvfrom(self.port)
            print(f"\nmessaggio arrivato da {data.decode()}")

def main():
    #s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(LOCAL)
    conn = Connection(5000, s)
    conn.start()

    while True:
        msg = input('insert a message: ')
        s.sendall(msg.encode())
        if msg == 'exit':
            print('Disonnessione...')
            conn.running = False
            conn.join()
            s.close()
            exit()
    

if __name__ == '__main__':
    main()
