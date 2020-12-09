from pprint import pprint #better file print
from random import randint

header = ['numero', 'titolo', 'artista'] #header of csv

def getcsv(fname, header, separator=','): #read csv file
    lines = []
    with open(fname) as file: #open the file and close it itself
        for line in file.readlines():
            fields = line.split(separator)
            
            line_dict = {}

            for i, field in enumerate(fields):
                key = header[i] #assign to the title or number or artist the field readed
                line_dict[key] = field.strip() #eliminate the space between the lines
            lines.append(line_dict) #add the line to the list

    return lines


def shuffle(l, rep=10000): #shuffle the csv file
    lines = l[:] #clone the entire list
    for _ in range(rep): #_ is a ignorable value
        ifrom = randint(0, len(lines) - 1)
        ito = randint(0, len(lines) - 1)
        lines[ifrom], lines[ito] = lines[ito], lines[ifrom] #echange the value x times
    return lines


csvin = getcsv("canzoni.csv", header)
shuffled = shuffle(csvin)

print("\noriginal playlist: \n")
#print(*csvin, sep='\n')
pprint(csvin, sort_dicts=False)

print("\n")

print("shuffled playlist: \n")
#print(*shuffled, sep='\n')
pprint(shuffled, sort_dicts=False)
