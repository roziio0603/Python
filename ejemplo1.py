##Rocio
##Calcular la edad actual de una persona, previamente ingresando el año actual y el año de nacimiento

print("Bienvenido al programa".center(50,"*"))
FEC_ACT = 2019
fec_nac = int(input("ingresa tu anio de nacimiento"))

edad = FEC_ACT - fec_nac
print("Tu edad es {}".format(edad))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

