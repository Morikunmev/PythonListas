#Almacenar en una lista los sueldos (valores float() de 5 operarios.
#imprimir la lista y el promedio de sueldos

sueldos = []
suma = 0
for i in range(5):
    sueldo = float(input(f"Ingrese el sueldo del operario {i+1}: "))
    sueldos.append(sueldo)
    suma+= sueldo
promedio = suma / 5
print(f"El promedio del sueldo de los 5 operarios es: {promedio}")


#forma de strings

sueldos1 = ""
suma1 = ""
for i in range(5):
    sueldo = float(input(f"Ingrese el sueldo del operario {i+1}: "))
    suma1+=str(sueldo) + " "
    lista1 = suma1.split()
    for i in range(len(lista1)):
        lista1[i] = float(lista1[i])
suma2 = 0
for i in lista1:
    suma2+= i
promedio2 = suma2 / 5
print(promedio2)
    
