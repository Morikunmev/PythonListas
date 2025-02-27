#Se tiene la siguiente lista:
lista = [[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]
#Imprimir la lista.Luego fijar con el valor cero todos los elementos mayores a 10
#Contenidos en todos los elementos de la variable "Lista"
#Volver a imprimir la lista

print(lista)
for i in range(len(lista)):
    for x in range(len(lista[i])):
        if lista[i][x]>10:
            lista[i][x]=0
print(lista)
