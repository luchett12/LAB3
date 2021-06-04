def caracteres(string):
    i = 0
    for x in string:
        i = i + 1
    return i

print("Ingrese el primer nombre: ")
nombre1 = input()
print("Ingrese el segundo nombre: ")
nombre2 = input()

valor1 = caracteres(nombre1)
valor2 = caracteres(nombre2)

if(valor1 > valor2):
    print(f"El nombre con mas caracteres es{nombre1} con  {valor1}" )
else:
    print(f"El nombre con mas caracteres  {nombre2} con  {valor2}")
