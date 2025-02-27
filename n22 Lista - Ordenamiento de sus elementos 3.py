#Crear una lista y almacenar los nombres de 5 paises. Ordenar alfabeticamente la lista e imprimirla

paises = []
for i in range(5):
    pais = input("Ingresa pais: ")
    paises.append(pais)

for i in range(len(paises) -1):
    for x in range(len(paises) -1):
        if paises[x]>paises[x+1]:
            paises[x], paises[x+1] = paises[x+1], paises[x]
print(paises)
paises = []
