##Realizar el promedio de cinco notas utilizando el ciclo for

suma = 0
for i in range(1,6):
    n1 = input("Ingrese nota")
    suma = suma + int(n1)
promedio = suma /5
print("El promedio es {}".format(promedio))

