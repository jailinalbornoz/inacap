from Clases.controlClass import ControlClass
class actoresClass(ControlClass):
    def __init__(self, nombre, fecha_nacimiento,
                 usuario_creacion, fecha_creacion, ip, 
                 usuario_modificacion, fecha_modificacion, 
                 id=None, existe=False):
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion)
        self.id = id  # ID del actor (opcional, por defecto None)
        self.nombre = nombre  # Nombre completo del actor
        self.fecha_nacimiento = fecha_nacimiento  # Fecha de nacimiento del actor
        self.existe = existe  # Indica si el actor ya existe en la base de datos

    def __str__(self):
        return (
            f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Nacimiento: {self.fecha_nacimiento}, "
            f"Existe: {'Sí' if self.existe else 'No'}, "
            f"{super().__str__()}"
        )
