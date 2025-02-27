#Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra.
#Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

productos = []
precios = []

for i in range(5):
    producto = input(f"Ingresa producto {i+1}/{5}: ")
    productos.append(producto)
    precio = int(input(f"Ingresa el precio {i+1}/{5}: "))
    precios.append(precio)

mayor = precios[0]
cantidad = 0
for i in range(len(precios)):
    if precios[i]>mayor:
        cantidad+=1
        mensaje = f"Cantidad de productos con un precio mayor al primer producto ingresado: {cantidad}"
print(mensaje)
