import socket as sck
import time
import threading as thr

messageSent = ""
messageReceived = ""

class recive(thr.Thread):
    def __init__(self, socket):
        thr.Thread.__init__(self)
        self.s = socket
        self.running = True

    def stopRun(self):
        self.running = False

    def run(self):
        while self.running:
            messageReceived = self.s.recv(4096)
            print(f"messaggio dal server: " + messageReceived.decode())
            time.sleep(0.2)



def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    s.connect(('localhost', 5006))
    print("Connessione avvenuta")
    rec = recive(s)
    rec.start()

    while True:
        x = input("inserisci messaggio --> ")
        s.sendall(x.encode())

        if x == "exit":
            print(f"Disconnessione...")
            break
    rec.stopRun()
    rec.join()
    s.close()

if __name__ == "__main__":
    main()