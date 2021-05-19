'''
Simple chat in python using TCP socket and multithreading
'''
import socket as sck
import threading as thr

LOCAL = ("localhost", 5003)
lstClient = {}
dizMessages = {}

class encryptMessage():
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)

    def encode_msg(self):
        return self.outputString.encode()


class Client_Manager(thr.Thread):
    def __init__(self, addr, nickname, s):
        thr.Thread.__init__(self)
        self.addr = addr
        self.s = s
        self.nickname = nickname
        self.running = True
        self.lung = 0
    
    def run(self):
        dizMessages[self.addr] = []
        while self.running:
            if dizMessages[self.addr].len() != self.lung:
                msg = dizMessages[self.addr][self.lung]
                msg = msg.decode().split('浤')

            if msg[-1].startswith('exit') and self.running: 
                self.running = False   
            
            #print(f'<{thr.current_thread()}>messaggio spedito da {self.nickname} a {msg_received[0]}: {msg_received[-1]}')
            for key in lstClient.keys():
                if key == msg[0] or (msg[0] == 'all' and self != key):
                    msg_send = encryptMessage(self.nickname, msg[-1])
                    self.s.sendto(msg_send.encode_msg(), lstClient[key])

            self.lung += 1

            



class Controllo(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
        self.running = True
    
    def run(self):
        while True:
            msg_received, addr = self.s.recvfrom(4096)        #ottengo stringa inviata --> nicknamed: testo --> ["nickname", "testo"]
            msg_received_split = msg_received.decode().split('浤')
            
            for value in lstClient.values():
                if addr == value:
                    for key in dizMessages.keys():
                        if key == addr:
                            dizMessages[key].append(msg_received)                    
                else:
                    c = Client_Manager(addr, msg_received_split[0], self.s)
                    lstClient[msg_received_split[0]] = addr
                    c.start()
                    



def main():
    print(thr.current_thread())
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(LOCAL)

    acc = Controllo(s)
    acc.start()
    '''
    while True:
        for c in lstClient:
            if not c.running:
                print(f"Closing {c.nickname}")
                c.join()
                #print(lstClient)
    '''


if __name__ == "__main__":
    main()