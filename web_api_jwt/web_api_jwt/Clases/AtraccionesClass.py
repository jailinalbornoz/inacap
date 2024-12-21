class AtraccionesClass:
    def __init__(self, atraccion_id, nombre, descripcion):
        self.atraccion_id = atraccion_id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.atraccion_id}, Nombre: {self.nombre}, Descripción: {self.descripcion}"
