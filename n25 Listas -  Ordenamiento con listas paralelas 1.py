#Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas
#Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos


alumnos = []
notas = []


for i in range(10):
    if 0<=i<=4:
        alumno = input(f"Ingresa el nombre del alumno {i+1}/{5}: ")
        alumnos.append(alumno)
    else:
        nota = int(input(f"Ingresa la nota del alumno {i-len(alumnos)+1}/{5}: "))
        notas.append(nota)
print(alumnos)
print(notas)

for i in range(len(notas)-1):
    for x in range(len(notas)-1):
        if notas[x]<notas[x+1]:
            aux = notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux

            aux2 = alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux2
print("Listado de alumnos y sus notas ordenados de mayor a menor")
for i in range(5):
    print(alumnos[i],notas[i])

