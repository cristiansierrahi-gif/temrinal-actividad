usuario = "Boot"
contraseña = "1234"

soli_n = input( "Usuario: ")
soli_c = input("Contraseña: ")
correcto = usuario and contraseña
if (soli_n and soli_c) == correcto:
    print (f"Bienvenido {usuario}")
else:
    print("Usuario o ontraseña incorrecta, intentelo de nuevo")