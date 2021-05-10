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
    main()