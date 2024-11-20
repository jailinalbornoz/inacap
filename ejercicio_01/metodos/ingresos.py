from clases.carnivoroclass import carnivoroclass
from clases.herbivoroclass import herbivoroclass
from clases.omnivoroclass import omnivoroclass
from datetime import datetime, date

def ingresar_carnivoro(dinosaurios):
    nombre = input("Nombre del Dinosaurio: ")
    especie = "Carnivoro"
    nivel_agresividad = int(input("Nivel de Agresividad: "))
    nivel_caza = int(input("Nivel de Caza: "))
    while True:
            ultima_revision = input("Fecha de Última Revisión (DD-MM-YYYY): ").strip()
            try:
                # Validar y convertir la fecha
                fecha_valida = datetime.strptime(ultima_revision, "%d-%m-%Y")
                ultima_revision = fecha_valida.strftime("%d-%m-%Y")  # Formatear de nuevo por consistencia
                break
            except ValueError:
                print("Formato de fecha inválido. Asegúrese de usar el formato DD-MM-YYYY.")
    carnivoro = carnivoroclass(nombre, especie, nivel_agresividad, nivel_caza, ultima_revision)
    dinosaurios.append(carnivoro)
    print("Dinosaurio ingresado exitosamente.")

def ingresar_herbivoro(dinosaurios):
    nombre = input("Nombre del Dinosaurio: ")
    especie = "Herbivoro"
    nivel_agresividad = int(input("Nivel de Agresividad: "))
    preferencia_vegetal = input("Preferencia Vegetal: ")
    #ultima_revision = input("Ultima Revision: ")
    herbivoro = herbivoroclass(nombre, especie, nivel_agresividad, preferencia_vegetal)
    dinosaurios.append(herbivoro)
    print("Dinosaurio ingresado exitosamente.")

def ingresar_omnivoro(dinosaurios):
    nombre = input("Nombre del Dinosaurio: ")
    especie = "Omnivoro"
    nivel_agresividad = int(input("Nivel de Agresividad: "))
    versatilidad = input("Versatilidad: ")
    #ultima_revision = input("Ultima Revision: ")
    omnivoro = omnivoroclass(nombre, especie, nivel_agresividad, versatilidad)
    dinosaurios.append(omnivoro)
    print("Dinosaurio ingresado exitosamente.")


