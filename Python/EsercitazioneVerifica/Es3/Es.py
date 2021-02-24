import sys
import csv

mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

def cDictLike(file):
    
    dizLike = {}
    lst = []

    nPost = 0
    nLike = 0

    for mese in mesi:
        f = open(file, "r")
        for k,row in enumerate(f):
            if k > 0:
                lst = row.split(',')
                if mese == lst[0]:
                    #print(lst[-1]) #stampa ultimo elemento --> -1 prende l'ultimo elemento
                    nPost += 1
                    nLike += int(lst[-1])
                    dizLike[mese] = [nPost,nLike]
                    #print(dizLike)
        nPost = 0
        nLike = 0
        
        f.close()
    return dizLike

def trova(mese, diz):
    for e in diz.keys():
        if e == mese:
            print(diz[e])
            
def main():
    file = "instagram.csv"
    diz = cDictLike(file)
    mese = input("inserisci il mese da cercare: ")
    trova(mese, diz)

    
if __name__ == "__main__":
    main()