#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores: float)
#Obtener el promedio de las mismas. Contar cuantas personas son mas altas que el promedio y cuantas mas bajas

alturas = []
suma = 0
for i in range(5):
    altura = float(input("Ingrese la altura de la persona {}: ".format(i+1)))
    suma+= altura
    alturas.append(altura)

promedio = round(suma / 5,2)
print("La altura de las personas es: ")
print(alturas)
print(f"El promedio es: {promedio}")

contador=0
contador2 = 0
lista1 =[]
lista2 = []
for i in alturas:
    if i>=promedio:
        contador+=1
        lista1.append(i)
    else:
        contador2+=1
        lista2.append(i)

print(f"Las personas mas altas del promedio son: {contador}")
print(lista1)
print(f"Las personas mas bajas del promedio son_ {contador2}")
print(lista2)
