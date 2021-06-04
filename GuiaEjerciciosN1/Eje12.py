#Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si
#comienza con vocal dicho nombre.

nombre=input("INGRESE UN NOMBRE:")

if nombre[0]=="a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print("EL NOMBRE INGRESADO COMIENZA CON VOCAL...")
else:
    print("EL NOMBRE INGRESADO NO COMIENZA CON VOCALES O ESTA EN MAYUSCULAS")
    