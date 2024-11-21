from metodos.ingresos import ingresar_carnivoro, ingresar_herbivoro, ingresar_omnivoro
from metodos.interacciones import actualizar_revision, revisiones_atrasadas, mostrar_dinosaurios

# Menú principal del sistema
def mostrar_menu():
    print("\n--- Sistema de Parque Jurásico - Gestión de Dinosaurios ---")
    print("1. Ingresar un Carnivoro")
    print("2. Ingresar un Herbivoro")
    print("3. Ingresar un Omnivoro")
    print("4. Actualizar la fecha de revisión médica")
    print("5. Mostrar todos los dinosaurios")
    print("6. Revisiones Atrasadas")
    print("7. Salir")

# Función principal del programa
def main():
    
# Lista global de dinosaurios compartida por todas las funciones
    dinosaurios = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_carnivoro(dinosaurios)
        elif opcion == "2":
            ingresar_herbivoro(dinosaurios)
        elif opcion == "3":
            ingresar_omnivoro(dinosaurios)
        elif opcion == "4":
            actualizar_revision(dinosaurios)
        elif opcion == "5":
            mostrar_dinosaurios(dinosaurios)
        elif opcion == "6":
            revisiones_atrasadas(dinosaurios)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


            