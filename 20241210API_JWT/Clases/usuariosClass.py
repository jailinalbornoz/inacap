from Clases.controlClass import ControlClass
class usuariosClass(ControlClass):
    def __init__(self, rut, nombre, apellido, estado, password_hash, password_plain, 
                usuario_creacion, fecha_creacion, ip, 
                usuario_modificacion, fecha_modificacion,                 
                 id=None, existe=False):
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion)
        self.id = id  # ID del personaje (opcional, por defecto None)
        self.rut = rut  # RUT del personaje
        self.nombre = nombre  # Nombre del personaje
        self.apellido = apellido  # Apellido del personaje
        self.estado = estado  # Apellido del personaje
        self.password_hash = password_hash  # Contraseña cifrada
        self.password_plain = password_plain  # Contraseña en texto plano (NO RECOMENDADO)
        self.existe = existe  # Indica si el personaje ya existe en la base de datos
    
    def __str__(self):
        return (
            f"ID: {self.id}, RUT: {self.rut}, Nombre: {self.nombre} {self.apellido}, Estado: {self.estado}"
            f"Existe: {'Sí' if self.existe else 'No'}, Password (hash): {self.password_hash}"
        )
    