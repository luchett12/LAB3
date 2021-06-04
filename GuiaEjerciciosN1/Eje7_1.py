def retornar_lista():
    lista = []
    for x in range(5):
         valor = int(input(f"Ingrese el valor {x} de la lista:"))
         lista.append(valor)

    return lista

def lista_mayor(lista):
    for x in range(len(lista)):
        if(lista[x]>10):
            print(lista[x])
            print("----------------")

    


lista = [15,2,24,3,5,12,45]

print(retornar_lista())
print("Valores mayores a 10: ")
lista_mayor(lista)

