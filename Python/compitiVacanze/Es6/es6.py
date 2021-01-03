def anomalia(diz,y1,y2): # y --> year ; y1 --> year1
    
    max = diz[str(y1)]
    min = diz[str(y1)]

    for year in diz: 

        if(int(year) >= int(y1) and int(year)<=int(y2)):

            if(max<diz[year]):
                max = diz[year]

            elif(min>diz[year]):
                min = diz[year] 

    print("\nMassimo: "+str(max) +" Minimo: "+ str(min)) 



if __name__ == "__main__":

    file = open("annual.csv",'r')
    cnt = 0
    temp = 0

    y1 = 0
    y2 = 0

    year = {}

    for line in file:

        try:
            if (cnt%2 == 0):
                temp = float(line.split(',')[2])
            else:
                year[line.split(',')[1]] = (float(temp) + float(line.split(',')[2]) )/2
            cnt = (cnt+1)%2
        except:
            pass 
              
    anomalia(year,y1=input("Inserisci il primo anno: "),y2=input("Inserisci il secondo anno: ")) 

    file.close()
