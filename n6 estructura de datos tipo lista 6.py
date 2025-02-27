#Definir una lista que almacene por asignacion los nombres de 5 personas.
#Contar cuantos de esos nombres tienen 5 o mas caracteres.

personas = ["juan", "ana" ,"marcos", "carlos", "luis"]

for i in range(len(personas)):
    if len(personas[i]) >= 5:
        print(f"{personas[i]} tiene 5 o mas caracteres")
    else:
        print(personas[i])
print()

x = 0
cantidad = ""
while x <len(personas):
    if len(personas[x]) >=5:
        cantidad+=personas[x] + " "
    x+=1

cantidad = cantidad.split()
print(cantidad)
