#Definir una lista y almacenar los nombres de 3 empleados
#Por otro lado definir otra lista y almacenar en cada elemento una sublista con los numeros de dias del mes que el empleado falto
#Imprimir los nombres de empleados y los dias que falto
#Mostrar los empleados con las cantiad de inasistencias
#Finalmente mostrar el nombre o los nombres de empleados que faltaron menos dias

empleados = []
faltas = []
for k in range(3):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    cant = int(input(f"Indique cuantos dias falto el empleador {nombre}: "))
    faltas.append([])
    for x in range(cant):
        dia = input("Ingrese el numero de dias que falto: ")
        faltas[k].append(dia)

print("Nombre de empleados y dias que falto")
for x in range(3):
    print(empleados[x])
    for k in range(len(faltas[x])):
        print(faltas[x][k])

print("Nombre del empleado y la cantidad de inasistencias")
for x in range(3):
    print(empleados[x],len(faltas[x]))

menor = len(faltas[0])
for i in range(1,3):
    if len(faltas[i])<menor:
           menor = len(faltas[i])
print("Empleado o empleados que faltaron menos")
for i in range(3):
    if len(faltas[i])==menor:
        print(empleados[i])
