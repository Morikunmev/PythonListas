#Crear y cargar una lista con 5 enteros por teclados.
#Implementar un algoritmo que identifique el menor valor de la lista y la
#posicion donde se encuentra

lista = []
for i in range(5):
    valor = int(input("Ingrese: "))
    lista.append(valor)

menor = lista[0]
posicion = 0

for i in range(len(lista)):
    if lista[i]<menor:
        menor = lista[i]
        posicion = i
print(f"El menor es: {menor}")
print(f"Posicion: {posicion}")
        
