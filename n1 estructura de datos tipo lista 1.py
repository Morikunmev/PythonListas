#definir una lista que almacene 5 enteros. Sumar todos suss elementos y mostrar la suma

#dos formas con el ciclo for
numero = [2,4,5,6,6]
suma = 0
for i in numero:
    suma+=i
print(suma)

suma1 = 0
for x in range(len(numero)):
    suma1+=numero[x]
print(suma1)

#forma con el ciclo while
i = 0
suma2 = 0
while i<len(numero):
    suma2+=numero[i]
    i+=1
print(suma2)


