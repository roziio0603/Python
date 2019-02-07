QUETZAL_DOLAR = 7.69
DOLAR_QUETZAL = 0.13
cantidad = 0
total = 0
print("Bienvenido al conversor".center(50,"*"))
opcion = input("1-quetzales a dolares:. 2- dolares a quetzales:.")


if opcion == "1":
    quetzales = input("cantidad de quetzales")
    saldo = float(quetzales) / QUETZAL_DOLAR
    print("La conversion es {}".format(saldo))
elif opcion == "2":
    dolares = input("cantidad de dolares")
    saldo = float(dolares) * QUETZAL_DOLAR
    print("La conversion es {}".format(saldo))
else:
    print("Opcion no valida")
