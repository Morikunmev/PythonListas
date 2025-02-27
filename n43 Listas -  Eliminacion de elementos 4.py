#Crear una lista de 5 enteros y cargarlos por teclado.
#Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores

enteros = []
for i in range(5):
    valor = int(input(f"Ingresa un valor {i+1}/{5}: "))
    enteros.append(valor)
    print(enteros)

nuevos = []

x = 0
while x <len(enteros):
    if enteros[x]>=10:
        nuevos.append(enteros.pop(x))
    else:
        x+=1
print("Lista principal actualizada")
print(enteros)
print("Lista nueva")
print(nuevos)
