#Crear una lista por asignacion.
#La lista tiene que tener 2 elementos. Cada elementos debe ser una lista de 5 enteros
#Calcular y mostrar la suma de cada lista contenida en la lista principal

lista = [[1,1,1,1,1],[2,2,2,2,2]]

suma1 = lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
suma2 = lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print(suma1),print(suma2)
print()
suma3 = 0
suma4 = 0
for i in range(len(lista[0])):
    suma3+=lista[0][i]
print(suma3)

for i in range(len(lista[1])):
    suma4+=lista[1][i]
print(suma4)
print()
for i in range(len(lista)):
    suma = 0
    for x in range(len(lista[i])):
        suma+=lista[i][x]
print(suma)
