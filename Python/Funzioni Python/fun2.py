#argomenti default funzioni

def operazione(x,y,tipo_operazione="+"):
    if tipo_operazione=="+":
        return x+y
    elif tipo_operazione=="-":
        return x-y
    elif tipo_operazione=="*":
        return x*y
    elif tipo_operazione=="/":
        return x/y
    else:
        return "error"

z = operazione(4,8)
print(z);

    