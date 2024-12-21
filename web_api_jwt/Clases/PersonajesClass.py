class PersonajesClass:
    def __init__(self, nombre, especialidad, nivel_locura, personaje_id=None):
        self.personaje_id = personaje_id
        self.nombre = nombre
        self.especialidad = especialidad
        self.nivel_locura = nivel_locura

    def __str__(self):
        return f"ID: {self.personaje_id}, Nombre: {self.nombre}, Especialidad: {self.especialidad}, Nivel Locura: {self.nivel_locura}"
