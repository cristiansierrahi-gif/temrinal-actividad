saldo = 500000

print   ("-----------Bienvenido a su banco -----------")
print  ("1. Consultar saldo")
print  ("2. Retirar dinero")
print  ("3. Depositar dinero")
print  ("4. Salir")

opcion = int(input("Ingrese una opción: "))
if opcion == 1:
    print("Su saldo actual es: ", saldo)
elif opcion == 2:
    monto = int(input("Ingrese el monto a retirar: "))
    if monto <= saldo:
        saldo -= monto
        print("Retiro exitoso. Su saldo actual es: ", saldo)
    else:
        print("Fondos insuficientes.")
elif opcion == 3:
    monto = int(input("Ingrese el monto a depositar: "))
    saldo += monto
    print("Depósito exitoso. Su saldo actual es: ", saldo)
elif opcion == 4:
    print("Gracias por usar nuestro servicio.")
else:
    print("Opción no válida.")