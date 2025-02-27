#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
#Mostrar el nombre de persona menor en orden alfabetico

lista = []
for i in range(5):
    valor = input("Ingresa: ")
    lista.append(valor)

menor = lista[0]
nombre_menor = 0
for i in range(5):
    if lista[i] < menor:
        menor = lista[i]
        nombre_menor= i
print(lista)
print(menor)
print(nombre_menor)

