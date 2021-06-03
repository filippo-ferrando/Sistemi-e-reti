import threading
import time
import random

lock = threading.Lock()

class filosofo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.durata = random.randint(10,20)/10
        self.mangiato = False

    def run(self):
        if prendiForchetta(self.id) and not self.mangiato:
            print('iniziato: ' + str(self.id))
            lock.acquire()
            time.sleep(self.durata)
            liberaForchetta(self.id)
            lock.release()
            print('terminato: ' + str(self.id))
            self.mangiato = True
        else:
            time.sleep(self.durata)
            self.mangiato = False
            print('none')

forchette = [False for i in range(5)]
filosofi = [filosofo(i) for i in range(5)]

def prendiForchetta(filosofo):
    if not forchette[filosofo] and not forchette[(filosofo+1) % len(filosofi)]:
        forchette[filosofo] = True
        forchette[(filosofo+1) % len(filosofi)] = True
        return True
    else:
        return False


def liberaForchetta(filosofo):
    forchette[filosofo] = False
    forchette[(filosofo+1) % len(filosofi)] = False


def refreshThread(filosofi):
    filosofi = [None for i in range(5)]
    filosofi = [filosofo(i) for i in range(5)]


def main():
    for fil in filosofi:
        fil.start()
    for fil in filosofi:
        fil.join()
    
    refreshThread(filosofi)



if __name__ == '__main__':
    main()import threading
import time
import random

class Filosofo (threading.Thread):
    running = True
    def __init__ (self,name,forkOnLeft,forkOnRight):
        threading.Thread.__init__(self)
        self.name = name
        self.forkOnLeft = forkOnLeft #forchetta di sinistra
        self.forkOnRight = forkOnRight #forchetta di destra
    
    def run (self):
        while(self.running):
            time.sleep(random.uniform(1,5))#prima di mangiare il filosofo dorme per un tempo casuale tra 1-5
            print (f"{self.name} ha fame")
            self.cena()

    def cena(self):
        fork1 , fork2 = self.forkOnLeft , self.forkOnRight
        while self.running: #esegui il while finchè il filosofo non trova le due forchette libere
            fork1.acquire(True) #prendo brutalmente la fork1
            locked = fork2.acquire (False) #chiedo gentilmente la fork2
            if locked: #se fork2 non è libera
                break
            fork1.release() #fork1 viene rilasciata
            print (f"{self.name} scambia le forchette")#e il filosofo scambia le forchette fino a che sono libere entrambe
            fork1 , fork2 = fork2, fork1 #scambia le forchette
        else:
            return
        print (f"{self.name} inizia a mangiare") #se le forchette sono libere il filosofo può mangiare
        time.sleep(random.uniform(1,3)) #mangia per un tempo casuale tra 1-3
        print (f"{self.name} finisce di mangiare e torna a pensare")#finito di mangiare torna a pensare
        fork2.release()#e rilascia entrambre le forchette
        fork1.release()#e rilascia entrambre le forchette

        

def main ():
    forks = [threading.Lock() for n in range(5)] # creo una lista con 5 lock che sono le forchette
    philosopherName = ('Aristotele','Kant','Buddha','Marx','Russel') #assegno i nomi ai filosofi
    philosopher = [Filosofo(philosopherName [i], forks[i%5], forks[(i+1)%5]) for i in range(5)] #lista di  Filosofi in cui passi nome del filosofo,forchetta di posizione i, forchetta di posizione i+1
    Filosofo.running = True
    for p in philosopher:
        p.start()
    time.sleep(60)#tempo della cena di 60 secondi
    Filosofo.running = False
    print ("ora abbiamo finito")

if __name__ == "__main__":
    main()