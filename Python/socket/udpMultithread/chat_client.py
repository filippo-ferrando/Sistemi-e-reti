'''
Simple chat in python using UDP socket and multithreading
'''
import socket as sck
import threading as thr
import time

LOCAL = ('localhost', 5000)
SERVER = ('0.0.0.0', 5000)

class encryptMessage():
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)

    def encode_msg(self):
        return self.outputString.encode()


class Receiver(thr.Thread):
    def __init__(self, port, s):
        thr.Thread.__init__(self)
        self.port = port
        self.s = s
        self.running = True
    def run(self):
        while self.running:
            data,_ = self.s.recvfrom(self.port)
            msg_received = data.decode().split('浤')
            print(f"\nmessaggio arrivato da {msg_received[0]} : {msg_received[1]}")

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    rec = Receiver(SERVER[1], s)
    rec.start()

    while True:
        time.sleep(0.2)
        receiver = input('tell me the receiver nick: ')
        if receiver.startswith('newUser'):
            body = input('insert a nickname: ')
        else:
            if receiver.startswith('exit'):
                body = 'exit'
            else: body = input('insert a message: ')
        msg = encryptMessage(receiver,body)

        if body.startswith('exit'):
            msg = encryptMessage('None',body)
            
        s.sendto(msg.encode_msg(), SERVER)
        if body.startswith('exit'):
            s.close()
            rec.join()
            print('Thread killed succesfully')
            exit()
    

if __name__ == '__main__':
    main()
