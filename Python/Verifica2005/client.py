import socket as sck
import threading as thr
import time

LOCAL = ('localhost', 5011)

winControll = False

class encryptMessage():         #protocollo per inviare messaggi con carattere divisorio speciale
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)

    def encode_msg(self):
        #print(self.outputString)
        return self.outputString.encode()


class Connection(thr.Thread):
    global winControll  #variabile controllo risposta server

    def __init__(self, port, s):
        thr.Thread.__init__(self)
        self.port = port
        self.s = s
        self.running = True
    def run(self):
        while self.running:
            data, addr = self.s.recvfrom(self.port)
            msg_received = data.decode().split('浤')
            print(f"\nmessaggio arrivato dal Croupier : {msg_received[-1]}")
            #print(msg_received[-1])
            if msg_received[-1].startswith("HAI VINTO"): #controllo messaggio server
                winControll = True

def main():
    global winControll

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(LOCAL)
    conn = Connection(LOCAL[1], s)
    conn.start()

    manche = 3

    s.sendall(input('tell me your nickname: ').encode())

    while True:
        time.sleep(0.2)
         
        message = input('insert a message: ')
        print(winControll)       # "criptazione" messggio e diminuzione manche
        msg = encryptMessage(winControll,message)
        manche -= 1
        

        if manche >= 0: #se ho ancora manche continua a giocare
            s.sendall(msg.encode_msg())
        elif winControll: #se il server risponde che ho finto consegna messaggio uscita
            msg = encryptMessage(winControll, "exit")
            s.sendall(msg.encode_msg())
        else:#se ho finito le manche manda l'uscita
            msg = encryptMessage(winControll, "exit")
            s.sendall(msg.encode_msg())

            
       
        
        if message.startswith('exit') or manche == 0 or winControll: #controllo i valori per uscire dal client
            conn.running = False
            s.close()
            conn.join()
            print('Thread killed succesfully')
            exit()

        
    

if __name__ == '__main__':
    main()
