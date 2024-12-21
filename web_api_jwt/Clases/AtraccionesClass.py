class AtraccionesClass:
    def __init__(self, nombre, descripcion, atraccion_id=None, existe=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.atraccion_id = atraccion_id
        self.existe = existe

    def __str__(self):
        return f"ID: {self.atraccion_id}, Nombre: {self.nombre}, Descripción: {self.descripcion}"
