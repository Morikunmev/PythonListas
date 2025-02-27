#Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

sueldos = []
for i in range(5):
    valor = int(input("Ingresa sueldo: "))
    sueldos.append(valor)
print("Lista sin ordenar")
print(sueldos)

for i in range(len(sueldos)-1):
    for x in range(len(sueldos)-1):
        if sueldos[x]>sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
print(sueldos)

#Otra forma

sueldos1 = []
for i in range(5):
    valor1 = int(input("Ingresa sueldo: "))
    sueldos1.append(valor1)
for i in range(len(sueldos1) -1):
    for x in range(len(sueldos1) -1):
        if sueldos1[x]>sueldos1[x+1]:
            sueldos1[x], sueldos1[x+1] = sueldos1[x+1], sueldos1[x]
print(sueldos1)

sueldos2 = []
for i in range(5):
    valor2 = int(input("Ingrese sueldo: "))
    sueldos2.append(valor2)
for i in range(len(sueldos2)-1):
    for x in range((len(sueldos2) -1) -i):
        if sueldos2[x]>sueldos2[x+1]:
            sueldos2[x],sueldos2[x+1] = sueldos2[x+1],sueldos2[x]
print(sueldos2)
