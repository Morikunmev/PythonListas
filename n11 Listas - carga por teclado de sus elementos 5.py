#Una empresa tiene dos turnos(mañana y tarde) en los que trabajan 8 empleados
#(4 por la mañana y 4 por la tarde)
#Confeccionar un programa que permita almacenar los sueldos de los empleados en 2 listas
#Imprimir las dos listas de sueldos

mañana = []
tarde = []

for i in range(8):
    if 0<=i<=3:
        sueldo = float(input(f"Ingrese sueldo de mañana {i+1}/{4}: "))
        mañana.append(sueldo)
        print(f"Sueldo de mañana: {mañana}")
    else:
        sueldo = float(input(f"Ingrese sueldo de tarde {i-len(mañana)+1}/{4}: "))
        tarde.append(sueldo)
        print(f"Sueldo de tarde: {tarde}")

print("Sueldo de mañana")
print(mañana)
print("Sueldo de tarde")
print(tarde)
    
