from typing import final
import requests #Importamos la libreria request
import matplotlib.pyplot as plt #Importamos la libreria matplotlib

respuesta = requests.get("https://api.covid19api.com/countries") #Con el URL obtengo los nombres de los paises
my_data = respuesta.json()#convierte el .JSON que nos devuelve el request
paises = [] #aca tenemos todos los nombres de los paises
for x in my_data:    
    paises.append(x["Country"])#Agregamos los nombres de los paises

mes = input("Ingrese el mes deseado: ") #Pedimos que ingresse un numero de mes

todalainfo = []
casos_pais = []
muertes_pais = []
y=0 



for x in paises:    #Recorremos toda la lista de los paises ingresados anteriormente
    url = "https://api.covid19api.com/country/"+x+"?from=2020-"+mes+"-01T00:00:00Z&to=2020-"+mes+"-01T00:00:01Z" #Se envia la URL modificandola con el mes ingresado y el pais correspondiente

    url = url.replace(' ','-')#Se remplazan los espacios de los paises por guiones para el correcto funcionamiento del URL
    respu = requests.get(url) #Enviamos la peticion a la API para obtener los datos
    respu = respu.json()#convierte el .JSON que nos devuelve el request

    
    try: #comenzamos a recorrer los datos y mostrar lo obtenido 1 por 1
        pais = x
        casos = respu[0]["Confirmed"]
        muertes = respu[0]["Deaths"]
    except: #Si no existen datos de los casos y muertes en el momento se muetra 0
        casos = 0
        muertes = 0

#Se imprimen los datos
    print("\n")
    print("País: ", pais)
    print("Cantidad de casos: ", casos)
    print("Cantidad de muertes: ", muertes)
    print("\n")
    print("- " * 15)
#Asignamos a cada lista la cantidad de casos por pais
    casos_pais.insert(y,casos)
#Asignamos a cada lista la cantidad de muertes por pais

    muertes_pais.insert(y,muertes)
    y=y+1




#Graficamos con la libreria importada
fig, ax = plt.subplots()

ax.set_ylabel('Cantidad')   #etiqueta en y
ax.set_title('Cantidad de casos por Pais') #titulo del grafico
plt.bar (paises,casos_pais) #pasamos las listas para graficar
plt.savefig('Cant_casos.png') #guardamos el grafico 

plt.show() #Graficamos

ax.set_ylabel('Cantidad')   #etiqueta en y
ax.set_title('Cantidad de muertes por Pais') #titulo del grafico
plt.bar (paises,muertes_pais) #pasamos las listas para graficar
plt.savefig('Cant_muert.png') #guardamos el grafico

plt.show() #Graficamos





    

    