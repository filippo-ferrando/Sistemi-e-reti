def recur_fibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(recur_fibo(n-1) + recur_fibo(n-2))  
nterms = int(input("Inserisci la lunghezza: "))  

if nterms <= 0:  
    print("Numero inserito non valido")  
else:  
    print("Sequenza: ")  
    for i in range(nterms):  
        print(recur_fibo(i))  