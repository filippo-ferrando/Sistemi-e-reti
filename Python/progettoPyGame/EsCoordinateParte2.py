import sys
import pygame as pg
import pygame

global personaggio, possibilita, pavimento

possibilita = {}

pavimento = [[0, 0, 0, -1, -1, 0, -1], #0 libero -1 occupato
            [-1, 0, 0, 0, -1, -1, 0], 
            [0, 0, -1, -1, -1, 0, 0], 
            [-1, 0, 0, 0, -1, -1, 0], 
            [-1, 0, 0, 0, 0, -1, -1], 
            [-1, -1, -1, 0, 0, 0, -1]] 


dimensione = 50 
DIMENSIONI = (dimensione * len(pavimento[0]), dimensione * len(pavimento))


NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)
VERDE = (0,255,0)


def disegnaSfondo():
    for x in range (len(pavimento)):
        for y in range (len(pavimento[0])):
            piastrella = pg.Rect(y*dimensione,x*dimensione,dimensione,dimensione)

            if (pavimento[x][y] == -1):
                pg.draw.rect(screen, ROSSO, piastrella)
            else:
                pg.draw.rect(screen, BIANCO, piastrella)


def controllaMovimenti(event):
    global personaggio, possibilita
    spostX = 0
    spostY = 0

    if event.key == pg.K_w:
        print("su")
        spostY = -1
    elif event.key == pg.K_s:
        print("giu")
        spostY = +1 
    elif event.key == pg.K_a:
        print("sinistra")
        spostX = -1
    elif event.key == pg.K_d:
        print("destra")
        spostX = +1
   

    for posFuture in possibilita[personaggio][1:]:
        if([possibilita[personaggio][0][0] + spostY, possibilita[personaggio][0][1] + spostX] == possibilita[posFuture][0]):
            personaggio = posFuture

        print(posFuture)
        print(possibilita[personaggio])

def mappaPavimento():
    global possibilita, pavimento

    possibilita = {}
    k = 0

    for cordx in range (len(pavimento)):
        for cordy in range (len(pavimento[cordx])):
            if pavimento[cordx][cordy] == 0:
                pavimento[cordx][cordy] = k
                k += 1

    for cordx in range (len(pavimento)):
        for cordy in range (len(pavimento[cordx])):
            lElemento = []
            if pavimento[cordx][cordy] != -1:
                if cordx > 0:
                    if pavimento[cordx-1][cordy] != -1:
                        lElemento.append(pavimento[cordx-1][cordy])
                if cordx+1 < len(pavimento):
                    if pavimento[cordx+1][cordy] != -1:
                        lElemento.append(pavimento[cordx+1][cordy])
                if cordy > 0:
                    if pavimento[cordx][cordy-1] != -1:
                        lElemento.append(pavimento[cordx][cordy-1])
                if cordy < len(pavimento):
                    if pavimento[cordx][cordy+1] != -1:
                        lElemento.append(pavimento[cordx][cordy+1])
    
                if len(lElemento) != 0:
                    lElemento.insert(0, (cordx, cordy)) 

                possibilita[pavimento[cordx][cordy]] = lElemento


def stampaRect():
    global possibilita
    
    stampaPer = pg.Rect(possibilita[personaggio][0][0]*dimensione, possibilita[personaggio][0][1]*dimensione, dimensione,dimensione)
    
    pg.draw.rect(screen, VERDE, stampaPer)

    


def main():
    global screen, personaggio, possibilita
    pg.init()

    screen = pg.display.set_mode(DIMENSIONI)
    screen.fill(NERO)

    mappaPavimento()

    personaggio = 0

    while True:
        disegnaSfondo()
        stampaRect()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                controllaMovimenti(event)
        
        
        pg.display.update()


        

if __name__ == "__main__":
    main()