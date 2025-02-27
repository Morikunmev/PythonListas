#Cargar una lista con 5 elementos enteros.
#Ordenarla de menor a mayor y mostrarla por pantalla
#Hago ordenar de mayor a menor e imprimir nuevamente

elementos = []
for i in range(5):
    valor = int(input("Ingresa: "))
    elementos.append(valor)

for i in range(len(elementos) -1):
    for x in range(len(elementos)-1):
        if elementos[x]>elementos[x+1]:
            aux = elementos[x]
            elementos[x]=elementos[x+1]
            elementos[x+1]= aux
print("Ordenado de menor a mayor")
print(elementos)

for i in range(len(elementos) -1):
    for x in range(len(elementos) -1):
        if elementos[x]<elementos[x+1]:
            aux = elementos[x]
            elementos[x]=elementos[x+1]
            elementos[x+1]=aux
print("Ordenado de mayor a menor")
print(elementos)
