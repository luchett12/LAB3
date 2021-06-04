def carga():
    n1 = int (input ("PRIMER VALOR:"))
    n2 = int (input ("SEGUNDO VALOR:"))
    return n1,n2
def suma(n1,n2):
    return (n1 + n2)
def mensaje():
    print("PROGRAMA FINALIZADO")

val = carga()
print("VALOR DE LA SUMA: ", suma( val[0], val[1]))
mensaje()
