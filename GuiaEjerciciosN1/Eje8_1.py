def cargar_datos():
    lista_edad =[]
    lista_nombre = []
    acumular = 0
    promedio = 0
    for x in range(5):
        nombre = input(f"Ingrese el nombre de la persona {x}: ")
        lista_nombre.append(nombre)
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        lista_edad.append(edad)

    print("---------------------------------- \n")

    for i in range(5):
        acumular = acumular + lista_edad[i]
        if(lista_edad[i] >= 18):
            print(f"{lista_nombre[i]} es mayor de edad")

    promedio = acumular / 5
    print(f"El promedio de edad es:{promedio} ")    


cargar_datos()