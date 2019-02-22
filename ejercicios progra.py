##Rocio
##Ejercicios

##1.Realice un programa que determine el pago a realizar por la entrada a un
##espectaculo donde se pueden comprar solo hasta cuatro entradas, donde al costo
##de dos entradas se les descuenta el 10%, al de tres entradas el 15% y a la
##compra de cuatro tickets se le descuenta el 20%
##BOLETOS = 200
##print("El valor de los boletos de es Q200.00")
##num1 = input("1- Dos entradas el descuento es de 10% 2- Tres entradas el descuento es de 15% 3- Cuatro entradas el descuento es de 20%")
##if num1 == "1":
##    ticket = BOLETOS * 2
##    descuento = ticket * 0.10
##    resta = ticket - descuento
##    print("El pago a realizar es de {}".format(resta))
##elif num1 == "2":
##    ticket = BOLETOS * 3
##    descuento = ticket * 0.15
##    resta = ticket - descuento
##    print("El pago a realizar es de {}".format(resta))
##elif num1 == "3":
##    ticket = BOLETOS * 4
##    descuento = ticket * 0.20
##    resta = ticket - descuento
##    print("El pago a realizar es de {}".format(resta))
##else:
##    print("No puede comprar esta cantidad de entradas")
    

##2.Programa que pida en pantalla datos del empleado: nombre, puesto, direccion,
##telefono, años de antiguedad en la empresa. Determine el sueldo nuevo del
##empleado calculado por los años de antiguedad del empleado.
##    1. Nivel de antiguedad 3 años aumento 5%
##    2. Nivel de antiguedad 5 años aumento 15%
print ("Bienvenidos al programa")
aumento = 0
nombre = input("Ingrese su nombre:.")
puesto = input("Ingrese su puesto:.")
direc = input("Ingrese su direccion:.")
tel = int(input("Ingrese su numero de telefono:."))
anios = int(input("Ingrese sus anios de antiguedad:."))
sueldo = int(input("Ingrese su sueldo:."))
if anios <= 3:
    aumento = int(sueldo) * 0.05
    aumento = aumento + sueldo
    print("Su nuevo sueldo es de{} ".format(aumento))
elif anios >=5:
    aumento = int(sueldo)* 0.15
    aumento = aumento + sueldo
    print("Su nuevo sueldo es de{}".format(aumento))
else:
    print("Fin de ejecucion")
    

##3.Construya programa en python con funciones correspondientes
##    1.Promedio de alumno(ingrese las 4 notas y determine promedio)
##    2.Division (Si el segundo valor es 0 debe mostrar error valor incorrecto
##                y volver a ejecutar el programa)
##print("Bienvenidos")
##promedio = 0
##num2 = 0
##print("Ingrese cuatro notas")
##while num2 == 0:
##    num1 = int(input("Ingrese primera nota"))
##    num2 = int(input("Ingrese segunda nota"))
##    num3 = int(input("Ingrese tercera nota"))
##    num4 = int(input("Ingrese cuarta nota"))
##    promedio = (num1 + num2 + num3 + num4)/4
##    if num2 != 0:
##        print("El promedio es de{}".format(promedio))
##        print("Gracias")
##    elif num2 == 0:
##        print("Valor invalido")

