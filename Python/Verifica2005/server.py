import socket as sck
import threading as thr
import random


lstClient = []

SECRET_NUMBER = random.randint(1, 100) #numero segreto del croupier
print(SECRET_NUMBER)

class encryptMessage():
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)     #stesso sistema del client

    def encode_msg(self):
        return self.outputString.encode()


class Client_Manager(thr.Thread):
    def __init__(self, addr, conn):
        thr.Thread.__init__(self)
        self.addr = addr
        self.conn = conn
        self.nickname = ''
        self.running = True
        self.manche = 3
        #self.diff = []
    
    def run(self):
        while self.running:
            msg_received = self.conn.recv(4096)
            msg_received = msg_received.decode().split('浤')
            print(msg_received[0])
            if msg_received[-1].startswith('exit') and self.running or self.manche==0 or msg_received[0] == True: #controllo per messaggio ad exit o manche finite
                self.running = False
            
            else:
                print(f'<{thr.current_thread()}>messaggio spedito da {self.nickname} : {msg_received[-1]}')
                for client in lstClient:
                    if client.nickname == self.nickname and self.manche > 0:    #controllo messaggio ricevuto per rispondere correttamente
                        if int(msg_received[-1]) < SECRET_NUMBER:
                            msg_send = encryptMessage("server", "+")
                            client.conn.sendall(msg_send.encode_msg())
                        elif int(msg_received[-1]) > SECRET_NUMBER:
                            msg_send = encryptMessage("server", "-")
                            client.conn.sendall(msg_send.encode_msg())
                        elif int(msg_received[-1]) == SECRET_NUMBER:
                            msg_send = encryptMessage("server", "HAI VINTO")
                            #self.vinto = True
                            client.conn.sendall(msg_send.encode_msg())
                        self.manche -= 1
                        #self.diff.append(abs(int(msg_received[-1])) - abs(SECRET_NUMBER))
    

class Accettazione(thr.Thread):     #thread accettazione connesioni
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
    s.bind(('127.0.0.1', 5011))
    s.listen()

    acc = Accettazione(s)
    acc.start()

    while True:     #controllo delle chiusure
        for c in lstClient:
            if not c.running:
                print(f"Closing {c.nickname} --> {c.conn}")
                c.conn.close()
                c.join()
                lstClient.remove(c)
                #print(lstClient)
            '''
            if not c.vinto:         #prova del facoltativo
                listFalse += 1

            if len(listFalse) == len(lstClient):
                pass
            '''


if __name__ == "__main__":
    main()


'''
            elif self.manche == 0 and int(msg_received[-1]) == SECRET_NUMBER:
                msg_send = encryptMessage("server", "Hai vinto")
                for client in lstClient:
                    if client.nickname == self.nickname:
                        client.conn.sendall(msg_send.encode_msg())
                self.running = False
            '''