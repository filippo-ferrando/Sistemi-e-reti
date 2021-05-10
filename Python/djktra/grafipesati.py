from numpy import Infinity as INFINITE

'''
a 1
b 2
c 3
d 4
e 5
f 6
g 7
h 8
i 9
j 10 
k 11 
l 12
m 13
n 14
o 15
'''

dizionario = {
    0:[(3,1),(4,4),(7,10)],
    1:[(2,2),(5,1)],
    2:[(1,2),(5,1)],
    3:[(0,4),(7,1)],
    4:[(0,1),(7,5),(5.3)],
    5:[(1,1),(4,3),(6,7),(8,1),(2,3)],
    6:[(5,7),(9,1)],
    7:[(0,10),(3,1),(4,5),(8,9)],
    8:[(7,9),(5,1),(9,2)],
    9:[(6,1),(8,2)]

}

def dijkstra(start, diz):
    label = {key : INFINITE for key,_ in dizionario.items()}
    label[start] = 0

    node=[start]

    while len(node):
        #cerco tra i nodi in node (label più piccola)   FOR
        #nodo trovato = nodo corrente

        #controllo adiacenze nodo corrente FOR
        #per ogni adiacenza calcolo la nuova label (solo se label trovata < di label già presente) FOR
        

def main():
    start = input("Inserire nodo partenza: ")

    dijkstra(start,dizionario)
