print("Calculadora en python")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero numero: "))

print("Operaciones disponibles: + (Suma), - (Resta), * (Multiplicación), / (División)")
operacion = input("¿Qué operación deseas realizar? Indica el simbolo: ")

if operacion == "+":
    resultado = num1+num2
    print(f"\n Resultado: {num1} + {num2} = {resultado}")
elif operacion == "+":
    resultado = num1-num2
    print(f"\n Resultado: {num1} - {num2} = {resultado}")
elif operacion == "+":
    resultado = num1*num2
    print(f"\n Resultado: {num1} * {num2} = {resultado}")
elif operacion == "+":
    resultado = num1/num2
    if num2 !=0:
        print(f"\n Resultado: {num1} + {num2} = {resultado}")
    else:
        print(f"\n Error: No se puede dividir entre cero")
else:
    print("Error: operacion no valida, introduzca una operacion")