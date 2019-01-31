##Rocio

##Crear un programa que permita seleccionar entre una de dos opciones
##Convertir dolares a quetzales
##quetzales a dolares

dolar = 7.5
print ("Opciones")
print ("1. Convertir dolares a quetzales")
print ("2. Convertir quetzales a dolares")
opcion = input("Ingrese la opcion que desee realizar")

if opcion == 1:
    cantidad = input("Ingrese cantidad")
    print ("resultado")
    print (cantidad * dolar)
elif opcion == 2:
    cantidad = input("Ingrese cantidad")
    print ("resultado")
    print (cantidad / dolar)
else:
    print ("opcion no valida")

##Solicitar al usuario que escoga una de las siguientes opciones
##Sumar dos numeros, restar tres numeros, multiplicar cuatro numeros, dividir dos numeros.
##si el usuario elegi una opcion invalida hacerselo saber


##print ("Operacion a realizar")
##print ("1)suma ")
##print ("2)resta")
##print ("3)multiplicacion ")
##print ("4)division")
##
##opcion = input("Elija una operacion")
##valor1 = int(input("Ingrese numero"))
##valor2 = int(input("Ingrese numero"))    
##valor3 = int(input("Ingrese numero"))     
##valor4 = int(input("Ingrese numero"))
##if opcion  == "1":
##    suma = valor1 + valor2
##    print ("La suma es \n {}".format(suma))
##
##elif opcion == "2":
##    resta = valor1 - valor2 - valor3
##    print ("La resta es \n {}".format(resta))
##
##elif opcion == "3":
##    multiplicacion = valor1 * valor2 * valor3 * valor4
##    print ("La multiplicacion es \n {}".format(multiplicacion))
##
##elif opcion == "4":
##    multiplicacion = valor1 / valor2
##    print ("La division es \n {}".format(division))
##    
