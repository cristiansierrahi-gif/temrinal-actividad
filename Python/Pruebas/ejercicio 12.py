lado1 = int(input("Indique el valor del primer lado "))
lado2 = int(input("Indique el valor del segundo lado "))
lado3 = int(input("Indique le valor del tercer lado "))

if lado1 ==lado2 == lado3: 
    print("Es un triaungulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triaungulo isoseles")
else:
    print("Es un triángulo escaleno")
