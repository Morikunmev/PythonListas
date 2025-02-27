#Definir una lista vacia y luego solicitar la carga de 5 enteros por teclado
#y añadirlos a la lista. Imprimir la lista generada

lista = []
print(len(lista))

for i in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista.append(valor)
print(lista)

lista1 = ""
for i in range(5):
    lista1+= str(i) + " "

lista1 = lista1.split()
for i in lista1:
    i = int(i)
print(lista[0] + lista[1])

