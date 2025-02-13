nota = int(input ("Ingresa tu calificación (0-100): "))

if 90 <= nota <= 100:
 print ("Tu calificacion es: 'A'")
elif 80 <= nota < 90:
 print ("Tu calificacion es: B")
elif 70 <= nota < 80:
 print ("TU calificacion es: C")
elif 60 <= nota < 70:
 print("Tu calificacion es: D")
else:
 print("Tu calificacion es: F")