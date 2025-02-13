import random
numero_aleatorio = random. randint(1, 10)
adivina = int(input("Adivina el número entre 1 y 10: "))

print (f"El número aleatorio es {numero_aleatorio}.")
if adivina == numero_aleatorio:
 print ("¡Correcto! Has adivinado el número.")
else:
 print (f"Incorrecto. El número era {numero_aleatorio}.")