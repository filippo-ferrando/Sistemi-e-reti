def forward(x):
    print(f"vado avanti di {x}")

def backward(x):
    print(f"vado indietro di {x}")

def left(x):
    print(f"vado a sinistra di {x}")

def right(x):
    print(f"vado a destra di {x}")

def main():
    lista = [("f", 30), ("r", 40), ("l", 58), ("b", 67), ("f", 98)]

    dizionarioFunz = {"f":forward, "b":backward, "r":right, "l":left}

    for movimento, val in lista:
        dizionarioFunz[movimento](val)



if __name__ == "__main__":
    main()
    