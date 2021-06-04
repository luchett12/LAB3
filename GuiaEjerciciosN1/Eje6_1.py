def sumar_lista(lista):

    suma = 0

    for x in range(len(lista)):
        suma = suma + lista[x]
    
    return suma

def mayor_lista(lista):

    mayor = 0

    for x in range(len(lista)):
        if(lista[x]> mayor):
            mayor = lista[x]
    
    return mayor

def menor_lista(lista):

    menor = lista[3]

    for x in range(len(lista)):
        if(lista[x]< menor):
            menor = lista[x]
    
    return menor

lista =  [ 2, 1, 5, 4, 3]

print(f"La suma es: {sumar_lista(lista)}")
print(f"El mayor es: {mayor_lista(lista)}")
print(f"El menor es: {menor_lista(lista)}")
