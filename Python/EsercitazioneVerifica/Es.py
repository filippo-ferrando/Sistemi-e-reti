import sys
import pygame
import random
import csv

distanza = 10
dizPosizioni = {1:[0,0]}
decisione = 0

DIMMAX = 60
OFFSET = 30

dimensione = 15
DIMENSIONI = (dimensione * DIMMAX, dimensione * DIMMAX)

NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)
VERDE = (0,255,0)

global cordX, cordY


def disegnaCampo():
    for x in range (DIMMAX): #dovrebbe essere il doppio ma spacca gli occhi
            for y in range (DIMMAX):
                piastrella = pygame.Rect(y*dimensione,x*dimensione,dimensione,dimensione)
                pygame.draw.rect(screen, BIANCO, piastrella,1)

def disegnaPartenza(x, y):
    piastrella = pygame.Rect(x*dimensione,y*dimensione,dimensione,dimensione)
    pygame.draw.rect(screen, ROSSO, piastrella)

def disegnaPercorso(x, y):
    piastrella = pygame.Rect(x*dimensione,y*dimensione,dimensione,dimensione)
    pygame.draw.rect(screen, VERDE, piastrella)

def main():
    global screen, cordX, cordY

    pygame.init()

    screen = pygame.display.set_mode(DIMENSIONI)
    screen.fill(NERO)

    cordX = 0
    cordY = 0

    partenza = [OFFSET, OFFSET]
    

    with open('percorso.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for x in range(1,DIMMAX,1):
            decisione = random.randint(0, 5)
            
            if decisione == 0: #Sud scendo
                cordY -= 1
            elif decisione == 1: #Nord salgo
                cordY += 1
            elif decisione == 2: #ovest sinistra
                cordX -= 1
            elif decisione == 3: #est destra
                cordX += 1
            
            dizPosizioni[x+1] = [cordX, cordY]

            writer.writerow([x, dizPosizioni[x][0], dizPosizioni[x][1]])


    while True:
        disegnaCampo()
        
        for x in dizPosizioni:
            disegnaPercorso((dizPosizioni[x][0])+OFFSET, (dizPosizioni[x][1])+OFFSET)

        disegnaPartenza(partenza[0], partenza[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        pygame.display.update()

            

if __name__ == "__main__":
    main()