print ("1. suma 2. resta 3. multi 4. division")
opcion = input(":.")

if opcion == "1":
    valor1 = input("Ingresa primer valor")
    valor2 = input("Ingresa segundo valor")
    suma = int(valor1) + int(valor2)
    print ("La suma es:. {}".format(suma))
elif opcion == "2":
    valor1 = input("Ingresa primer valor")
    valor2 = input("Ingrese segundo valor")
    valor3 = input("Ingrese tercer valor")
    resta = int(valor1) - int(valor2) - int(valor3)
    print ("La resta es:. {}.".format(resta))
elif opcion == "3":
    valor1 = input("Ingresa primer valor")
    valor2 = input("Ingresa segundo valor")
    valor3 = input("Ingresa tercer valor")
    valor4 = input("Ingresa cuarto valor")
    multi = int(valor1) * int(valor2) * int(valor3) * int(valor4)
    print ("La multi es:. {}".format(multi))
elif opcion == "4":
    valor1 = input("Ingresa primer valor")
    valor2 = input("Ingresa segundo valor")
    division = int(valor1) / int(valor2)
    print ("La division es:. {}".format(division))
else:
    print("Opcion no valida")
