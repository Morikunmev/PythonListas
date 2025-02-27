#Crear dos listas paralelas
#En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado
#Ingresar por teclado cuando inicia el programa a la cantidad de empleados de la empresa
#Borrar luego todos los empleados que tiene un sueldo mayor a 100000 (tanto el sueldo como su nombre)

empleados = []
sueldos = []

cant = int(input("Ingresa la cantidad de empleados: "))
for i in range(cant):
    empleado = input(f"Ingresa el empleado nro {i+1}/{cant}: ")
    empleados.append(empleado)
    sueldo = int(input(f"Ingresa el sueldo del empleado {empleado}: "))
    sueldos.append(sueldo)

posicion = 0
while posicion <len(empleados):
    if sueldos[posicion]>10000:
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion+=1
for i in range(len(empleados)):
    print(empleados[i], sueldos[i])
