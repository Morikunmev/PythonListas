#Se debe crear y cargar una lista donde se almacenan 5 sueldos.
#Desplazar el valor mayor de la lista a la ultima posicion

sueldos = []
for i in range(5):
    valor = int(input("Ingresa: "))
    sueldos.append(valor)
print("Lista original")
print(sueldos)

for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1]=aux
print("La lista tiene el ultimo elemento ordenado")
print(sueldos)

#Otra forma

sueldos1 = []
for i in range(5):
    valor1 = int(input("Ingresa: "))
    sueldos1.append(valor1)

for x in range(len(sueldos1) - 1):
    if sueldos1[x]>sueldos1[x+1]:
        sueldos1[x],sueldos1[x+1] = sueldos1[x+1],sueldos1[x]

print(sueldos1)
