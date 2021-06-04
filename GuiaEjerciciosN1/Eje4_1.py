def cuadrado():
    print("Ingrese el valor de los lados del cuadrado:")
    lados = int(input())

    print("Seleccione una opcion: 1. Calcular perimetro - 2. Calcular area ")
    opcion = int(input())
    if(opcion == 1):
        print(f"El perimetro es: {lados*4}")
    if(opcion == 2):
        print(f"El area es: {lados**2}")
cuadrado()