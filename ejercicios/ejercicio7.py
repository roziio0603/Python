##ROCIO
##EJERCICIO 7
URGENCIA = 0.37
PEDIATRIA = 0.42
TRAUMATOLOGIA = 0.21
print("Desea calcular presupuesto")
salida = input("Ingresar presupuesto 1-si \n 2-no")
while salida != 2:
    presupuesto = int(input("Ingresar cantidad"))
    print("La cantidad de urgencias es:.{}".format(presupuesto * URGENCIA))
    print("La cantidad de pediatria es:.{}".format(presupuesto * PEDIATRIA))
    print("La cantidadde traumatologia es:.{}".format(presupuesto * TRAUMATOLOGIA))
    salida = input("Ingresar presupuesto 1-si \n 2-no")
print ("Gracias")
