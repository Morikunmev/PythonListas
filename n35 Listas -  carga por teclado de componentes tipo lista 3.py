#Solititar por teclado dos enteros. El primer valor la cantidad de elementos que crearemos en la lista
#El segundo valor indica la cantidad de elementos que tendra cada una de las listas internas a la lista principal
#Mostrar la lista y la suma de todos sus elementos

lista = []
elementos = int(input("Cuantos elementos tedra la lista: "))
sublista = int(input("Cuantos elementos tendran las listas internas: "))
for k in range(elementos):
    lista.append([])
    for x in range(sublista):
        valor = int(input("Ingrese valor: "))
        lista[k].append(valor)
print(lista)
suma = 0
for i in range(len(lista)):
    for x in range(len(lista[i])):
        suma +=lista[i][x]
print("La suma de todos los elementos es: ")
print(suma)
