print("--------------Bienvenido al sistema de facturación -----------")
nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")
valor = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
total = valor * cantidad

if total > 500000:
    descuento = total * 0.15
    total_con_descuento = total - descuento
    print(f"Hola {nombre}, lista de su producto {producto} \n El total de su compra es: {total_con_descuento} \n (descuento aplicado: {descuento})")
elif total >= 200000 and total <= 500000:
    descuento = total * 0.10
    total_con_descuento = total - descuento
    print(f"Hola {nombre}, lista de su producto {producto} \n El total de su compra es: {total_con_descuento} \n (descuento aplicado: {descuento})")
else:
    print(f"Hola {nombre}, lista de su producto {producto} \n El total de su compra es: {total} \n (no se aplicó descuento)")