my_list = []
mayor = 0

for x in range(5):
    val = int(input("Ingrese un numero entero: "))
    my_list.append(val)
    
for x in my_list:
    if x > mayor:
        mayor = x
        
    print("El mayor numero ingresadi es {}".format(mayor))