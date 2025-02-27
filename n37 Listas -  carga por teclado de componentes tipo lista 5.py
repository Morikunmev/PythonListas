#Se desea saber la temperatura media trimenstral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
#Se debe ingresar el nombre del pais y seguidamente las tres temperaturasmedias mensuales.
#Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
#A - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales
#B - imprimir los nombres de los paises y las temperaturas medias mensuales de las mismas
#C - Calcular la temperatura media trimestral de cada pais.
#D - Imprimir los nombres de los paises y las temperaturas medeias trimestrales
#E - Imprimir el nombre del pais con la temperatura media trimestral mayor

paises = []
temperaturas = []
promediotemp = []
for x in range(4):
    nombre = input(f"Ingresa el nombre del pais: ")
    paises.append(nombre)
    temperaturas.append([])
    for i in range(3):
        temp =int(input(f"Ingresa la temperatura {i+1}/{3}: "))
        temperaturas[x].append(temp)
print("Paises y temperaturas medias de los ultimos 3 meses: ")
for x in range(4):
    print(paises[x], temperaturas[x][0],temperaturas[x][1],temperaturas[x][2])

for x in range(4):
    promedio = (temperaturas[x][0] +temperaturas[x][1]+temperaturas[x][2]) / 3
    promediotemp.append(promedio)

print("Listado de paises y temperaturas medias trimestrales")
for x in range(4):
    print(paises[x], promediotemp[x])

posmayor = 0
for x in range(1,4):
    if promediotemp[x]>promediotemp[posmayor]:
        posmayor = x
print("Pais con temperatura media trimestral mayor",paises[posmayor])
