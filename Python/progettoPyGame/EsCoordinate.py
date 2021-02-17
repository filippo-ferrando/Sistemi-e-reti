import sys

'''
stanza rettangolare piastrellata (matrice)
robot si muove nella stanza
ostacoli nella stanza
robot in certo punto nella stanza
robot si muove avanti, dietro, destra, sinistra
dato pavimento con ostacoli produco dizionario 
{0: [1,5], ... #nella cella 0 può andare nelle celle vicine libere
'''

def main():

    pavimento = [[0, 0, 0, -1, -1, 0, -1], #0 libero -1 occupato
                [-1, 0, 0, 0, -1, -1, 0], 
                [0, 0, -1, -1, -1, 0, 0], 
                [-1, 0, 0, 0, -1, -1, 0], 
                [-1, 0, 0, 0, 0, -1, -1], 
                [-1, -1, -1, 0, 0, 0, -1]]  

    dizPos = {} #futuri possibili movimenti

    

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

                dizPos[pavimento[cordx][cordy]] = lElemento

    print(dizPos)



                        

    

if __name__ == "__main__":
    main()