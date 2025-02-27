#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades.
#Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

nombres = []
edades = []

for i in range(5):
    nombre = input(f"Ingrese nombre {i+1}/{5}: ")
    nombres.append(nombre)
    edad = int(input(f"Ingrese edad: {i+1}/{5}: "))
    edades.append(edad)

edad_mayor = []
nombre_mayor = []
for i in range(len(edades)):
    if edades[i]>=18:
        edad_mayor.append(edades[i])
        nombre_mayor.append(nombres[i])
print(f"Los nombres mayores de edad son: {nombre_mayor}")
print(f"Las edades son: {edad_mayor}")

    
    
