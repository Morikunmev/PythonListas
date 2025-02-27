#Crear una lista por asignacion. La lista tiene que tener 5 elementos.
#Cada elementos debe ser una lista, La primera lista tiene que tener un elemento.
#La segunda dos elementos, la tercera tre elementos y asi
#Sumar todos los valores de las listas

lista = [[1], [1,2], [3,4,5], [6,7,8,9],[10,11,12,13,14]]
print(len(lista))

suma = 0
for i in range(len(lista)):
    for x in range(len(lista[i])):
        suma+=lista[i][x]
print("La suma de todos los elementos es: ")
print(suma)
