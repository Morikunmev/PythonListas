#Solicitar por teclado la cantidad de empleados que tiene la empresa.
#Crear y cargar una lista con todos los sueldos de dichos empleados.
#Imprimir la lista de sueldos ordenados de menor a mayor

n = int(input("Ingresa la cantidad de empleados de la empresa: "))
sueldos = []
for i in range(n):
    sueldo = int(input(f"Ingresa el sueldo del empleado {i+1}/{n}: "))
    sueldos.append(sueldo)

for i in range(len(sueldos)-1):
    for x in range((len(sueldos)-1)-i):
        if sueldos[x] > sueldos[x+1]:
            sueldos[x], sueldos[x+1] = sueldos[x+1], sueldos[x]
print("Sueldos ordenados: ")
print(sueldos)
