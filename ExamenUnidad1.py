import os
print(os.name)

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL DE PROGRAMAS DE PYTHON  ---")
    print("1. Ejecutar CiudadesTemperaturas.py")
    print("2. Ejecutar Ejer.15Mejorado2.py")
    print("3. Ejecutar Ejer1.6.py")
    print("4. Ejecutar Ejer1.7.py")
    print("5. Ejecutar Ejer1.8.py")
    print("6. Ejecutar Ejer1.py")
    print("7. Ejecutar Ejer2.py")
    print("8. Ejecutar Ejer3.py")
    print("9. Ejecutar Ejer4.py")
    print("10. Ejecutar Ejer5.py")
    print("11. Ejecutar Ejer8.py")
    print("12. Ejecutar Ejer10.py")
    print("13. Ejecutar Ejer11.py")
    print("14. Ejecutar Ejer12.py")
    print("15. Ejecutar Ejer14.py")
    print("16. Ejecutar Ejer15Mejorado.py")
    print("17. Ejecutar Ejer16.py")
    print("18. Ejecutar EjercicioNodo.py")
    print("19. Ejecutar Ejercicios.py")
    print("20. Salir")

def ejecutar_script(nombre_script):
    os.system(f"python {nombre_script}")  # Ejecuta el script en la terminal

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion.isdigit():
        opcion = int(opcion)

        if 1 <= opcion <= 19:
            scripts = [
                "CiudadesTemperaturas.py",
                "Ejer.15Mejorado2.py",
                "Ejer1.6.py",
                "Ejer1.7.py",
                "Ejer1.8.py",
                "Ejer1.py",
                "Ejer2.py",
                "Ejer3.py",
                "Ejer4.py",
                "Ejer5.py",
                "Ejer8.py",
                "Ejer10.py",
                "Ejer11.py",
                "Ejer12.py",
                "Ejer14.py",
                "Ejer15Mejorado.py",
                "Ejer16.py",
                "EjercicioNodo.py",
                "Ejercicios.py"
            ]
            ejecutar_script(scripts[opcion - 1])

        elif opcion == 20:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
    else:
        print("Por favor, ingrese un número válido.")