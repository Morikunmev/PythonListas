#Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o mas posiciones en la lista)

##lista = []
##for i in range(5):
##    nombre = int(input("Ingresa: "))
##    lista.append(nombre)
##
##mayor = lista[0]
##mensaje = 0
##for i in range(len(lista)):
##    if lista[i]>mayor:
##        mayor = lista[i]
##        mensaje = f"{mayor} es es el mayor"
##print(mensaje)
##
##contador = 0
##for i in range(len(lista)):
##    if lista[i]==mayor:
##        contador+=1
##if contador >1:
##    print("El valor mayor se encuentra repetido en la lista")



lista = []
for i in range(5):
    valor = int(input("Ingresa: "))
    lista.append(valor)
mayor = lista[0]
contador = 0
for i in range(len(lista)):
    if lista[i]>mayor:
        mayor = lista[i]
    if lista[i] == mayor:
        contador+=1
if contador>1:
    print("El valor mayor se encuentra repetido en la lista")
