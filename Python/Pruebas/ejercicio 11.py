temperatura = int(input("Indique su temperatura actual, solo escribe el numero "))
if temperatura < 10 :
    print("El clima esta frio")
elif 10 <= temperatura <25:
    print("El clima esta templado")
elif 25 <= temperatura <35:
    print("El clima esta caluroso")
else:
    print("El clima esta muy caluroso")