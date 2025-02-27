#En un curso de 4 alumnos se registraron las notas de sus examenes y se deben procesar de acuerdo a lo siguiente:
#a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
#b) Realizar un listado que muestre los nombres, notas y condicion del alumno.
#En la condicion, colocar "Muy Bueno" si la nota es mayor o igual a 8,
#"Bueno" si la nota esta entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
#C) Imprimir cuantos alumnos tienen la leyenda "Muy Bueno"

nombres = []
notas = []
condicion = []

for i in range(4):
    nombre = input("Ingresa el nombre: ")
    nombres.append(nombre)
    nota = int(input("Ingresa la nota: "))
    notas.append(nota)

contador=0
for i in range(len(notas)):
    if notas[i]>= 8:
        condicion.append("Muy bueno")
        contador +=1
    elif 4<=notas[i]<=7:
        condicion.append("Bueno")
    else:
        condicion.append("Insuficiente")
print(f"Los alumnos Muy buenos son: {contador}")

print(f"Listado completo")
for i in range(len(condicion)):
    if condicion[i] == "Muy bueno":
        print(nombres[i], condicion[i])
