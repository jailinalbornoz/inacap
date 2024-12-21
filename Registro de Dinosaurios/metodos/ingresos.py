from clases import carnivoroclass, herbivoroclass, omnivoroclass
from datetime import datetime


#Ingreso de Carnivoro
def ingresar_carnivoro(dinosaurios):
    nombre = input("Nombre del Dinosaurio: ")
    especie = "Carnivoro"
    
    while True:
        try:
            nivel_agresividad = int(input("Nivel de Agresividad (1-10): "))
            if 1 <= nivel_agresividad <= 10:
                break
            else:
                print("El nivel de agresividad debe estar entre 1 y 10.")
        except ValueError:
            print("Caracter Invalido.")

    while True:
        try:
            nivel_caza = int(input("Nivel de Caza (1-100): "))
            if 1 <= nivel_caza <= 100:
                break
            else:
                print("El nivel de caza debe estar entre 1 y 100.")
        except ValueError:
            print("Caracter Invalido.")

#Captura el valor ingresado por el usuario como texto
#Convierte el texto en un objeto datetime utilizando el formato
    while True:
        ultima_revision_str = input("Fecha de ultima revision (YYYY-MM-DD): ").strip()
        try:
            ultima_revision = datetime.strptime(ultima_revision_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Fecha invalida. Intente nuevamente.")

    carnivoro = carnivoroclass(nombre, especie, nivel_agresividad, nivel_caza, ultima_revision)
    #carnivoro = carnivoroclass("dino","carnivoro",10,50,"2024-10-11")
    dinosaurios.append(carnivoro)
    print("\nDinosaurio ingresado exitosamente.")
    input("\nPresione Enter para continuar...")


#Ingreso de Herbivoro
def ingresar_herbivoro(dinosaurios):
    nombre = input("Nombre del Dinosaurio: ")
    especie = "Herbivoro"
    while True:
        try:
            nivel_agresividad = int(input("Nivel de Agresividad (1-10): "))
            if 1 <= nivel_agresividad <= 10:
                break
            else:
                print("El nivel de agresividad debe estar entre 1 y 10.")
        except ValueError:
            print("Caracter Invalido.")
    preferencia_vegetal = input("Preferencia Vegetal: ")
    while True:
            ultima_revision_str = input("Fecha de ultima revision (YYYY-MM-DD): ").strip()
            try:
                ultima_revision = datetime.strptime(ultima_revision_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Fecha invalida. Intente nuevamente.")
    herbivoro = herbivoroclass(nombre, especie, nivel_agresividad, preferencia_vegetal, ultima_revision)
    #herbivoro = herbivoroclass("hoja","herbivoro",1,"lechuga","2024-10-11")
    dinosaurios.append(herbivoro)
    print("\nDinosaurio ingresado exitosamente.")
    input("\nPresione Enter para continuar...")



#Ingreso de Omnivoro
def ingresar_omnivoro(dinosaurios):
    nombre = input("Nombre del Dinosaurio: ")
    especie = "Omnivoro"
    while True:
        try:
            nivel_agresividad = int(input("Nivel de Agresividad (1-10): "))
            if 1 <= nivel_agresividad <= 10:
                break
            else:
                print("El nivel de agresividad debe estar entre 1 y 10.")
        except ValueError:
            print("Caracter Invalido.")

    while True:
        try:
            versatilidad = int(input("Nivel de Versatilidad Alimenticia (1-100): "))
            if 1 <= versatilidad <= 100:
                break
            else:
                print("El nivel de versatilidad debe estar entre 1 y 100.")
        except ValueError:
            print("Caracter Invalido.")
    while True:
            ultima_revision_str = input("Fecha de ultima revision (YYYY-MM-DD): ").strip()
            try:
                ultima_revision = datetime.strptime(ultima_revision_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Fecha invalida. Intente nuevamente.")
    omnivoro = omnivoroclass(nombre, especie, nivel_agresividad, versatilidad, ultima_revision)
    #omnivoro = omnivoroclass("pingu","omnivoro",5,50,"2024-10-11")
    dinosaurios.append(omnivoro)
    print("Dinosaurio ingresado exitosamente.")
    input(f"Presiona una tecla para continuar.")


