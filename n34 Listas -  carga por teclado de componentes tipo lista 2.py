empleados = []
sueldos = []
total_sueldos = []

for i in range(3):
    empleado = input(f"Ingresa el empleado nro {i+1}/{3}: ")
    empleados.append(empleado)
    print(empleados)
    sueldos_empleado = []
    for y in range(3):
        sueldo = int(input(f"Ingresa el sueldo {y+1}/{3} del empleado nro {i+1}/{3}: "))
        sueldos_empleado.append(sueldo)
    sueldos.append(sueldos_empleado)
for i in range(len(empleados)):
    print(empleados[i], sueldos[i][0],sueldos[i][1],sueldos[i][2])
print()
for i in range(3):
    total = sueldos[i][0]+sueldos[i][1]+sueldos[i][2]
    total_sueldos.append(total)
print()
for x in range(3):
    print(empleados[x],total_sueldos[x])

posmayor = 0
mayor = total_sueldos[0]

for x in range(len(empleados)-1):
    if total_sueldos[x]>mayor:
        mayor = total_sueldos[x]
        posmayor = x
print("El empleado con mayor ingreso es los ultimos 3 meses")
print(empleados[posmayor])
print("Con un ingreso: ",mayor)

    
