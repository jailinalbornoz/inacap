from Clases.controlClass import ControlClass
class peliculasActoresClass(ControlClass):  
    def __init__(self, id_pelicula, id_actor, sueldo, fecha_inicio_grabacion, fecha_fin_grabacion, escenas_participadas, 
                usuario_creacion, fecha_creacion, ip, 
                usuario_modificacion, fecha_modificacion, 
                 id=None, existe=False):
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion)
        self.id = id  # ID de la relación (opcional, por defecto None)
        self.id_pelicula = id_pelicula  # ID de la película
        self.id_actor = id_actor  # ID del actor
        self.sueldo = sueldo  # Sueldo recibido por el actor
        self.fecha_inicio_grabacion = fecha_inicio_grabacion  # Fecha de inicio de grabación
        self.fecha_fin_grabacion = fecha_fin_grabacion  # Fecha de fin de grabación
        self.escenas_participadas = escenas_participadas  # Número de escenas participadas
        self.existe = existe  # Indica si la relación ya existe en la base de datos
    
    def __str__(self):
        return (
            f"ID: {self.id}, ID Película: {self.id_pelicula}, ID Actor: {self.id_actor}, "
            f"Sueldo: {self.sueldo}, Fecha Inicio: {self.fecha_inicio_grabacion}, "
            f"Fecha Fin: {self.fecha_fin_grabacion}, Escenas Participadas: {self.escenas_participadas}, "
            f"Existe: {'Sí' if self.existe else 'No'}"
        )
