#Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
#Finalizar la carga de enteros al ingresar el cero.
#Mostrar finalmente el tamaño de la lista y el contenido de la lista

lista = []
valor = int(input("Ingresar un valor (0 para finalizar): "))
while valor!=0:
    lista.append(valor)
    valor = int(input("Ingresar un valor (0 para finalizar): "))

print("Contenido de la lista")
print(lista)
print("Tamaño de la lista")
print(len(lista))

lista1 = ""
valor = int(input("Ingresar un valor"))
while valor !=0:
    lista1+= str(valor) + " "
    lista2 = lista1.split()
    for i in range(len(lista2)):
        lista2[i] = int(lista2[i])
    print(lista2)
    valor = int(input("Ingresar un valor"))
print(lista2[0] + lista2[1])
