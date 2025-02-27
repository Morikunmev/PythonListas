#Crear una lista por asignacion.
#La lista tiene que tener cuatro elementos. Cada elementos debe ser una lista de 3 enteros
#Imprimir sus elementos accediendo de diferentes modos

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista)

#imprimir la primer componente
print(lista[0])
print(lista[0][0])
print()
for i in range(len(lista[0])):
    print(lista[0][i])

print()
for i in range(len(lista)):
    for x in range(len(lista[i])):
        print(lista[i][x])
