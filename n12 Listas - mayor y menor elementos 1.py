#Crear un cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista

lista = []
for i in range(5):
    valor = int(input(f"Ingresa {i+1}/{5}: "))
    lista.append(valor)

mayor = 0
for i in lista:
    if i>mayor:
        mayor = i
print(f"El mayor es: {mayor}")

#Otra forma

lista1 = []
for x in range(5):
    valor1 = int(input(f"Ingresa: "))
    lista1.append(valor1)

mayor1 = lista[0]
for x in range(1,5):
    if lista1[x] >mayor1:
        mayor1 = lista1[x]
print("Lista Completa")
print(lista)
print("Mayor de la lista")
print(mayor1)
