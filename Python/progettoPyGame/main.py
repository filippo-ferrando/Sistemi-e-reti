import pygame as pg
import sys

DIMENSIONI = (600,600)

NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)

def drawgrid():
    dimensione = 50
    for x in range (0, DIMENSIONI[0],dimensione):
        for y in range (0,DIMENSIONI[1],dimensione):
            piastrella = pg.Rect(x,y,dimensione,dimensione)
            pg.draw.rect(screen, BIANCO, piastrella, 2)

    ostacolo = pg.Rect(50,100, dimensione, dimensione)
    pg.draw.rect(screen, ROSSO, ostacolo)

def main():
    global screen
    pg.init()

    screen = pg.display.set_mode(DIMENSIONI)
    screen.fill(NERO)

    while True:
        drawgrid()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()


if __name__ == "__main__":
    main()