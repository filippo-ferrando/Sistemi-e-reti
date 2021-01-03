sc = input("Decode: d | Encode: e --> ")
abc = "abcdefghijklmnopqrstuvwxyz"

if(sc == 'e'):
    txt = input("Inserisci testo da codificare: ")
    secret = "".join([abc[(abc.find(c)+15)%26] for c in txt])
    print(secret)
else:
    txt = input("Inserisci testo da decodificare: ")
    secret = "".join([abc[(abc.find(c)-15)%26] for c in txt])
    print(secret)
