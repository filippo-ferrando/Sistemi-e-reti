import socket as sck
import threading as thr
import time 
import random

lista_clienti = []
MAX_CLIENTI = 3

#classe thread
class Classe_Thread(thr.Thread):
    #funzione che si avvia alla creazione della classe
    def __init__(self, nome, cassa):
        thr.Thread.__init__(self)   #costruttore super (java)
        self.nome = nome
        self.cassa = cassa
        self.running = True

    #funzione che si avvia con il comando start()
    def run(self):
        #il cliente sta pagando alla cassa
        while self.running:
            if self.cassa.acquire(False) == True:
                self.cassa.locked()
                print(f"Il cliente {self.nome} sta pagando")
                time.sleep(3) 

                print(f"Costo: {random.uniform(1,100)}")

                print(f"Il cliente {self.nome} esce dal supermercato")
                self.running = False 

                self.cassa.release()


def main():
    k = 0
    cassa = thr.Lock()
    while True:
        if len(lista_clienti) < MAX_CLIENTI:
            print(f"Il cliente {k} entra nel supermercato")
            client = Classe_Thread(k, cassa)
            lista_clienti.append(client)
            client.start()
            #client.join()
            k = k + 1

        #chiusura di tutti i client con running = False
        for c in lista_clienti:
            if c.running == False:
                c.join()
                lista_clienti.remove(c)



main()