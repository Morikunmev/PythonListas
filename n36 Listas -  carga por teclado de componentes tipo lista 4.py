#Definir dos listas de 3 elementos
#La primer lista cada elementos es una sublista con el nombre del padre y la madre de una familia
#La segunda lista esta constituida por listas con los nombres de los hijos de cada familia.
#Puede haber familias sin hijos
#Imprimir los nombres del padre, la madre y sus hijos
#Tambien imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre

padres = []
hijos = []

for i in range(3):
    padre = input("Ingrese el nombre del padre: ")
    madre = input("Ingrese el nombre de la madre: ")
    padres.append([padre,madre])
    cant = int(input("Cuantos hijos tiene la familia: "))
    hijos.append([])
    for x in range(cant):
        nombre = input("Ingresa el nombre del hijo: ")
        hijos[i].append(nombre)

print("Listado del padre, la madre y sus hijos")
for k in range(3):
    print("Padre: ", padres[k][0])
    print("Madre: ", padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijos: ",hijos[k][x])

print("Listado de padres y la cantidad de hijos")
for x in range(3):
    print("Padre: ",padres[x][0])
    print("Cantidad de hijos",len(hijos[x]))
    
