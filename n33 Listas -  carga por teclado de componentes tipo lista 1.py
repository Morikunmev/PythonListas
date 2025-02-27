#Crear y cargar una lista con los nombres de tres alumnos.
#Cada alumno tiene dos notas, almacenar las notas en una lista paralela.
#Cada componente de la lista paralela debe ser tambien una lista con dos notas
#Imrpimir luego cada nombre y sus dos notas

nombres = []
notas = []

for i in range(3):
    nombre = input(f"Ingresa el el nombre {i+1}/{3}: ")
    nombres.append(nombre)
    nota1 = int(input(f"Ingresa la nota 1 del alumno {i+1}/{3}: "))
    nota2 = int(input(f"Ingresa la nota 2 del alumno {i+1}/{3}: "))
    notas.append([nota1,nota2])

for i in range(len(nombres)):
    print(nombres[i], notas[i][0],notas[i][1])
