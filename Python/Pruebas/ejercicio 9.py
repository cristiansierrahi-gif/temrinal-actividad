print ("BIenvenido a la caja registradora. POr favor ingrese el valor de su compra")

compra = int(input("No agregue puntos: "))
if compra >= 200000:
    print(f"Su compra recibe un descuento del 20%")
    print(f"Valor a pagar {compra-(compra*0.20)}")
elif compra >100000<200000:
    print(f"Su compra recibe un descuento del 10%")
    print(f"Valor a pagar: {compra-(compra*0.10)}")
else:
    print("Su compra no tiene descuento")
