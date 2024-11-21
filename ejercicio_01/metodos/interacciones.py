from tabulate import tabulate
from datetime import datetime, date

def actualizar_revision(dinosaurios):
    if not dinosaurios:
        print("No hay dinosaurios ingresados.")
        return
    
    print("\n--- Lista de Dinosaurios ---")
    for i, dinosaurio in enumerate(dinosaurios):
        print(f"{i + 1}. {dinosaurio.nombre} - {dinosaurio.especie} - Última Revisión: {dinosaurio.ultima_revision}")

    
    while True:
        try:
            seleccion = int(input("\nSeleccione el dinosario a actualizar "))
            if 1 <= seleccion <= len(dinosaurios):
                dinosaurio_seleccionado = dinosaurios[seleccion - 1]
                break
            else:
                print("Seleccion invalida. Intente nuevamente.")
        except ValueError:
            print("Caracter Invalido.")

    #nueva fecha de revision
    while True:
        ultima_revision_str = input("Ingrese la nueva fecha de última revisión (YYYY-MM-DD): ").strip()
        try:
            nueva_revision = datetime.strptime(ultima_revision_str, "%Y-%m-%d").date()
            dinosaurio_seleccionado.ultima_revision = nueva_revision
            print(f"\nLa fecha de revision del dinosaurio '{dinosaurio_seleccionado.nombre}' ha sido actualizada.")
            break
        except ValueError:
            print("Formato Invalido")





#Muestra las revisiones atrasadas
def revisiones_atrasadas(dinosaurios):
    if not dinosaurios:
        print("No hay dinosaurios ingresados.")
        return
    
    hoy = date.today()
    atrasados = []

    for dinosaurio in dinosaurios:
        dias_revision = (hoy - dinosaurio.ultima_revision).days
        if dinosaurio.nivel_agresividad >= 8 and dias_revision > 7:
            prioridad = 1
        elif dinosaurio.nivel_agresividad <= 7 and dias_revision > 15:
            prioridad = 2
        else:
            continue 
        
        atrasados.append([
            dinosaurio.nombre, 
            dinosaurio.especie, 
            dinosaurio.nivel_agresividad, 
            dinosaurio.ultima_revision, 
            dias_revision, 
            prioridad
        ])

    if not atrasados:
        print("No hay revisiones atrasadas.")
    else:
        headers = ["Nombre", "Especie", "Nivel de Agresividad", "Última Revisión", "Días Atrasados", "Prioridad"]
        print("\nDinosaurios con revisiones atrasadas:")
        print(tabulate(atrasados, headers=headers, tablefmt="grid"))
        input(f"Presiona una tecla para continuar.")



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
        input(f"Presiona una tecla para continuar.")

