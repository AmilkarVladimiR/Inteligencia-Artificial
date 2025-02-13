import datetime
import random


tienda = "Carpinteria Reyes"
folio = random.randint(1, 200 ) 
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

nombre_cliente = input("Ingrese tu nombre: ")
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
total_compra = cantidad * precio_unitario
descuento = total_compra * 0.10 if total_compra > 100 else 0
total_final = total_compra - descuento

print("\n" + "="*30)
print("       TICKET       ")
print("="*30)
print(f"Tienda: {tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print(f"Cliente: {nombre_cliente}")
print("-" * 30)
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Total de la compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
print("="*30)
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("="*30)
