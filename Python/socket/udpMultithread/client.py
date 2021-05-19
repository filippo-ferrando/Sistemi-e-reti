'''
Simple chat in python using TCP socket and multithreading
'''
import socket as sck
import threading as thr
import time

LOCAL = ('localhost', 5003)

class encryptMessage():
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)

    def encode_msg(self):
        #print(self.outputString)
        return self.outputString.encode()


class Connection(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
        self.running = True
    def run(self):
        while self.running:
            data, addr = self.s.recvfrom(4096)
            msg_received = data.decode().split('浤')
            print(f"\nmessaggio arrivato da {msg_received[0]} : {msg_received[-1]}")

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    conn = Connection(s)
    conn.start()

    s.sendto(input('tell me your nickname: ').encode(), LOCAL)

    while True:
        time.sleep(0.2)
        receiver = input('tell me the receiver nick: ')
        if receiver.startswith('exit'):
            message = 'exit'
        else: 
            message = input('insert a message: ')
            msg = encryptMessage(receiver,message)

        if message.startswith('exit'):
            msg = encryptMessage('None',message)
            
        s.sendto(msg.encode_msg(), LOCAL)
        
        if message.startswith('exit'):
            conn.running = False
            s.close()
            conn.join()
            print('Thread killed succesfully')
            exit()
    

if __name__ == '__main__':
    main()
