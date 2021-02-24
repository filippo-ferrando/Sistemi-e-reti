import sys
import random
import csv

def dictC(nfile):
    file = open(nfile,"r")

    dict = {}
    lst = []

    for k,row in enumerate(file):
        if k>0:
            lst = row[:-1].split(',')
            dict[lst[0]] = lst[1:]
            #print(lst[1:])

    file.close
    return dict

#---------------------------------------------------------------

def trovaC(dict1, dict2):
    for e2 in dict2.keys():
        #print(f"e2: {e2}")
        for e1 in dict1.keys():
            #print(f"e1: {e1}")
            if e2 == e1:
                print(dict1[e1],dict2[e2])

#----------------------------------------------------------------

def main():
    anomalie = 'Anomalie_drone.csv'
    volo = 'Volo_drone.csv'

    dictAnomalie = dictC(anomalie)
    dictVolo = dictC(volo)

    #print(dictAnomalie)
    #print(dictVolo)

    trovaC(dictVolo, dictAnomalie)
    

if __name__ == "__main__":
    main()