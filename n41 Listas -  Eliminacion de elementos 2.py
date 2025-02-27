#Crear una lista y almacenar 10 enteros pedidos por teclado.
#Eliminar todos los elementos que sean iguales al numero entero 5


#Primera forma
lista = []
for i in range(10):
    elemento = int(input(f"Ingresa {i+1}/{10}: "))
    lista.append(elemento)

print(lista)

for i in lista:
    if i == 5:
        lista.pop(i)
print(lista)


#Segunda Forma
lista1 = []
for i in range(10):
    elemento1 = int(input(f"Ingresa {i+1}/{10}: "))
    lista1.append(elemento1)

i = 0
while i<len(lista1):
    if lista1[i]==5:
        lista1.pop(i)
    else:
        i+=1
print(lista1)
