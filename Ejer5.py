calificacion = int(input("Ingrese la calificación: "))

if 95 <= calificacion <= 100:
    print("La calificación es excelente")
elif 85 <= calificacion <= 94:
    print("La calificación es notable")
elif 75 <= calificacion <= 84:
    print("La calificación es aprobado")
elif 70 <= calificacion <= 74:
    print("La calificación es suficiente")
else:
    print("No aprobado")
