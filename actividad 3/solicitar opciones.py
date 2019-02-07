##Rocio
##Ejercicio

##Seleccione una opcion
##1.Solicitar dos numeros y elevar el primer numero al segundo
##2.Solicitar tres numeros y elevar el primero al segundo y el resultado elevarlo al tercero.

print("Bienvenidos")
opcion = input("1- Elevar el primero numero al segundo 2-Elevar el primer numero al segundo y el resultado elevado al tecero ")
elevacion = 0
if opcion == "1":
    valor1 = input("Ingrese el primer valor")
    valor2 = input("Ingrese el segundo valor")
    elevacion = int(valor1) ** int(valor2)
    print("La elevacion es {}".format(elevacion))
elif opcion == "2":
    valor1 = input("Ingrese el primer valor")
    valor2 = input("Ingrese el segundo valor")
    valor3 = input("Ingrese el tercer valor")
    elevacion = int(valor1) ** int(valor2) ** int(valor3)
    print("La elevacion es {}".format(elevacion))
else:
    print("Opcion invalida")
