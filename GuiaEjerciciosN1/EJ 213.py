my_list= []
mayor = 0

for x in range(5):
    val = input ("Ingrese un nombre: ")
    my_list.append(val)
     
my_list.sort()

print ("El primer nombre en orden alfabetico es: {}".format(my_list[0]))