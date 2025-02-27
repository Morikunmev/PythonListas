#Crear y cargar en una lista los nombres de 5 paises y e otra lista paralela la cantidad de habitantes del mismo.
#Ordenar alfabeticamente e imprimir los resultados.
#Por ultimo ordenar con respecto a la cantidad de habitantes (De mayor a menor) e imprimir nuevamente.

paises = []
habitantes = []

for i in range(10):
    if 0<=i<=4:
        pais = input(f"Ingresa el pais {i+1}/{5}: ")
        paises.append(pais)
    else:
        habitante = int(input(f"Ingresa la cantidad de habitantes {i-len(paises) +1}/{5}: "))
        habitantes.append(habitante)
for i in range(len(paises)-1):
    for x in range(len(paises)-1):
        if paises[x]>paises[x+1]:
            aux = paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux

            aux = habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux

print("Paises ordenados alfabeticamente")
for i in range (len(habitantes)):
    print(paises[i], habitantes[i])

for i in range (len(habitantes)-1):
    for x in range (len(paises)-1):
        if habitantes[x]<habitantes[x+1]:
            aux = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1]=aux

            aux = paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
print("Cantidad de habitantes ordenados de mayor a menor")
for i in range (len(habitantes)):
    print(habitantes[i], paises[i])
