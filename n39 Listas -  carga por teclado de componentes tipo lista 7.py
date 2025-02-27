#Desarrollar un programa que cree una lista de 50 elementos.
#El primer elementos es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
#La lista deberia tener esta estructura y asignarle esos valores a medida que se crean los elementos.

lista = []
cant = 1
for i in range(50):
    lista.append([])
    valor = 1
    for x in range(cant):
        lista[i].append(valor)
        valor = valor +1
    cant = cant +1

print(lista)
print()
lista=[]
for k in range(50):
    lista.append([])
    for x in range(k+1):
        lista[k].append(x+1)
print(lista)
