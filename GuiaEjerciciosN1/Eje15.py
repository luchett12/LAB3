#Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

#1.)Ingrese tres números que indican el nivel de audiencia o rating de tres programas de televisión, y cargue también los nombres de esos tres programas. Determine y muestre el nombre de programa con menor rating (muestre también ese rating menor). Si el menor rating es a su vez inferior a 4, muestre un mensaje indicando que ese programa debe ser removido de la programación.

#2.)Ingrese por teclado una secuencia de n números enteros (n se carga también por teclado), a razón de uno por vuelta de ciclo. Determine el promedio de todos los números cargados que hayan sido mayores que cero. Informe si ese promedio es menor, igual o mayor que un valor x que se carga por teclado.

#3.)Terminar el programa.

menu = 'Menu de Opciones \n' \
      '----------------------------- \n' \
      '1 ----------- Nivel de audiencia de programas de TV\n' \
      '2 ----------- Procesar numeros enteros\n' \
      '0 ----------- Salir\n' \
      'Ingrese su opcion: '

men = 0
menor = 0
opcion = 0

while opcion != 3:
    opcion = int(input(menu))

    if opcion == 1:
      nombre_programa1 = input("ingrese el nombre del primer programa: ")
      nivel_audiencia1 = int(input("ingrese el nivel de audiencia del primer programa de TV: "))
      nombre_programa2 = input("ingrese el nombre del segundo programa: ")
      nivel_audiencia2 = int(input("ingrese el nivel de audiencia del segundo programa de TV: "))
      nombre_programa3 = input("ingrese el nombre del tercer programa: ")
      nivel_audiencia3 = int(input("ingrese el nivel de audiencia del tercer programa de TV: "))

        if nivel_audiencia1 < nivel_audiencia2 and nivel_audiencia1 < nivel_audiencia3:
            men = nivel_audiencia1
            menor = nombre_programa1
        elif nivel_audiencia2 < nivel_audiencia3:
            men = nivel_audiencia2
            menor = nombre_programa2
        else:
            men = nivel_audiencia3
            menor = nombre_programa3

        print ("el menor es: ", menor)

        if men < 4:
            print("debe ser removido de la programacion!")


    else opcion ==2:
        n = 0
        acu = 0
        n = int(input("Ingrese la cantidad de numeros enteros que quiere cargar: "))
        print("flag", n)

        for x in range(n):
            aux = int(input("Ingrese un entero: "))
            acu += aux
        print("los enteros ingresados son: ", acu)