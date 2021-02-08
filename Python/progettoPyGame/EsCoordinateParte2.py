import sys
import pygame as pg

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



def disegnaSfondo():
    for x in range (len(pavimento)):
        for y in range (len(pavimento[0])):
            piastrella = pg.Rect(y*dimensione,x*dimensione,dimensione,dimensione)

            if (pavimento[x][y] == -1):
                pg.draw.rect(screen, ROSSO, piastrella)
            else:
                pg.draw.rect(screen, BIANCO, piastrella)



def main():
    global screen
    pg.init()

    screen = pg.display.set_mode(DIMENSIONI)
    screen.fill(NERO)

    while True:
        disegnaSfondo()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()

if __name__ == "__main__":
    main()