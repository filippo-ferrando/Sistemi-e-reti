#CICLO WHILE
#In python non si usa molto spesso il ciclo while 
contatore=0
while(contatore <len(lista)): #len() restituisce la lunghezza
    print(lista[contatore])
    contatore=contatore+1

#Ciclo che viene gestito per esempio per la gestione di robot. 
#Si tratta di un ciclo infinto
while(True):
    #bla bla

lista[1,"c","ciao",3,1415]

playlist=[1,"titolo1", "autore1"],
            [2,"titolo2", "autore2",],
            [3,"titolo3", "autore3",]

print(playlist[1][1]) #stampa solamente titolo2. Simile ad una matrice

for elemento in playlist:
    print(elemento[1])
'''
 ^ ^ ^ ^
 | | | |
ciclo che stampa solamente i titoli delle canzoni
perchè elemento fa da indice per scorrimento di playlist
mentre [1] fa puntare all secondo elemento di ogni lista
'''

#DIZIONARIO
#I dizionari sono elenchi, non ordinati, di coppie {chiave, valore}
canzone= {"numero":1, "titolo": "20 anni", "autore": "Maneskin"}
#"numero", "titolo" e "autore" sono le chiavi del dizionario
#1, "20 anni", "Maneskin" sono i valori del dizionario
print(canzone["titolo"])

#Esempio in cui uso un numero come chiave 
elenco_classe = {1:"Alladio",2:"Alpigiano",3:"Bertoglio",4:"Bongiovanni"}
print(elenco_classe[3])

#IMPORTANTE PER I FILE JSON E PER I DATABASE NOSQL

playlist=[{"numero":1, "titolo": "20 anni", "autore": "Maneskin"},
          {"numero":2, "titolo": "Titolo2 bla bla", "autore": "Mario Rossi"},
          {"numero":3, "titolo": "Titolo3 bla bla bla", "autore": "Paol Bianchi"}]

print(playlist[1]["titlo"])
voti_sistemi= {1:[8,9.5,7], 2: [8,9], 3:[10,7.5,8], 4:[9,9,7,6]}

for k in range [1,5]:
    print(f"I voti di {elenco_classe[2]} sono {voti_sistemi[2]}")

lista_numeri=[3,4,3,1,5]

lista_stringhe=[]
for numero in lista_numeri:
    lista_stringhe.append(str(numero))

print(" ".join(lista_stringhe))
#Per utilizzare la funzione join, devo trasformare tutti gli elementi della lista in stringhe
#La stringa messa prima di .join sarà la stringa che dividere ogni elemnt della lista
# append viene utilizzato per la concatenazione


def converti(lista_numeri):
    lista_stringhe=[]
    for numero in lista_numeri:
        lista_stringhe.append(str(numero)
    return " ".join(lista_stringhe)