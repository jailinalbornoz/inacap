from tabulate import tabulate
from datetime import datetime, date

def actualizar_revision(dinosaurios):
    if not dinosaurios:
        print("No hay dinosaurios ingresados.")
        return

    # Mostrar una lista de animales con índices para seleccionar
    print("\n--- Lista de Animales ---")

    for i, dinosaurio in enumerate(dinosaurios):
        print(f"{i + 1}. {dinosaurio.nombre} - {dinosaurio.especie} - Ultima Revision: {dinosaurio.ultima_revision}")

    try:
        # Seleccionar el animal por índice
        seleccion = int(input("Seleccione el número del dinosaurio que desea verificar: "))
        seleccion =  seleccion - 1
        if seleccion < 0 or seleccion >= len(dinosaurios):
            print("Selección no válida.")
            return
        
        # Ingresar la cantidad de daño
        cantidad = int(input("Ingrese la cantidad de daño: "))
        
        # Aplicar el daño al animal seleccionado
        dinosaurio = dinosaurios[seleccion]
        dinosaurio.actualizar_revision(cantidad)


    except ValueError:
        print("Ingrese un número válido para la selección y el daño.")

#Muestra las revisiones atrasadas
def revisiones_atrasadas(dinosaurios):
    if not dinosaurios:
        print("No hay dinosaurios ingresados.")
        return
    
    hoy = date.today()
    # Filtrar dinosaurios con revisiones atrasadas (más de 30 días)
    atrasados = [
        [dinosaurio.nombre, dinosaurio.especie, dinosaurio.nivel_agresividad, dinosaurio.ultima_revision, (hoy - dinosaurio.ultima_revision).days]
        for dinosaurio in dinosaurios
        if (hoy - dinosaurio.ultima_revision).days > 30
    ]
    
    if not atrasados:
        print("No hay revisiones atrasadas.")
    else:
        headers = ["Nombre", "Especie", "Nivel de Agresividad", "Última Revisión", "Días Atrasados"]
        # Imprimir la tabla usando tabulate
        print("\nDinosaurios con revisiones atrasadas:")
        print(tabulate(atrasados, headers=headers, tablefmt="grid"))


#Muestra todos los dinosaurios registrados
def mostrar_dinosaurios(dinosaurios):
    if not dinosaurios:
        print("No hay dinosaurios ingresados.")
    else:
        # Crear la lista de datos para la tabla
        datos = [[dinosaurio.nombre, dinosaurio.especie, dinosaurio.nivel_agresividad, dinosaurio.ultima_revision] for dinosaurio in dinosaurios]
        headers = ["Nombre", "Especie", "Nivel de Agresividad", "Ultima Revision"]
        # Imprimir la tabla usando tabulate
        print(tabulate(datos, headers=headers, tablefmt="grid"))

