num_1 = int(input("Escriba un número "))
num_2 = int(input("EScriba un número "))

print ("Se hara una una demostración de operaciones")

print(f"Suma {num_2+num_1}")
print(f"Resta {num_2-num_1}")
print(f"Multiplicación {num_2*num_1}")
if (num_1 and num_2) ==0:
    print("Esta división no se puede resolver")
else:
    print(f"División {num_1/num_2}")