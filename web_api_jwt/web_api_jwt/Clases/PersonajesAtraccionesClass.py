class PersonajesAtraccionesClass:
    def __init__(self, id, personaje_id, atraccion_id):
        self.id = id
        self.personaje_id = personaje_id
        self.atraccion_id = atraccion_id

    def __str__(self):
        return f"ID: {self.id}, Personaje ID: {self.personaje_id}, Atracción ID: {self.atraccion_id}"
