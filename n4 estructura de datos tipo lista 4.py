#Definir por asignacion una lista con 8 elementos enteros.
#Contar cuantos dichos valores almacenan un valor superior a 100

numeros = [2,3,4,102,6,105,100,4]
superior = ""
for i in numeros:
    if i >100:
        print("valor superior a 100!")
        superior+=str(i) + " "
    else:
        print("-")

print("Ese numero es: ")
superior = [int(i) for i in superior.split()]
print(superior)
print(f"serian {len(superior)} elementos en total")
