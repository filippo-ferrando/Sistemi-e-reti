'''
Simple chat in python using UDP socket
'''
import socket as sck
import threading as thr

PORT = 5000
lstClient = {}

class encryptMessage():
    def __init__(self, *args):
        self.outputString = '浤'.join(str(i) for i in args)

    def encode_msg(self):
        return self.outputString.encode()


def getKey(val):
    for nick, tupla in lstClient.items():
        if tupla == val:
            return nick
    return 'user not found'


def main():
    print(thr.current_thread())
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(('localhost', PORT))


    while True:
        msg_received, addr = s.recvfrom(PORT)
        msg_received = msg_received.decode().split('浤')
        

        if msg_received[0].startswith('newUser'):
            try:
                lstClient[msg_received[1]] = addr
                print(f"nuovo utente registrato: {msg_received[1]}")
            except Exception:
                print(f"errore: impossibile registrare nuovo utente")
        else:
            print(f"messaggio di {addr} : {msg_received[1]}")
            for key, value in lstClient.items():
                if msg_received[0].startswith(key):
                    print()
                    print(value)
                    print()
                    print(getKey(addr))
                    s.sendto(encryptMessage(getKey(addr),msg_received[1]).encode_msg(), value) #send to destination encrypted nickname, text, address
    s.close()

if __name__ == "__main__":
    main()