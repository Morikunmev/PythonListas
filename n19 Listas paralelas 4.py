#Realizar un programa que pida la carga de dos litas numericas enteras con 4 elementos de cada una.
#Generar una tercer lista que surga de la suma de los elementos de la misma posicion de cada lista.
#Mostrar esta tercer lista

lista1 = []
lista2 = []
lista3 = []

for i in range(4):
    num1 = int(input(f"Ingresa {i+1}/{4}: "))
    lista1.append(num1)
    num2 = int(input(f"Ingresa {i+1}/{4}: "))
    lista2.append(num2)

suma = 0
for i in range(len(lista1)):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)
print(f"La suma de las dos listas paralelas es: {lista3}")
