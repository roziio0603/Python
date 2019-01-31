##Rocio

##Crear un programa que permita seleccionar entre una de dos opciones
##Convertir dolares a quetzales
##quetzales a dolares

##menu = '''Menu
##        1.Convertir dolares a quetzales
##        2.Convetir quetzales a dolares
##        3.Salir
##        '''
##print(menu)
##opcion = input(":.")
##while opcion != 3:
##    if opcion == 1:
##        quetzal = float(input("Valor a convertir"))
##        TASA = 7.5
##        dolares = quetzal // 7.5
##        print("La cantidad es{dolares}".format(dolares))
##    elif opcion == 2:
##        dolares = float(input("Valor a convertir"))
##        quetzal = dolares * 7.5
##        print("La cantidad es{quetzal}".format(quetzal))
##    else:
##        print("Opcion no valida")
##        print(menu)
##    opcion = input(":.")

##Solicitar al usuario que escoga una de las siguientes opciones
##Sumar dos numeros, restar tres numeros, multiplicar cuatro numeros, dividir dos numeros.
##si el usuario elegi una opcion invalida hacerselo saber

menu = '''Menu
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir
        '''
print (menu)
opcion = input(":.")
while opcion != 5:
    if menu == 1:
        num1 = input("Valor numero1")
        num2 = input("Valor numero2")
        suma = num1 + num2
        print("La suma es {}".format(suma))
    elif opcion == 2:
        num1 = input("Valor numero1")
        num2 = input("Valor numero2")
        num3 = input("Valor numero3")
        resta = num1 - num2 - num3
        print("La resta es {}".format(resta))
    elif opcion == 3:
        num1 = input("Valor numero1")
        num2 = input("Valor numero2")
        num3 = input("Valor numero3")
        num4 = input("Valor numero4")
        multiplicacion = num1 * num2 * num3 * num4
        print("La multiplicacion es {}".format(multiplicacion))
    elif opcion == 4:
        num1 = input("Valor numero1")
        num2 = input("Valor numero2")
        division = num1 // num2
        print("La division es {}".format(division))
    else:
        print("Opcion no valida")
    print (menu)
    opcion = input(":.")
print ("FIN")
        
        
        
