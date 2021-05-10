# pavimento RETTANGOLARE diviso in piastrelle
# alcune piastrelle sono "rosse" ovvero con ostacoli
# piastrelle "verdi" è dove sta il robot
# (lista di liste=matrice)
# calcolare il percorso più breve per arrivare da A a B 
# movim solo sopra sotto destra sinistra
# risultato:{0:[1,5], 1(-->dalla cella) :[0,6,2](-->posso andare in)}
#
#
# 0 = libero
# -1 = ostacolo




import pygame
import sys
from pygame.locals import *
from numpy import Infinity as INFINITE
import time



pavimento=[[-1,0,0,-1,-1],
           [-1,0,0,0,-1],
           [0,0,-1,-1,-1],
           [0,0,-1,0,0], 
           [-1,0,0,0,-1],
           [-1,0,0,0,0]]

dimensione=50
matriceTrasform=[]
dizio={}
cellaRobot=0
XGR=len(pavimento[0])*dimensione
YGR=len(pavimento)*dimensione
#RGB
NERO=(0, 0, 0)
VERDE=(0,255, 0)
BIANCO=(255, 255, 255)
ROSSO=(255, 0, 0)


def drawgrid():
    fnt = pygame.font.SysFont("Arial", 15)
    for x in range (0, XGR, dimensione):
        for y in range (0, YGR, dimensione):
            piastrella=pygame.Rect(x, y, dimensione, dimensione)
            pygame.draw.rect(screen,  NERO, piastrella, 1)
            if pavimento[int(y/dimensione)][int(x/dimensione)]==-1:
                ostacolo=pygame.Rect(x, y, dimensione, dimensione)  
                pygame.draw.rect(screen, ROSSO, ostacolo) 
            else:
                scritta=""
                if pavimento[int(y/dimensione)][int(x/dimensione)]<10:
                    scritta=scritta+"0"
                scritta=scritta+str(pavimento[int(y/dimensione)][int(x/dimensione)])
                surf_text = fnt.render(scritta, True, (255, 255, 255))
                screen.blit(surf_text, (int(x+dimensione/3), int(y+dimensione/3)))
                pygame.display.flip()

    





def numerazion():
    global pavimento
    numer=0
    global cellaRobot
    for n in range(0, len(pavimento)):
        for i in range(0, len(pavimento[n])):
            if pavimento[n][i]!=-1:
                pavimento[n][i]=numer
                numer=numer+1
    cellaRobot=numer-1

'''
def creamatr():
    for i in dizio:
        sost=[]
        for j in range(XGR):
            if j in i:
'''


def creaDiz():
    #lista=[[0,1], [0,-1], [-1,0], [1,0]]
    global pavimento
    global dizio
    listaPoss=[]
    for n in range(0, len(pavimento)):
        for i in range(0, len(pavimento[n])):
            if pavimento[n][i]!=-1:
                if n!=0:
                    if pavimento[n-1][i]!=-1:
                        listaPoss.append((pavimento[n-1][i],1))
                if i!=0:
                    if pavimento[n][i-1]!=-1:
                        listaPoss.append((pavimento[n][i-1],1))   
                if i!=(len(pavimento[n])-1):
                    if pavimento[n][i+1]!=-1:
                        listaPoss.append((pavimento[n][i+1],1))
                if n!=(len(pavimento)-1):
                    if pavimento[n+1][i]!=-1:
                        listaPoss.append((pavimento[n+1][i],1))
                dizio[pavimento[n][i]]=listaPoss
                listaPoss=[]
            
def drawRob():
    global cellaRobot
    drawgrid()
    for i in range(len(pavimento)):
        for j in range(len(pavimento[i])):
            if cellaRobot==pavimento[i][j]:
                robottino=pygame.Rect(j*dimensione, i*dimensione, dimensione, dimensione) 
                pygame.draw.rect(screen, VERDE, robottino) 
            elif pavimento[i][j]!=-1:
                piastrella=pygame.Rect(j*dimensione, i*dimensione, dimensione, dimensione)
                pygame.draw.rect(screen,  NERO, piastrella)
            


def moveRight():
    global cellaRobot
    if (cellaRobot+1) in dizio[cellaRobot]:
        cellaRobot=cellaRobot+1
    else:
        print("hai sbattuto a destra")


def moveLeft():
    global cellaRobot
    if (cellaRobot-1) in dizio[cellaRobot]:
        cellaRobot=cellaRobot-1
    else:
        print("hai sbattuto a sinistra")

def moveUp():
    global cellaRobot
    if  dizio[cellaRobot][0]!=(cellaRobot-1) and dizio[cellaRobot][0]<cellaRobot:
        cellaRobot=dizio[cellaRobot][0]
    else:
        print("hai sbattuto a sopra")

def moveDown():
    global cellaRobot
    if  dizio[cellaRobot][-1]!=(cellaRobot+1) and dizio[cellaRobot][-1]>cellaRobot:
        cellaRobot=dizio[cellaRobot][-1]
    else:
        print("hai sbattuto a sotto")


def dijkstra(start, graph, predecessor={}):
    dizLabel = {}
    nodeList = [start]  
    deletedList = []

    for node in graph:
        dizLabel[node] = INFINITE
    
    dizLabel[start] = 0

    while len(nodeList) > 0:
        currentLable = INFINITE
        #cerco tra i nodi presenti in nodelist quello che ha la label più piccola  
        #il nodo trovato sarà il nodo corrente
        for node in nodeList:
            if dizLabel[node] < currentLable:
                currentLable = dizLabel[node]
                currentNode = node

        nodeList.remove(currentNode)
        deletedList.append(currentNode)

        #trovo le adicenze a partire dal nodo corrente      
        for node, label in graph[currentNode]:
            if not(node in deletedList) and not(node in nodeList):
                nodeList.append(node)
            #per ogni adiacenza calcolo la nuova label aggiornando il dizionario label solo se la label trovata 
            #risulta più piccola di quella già trovata    
            if label + dizLabel[currentNode] < dizLabel[node]:
                dizLabel[node] = dizLabel[currentNode] + label
                predecessor[node] = currentNode

    return dizLabel, predecessor

def trovaIlPercorso():
    predecessor = {}
    start = int(input("Inserisci un nodo di partenza: "))
    finish = input("Inserisci un nodo finale: ")

    control = False

    for node in dizio:
        if start == node:
            control = True
    
    for node in dizio:
        if finish == node:
            control = True

    if control == False:
        print("Nodo/Nodi non esistente")
    else:
        dizLabel, predecessor = dijkstra(start, dizio)
        #print(f"{dizLabel}\n{predecessor}")
        percorso=calcolaPerc(predecessor, int(finish), start)
        #print(percorso)
        return(percorso)
    


def calcolaPerc(predecessor, finish, start):
    if predecessor[finish]==start:
        return [finish]
    else:
        toret= calcolaPerc(predecessor, predecessor[finish], start) + [finish]   
        return toret
    

def main():
    global cellaRobot
    #print(f"righe:{len(pavimento)} colonne: {len(pavimento[0])}")
    numerazion()
    creaDiz()
    #trovaIlPercorso()
    #print(dizio)
    #----------SCREEN----------
    global screen
    pygame.init()
    screen= pygame.display.set_mode((XGR, YGR))
    screen.fill(NERO)
    
    drawRob()
    elements = trovaIlPercorso()
    while True:
        drawgrid()
        print(elements)
        for i in range(len(elements)) :
            cellaRobot = elements[i]
            drawRob()

        time.sleep(4)
            

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==K_RIGHT :
                    moveRight()
                    drawRob()
                
                if event.key==K_DOWN :
                    moveDown()
                    drawRob()
                if event.key==K_UP:
                    moveUp()
                    drawRob()
                if event.key==K_LEFT:
                    moveLeft()
                    drawRob()
        pygame.display.update()
    

if __name__ == "__main__":
	main()