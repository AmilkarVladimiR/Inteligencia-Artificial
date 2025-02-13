
nombre = input("Ingrese tu nombre: ")
producto = input("Ingrese el nombre del producto: ")
total_compra = float(input("Ingrese el total de su compra: "))

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Felicidades {nombre}! Has comprado {producto} y tienes un descuento del 10%. El total a pagar es: {total_final}")
else:
    print(f"{nombre}, has comprado {producto}. El total a pagar es: {total_compra}")
