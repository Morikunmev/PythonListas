#Definir una lista por asignacion que almacene en la primer componente el nombre de un alumno
#y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas

lista = ["Richard", 6.5, 4.5]
print(lista[0])

#primera forma con el ciclo for
suma = 0
for i in lista[1:]:
    suma+=i
promedio = suma / 2
print(promedio)

#segunda forma

promedio = (lista[1] + lista[2]) / 2
print(f"El promedio es: {promedio}")

