import pygame
import sys
import csv

dizionario = {'a':[0,0,0,0,0],  #dizionario
              'b':[0,0,0,0,1], 
              'c':[0,0,0,1,0], 
              'd':[0,0,0,1,1], 
              'e':[0,0,1,0,0], 
              'f':[0,0,1,0,1], 
              'g':[0,0,1,1,0], 
              'h':[0,0,1,1,1], 
              'i':[0,1,0,0,0], 
              'l':[0,1,0,0,1], 
              'm':[0,1,0,1,0], 
              'n':[0,1,0,1,1], 
              'o':[0,1,1,0,0], 
              'p':[0,1,1,0,1], 
              'q':[0,1,1,1,0], 
              'r':[0,1,1,1,1], 
              's':[1,0,0,0,0], 
              't':[1,0,0,0,1], 
              'u':[1,0,0,1,0], 
              'v':[1,0,0,1,1], 
              'z':[1,0,1,0,0], 
              '0':[1,0,1,0,1], 
              '1':[1,0,1,1,0], 
              '2':[1,0,1,1,1], 
              '3':[1,1,0,0,0], 
              '4':[1,1,0,0,1], 
              '5':[1,1,0,1,0], 
              '6':[1,1,0,1,1], 
              '7':[1,1,1,0,0], 
              '8':[1,1,1,0,1], 
              '9':[1,1,1,1,0],
              ' ':[1,1,1,1,1]}

DIMCELLA = 50
BITCODIFICA = 5
LUNGHEZZA = 12 #lunghezza finestra qr code

BIANCO = (255,255,255)
NERO = (0,0,0)

DIMENSIONI = (BITCODIFICA * DIMCELLA, LUNGHEZZA * DIMCELLA) #dimensioni della finestra

def drawGrid(string): #scrive sulla finestra di pygame la griglia
    for k in range(BITCODIFICA):
        for i in range(len(string)):
            rect = pygame.Rect(k * DIMCELLA, i * DIMCELLA, DIMCELLA, DIMCELLA)

            pygame.draw.rect(screen, BIANCO, rect, 1)

def drawQR(string, lst): #scrive sulla finestra di pygame il quadrato rappresentante uno 0 o un 1
    for k in range((len(lst))):
        for i in range(BITCODIFICA):
            rect = pygame.Rect(i * DIMCELLA, k * DIMCELLA, DIMCELLA, DIMCELLA)
            if(lst[k][i] == 0):
                pygame.draw.rect(screen, BIANCO, rect)
            else:
                pygame.draw.rect(screen, NERO, rect)


def codifica(stringa, diz): #apre il file csv, il ciclo for gira per la lunghezza della stringa
    lista = []
    with open('salvataggio.csv', 'w', newline='') as salvataggio:
        writer = csv.writer(salvataggio, delimiter=",", quoting = csv.QUOTE_ALL)

        for k in range (len(stringa)):
            lista.append(diz[stringa[k]]) #aggiungo la codifica dell'elemento alla lista
            writer.writerow([lista[-1]]) #carico l'ultimo elemento della lista nel csv
    return lista


def main():
    global screen

    listaFinale = []

    stringaIniziale = input("inserisci una stringa: ")
    while len(stringaIniziale) > LUNGHEZZA: #controllo per le 12 lettere/numeri al massimo
        stringaIniziale = input("inserisci una stringa: ")

    listaFinale = codifica(stringaIniziale, dizionario)
    print(listaFinale)
        
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONI)
    screen.fill(NERO)

    while True:
        drawGrid(stringaIniziale)
        drawQR(stringaIniziale, listaFinale)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
