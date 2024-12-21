from Clases.controlClass import ControlClass
class peliculasClass(ControlClass): 
    def __init__(self, titulo, anio_estreno, duracion, 
                usuario_creacion, fecha_creacion, ip, 
                usuario_modificacion, fecha_modificacion,
                 id=None, existe=False):
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion)
        self.id = id  # ID de la película (opcional, por defecto None)
        self.titulo = titulo  # Título de la película
        self.anio_estreno = anio_estreno  # Año de estreno de la película
        self.duracion = duracion  # Duración de la película en minutos
        self.existe = existe  # Indica si la película ya existe en la base de datos
    
    def __str__(self):
        return (
            f"ID: {self.id}, Título: {self.titulo}, Año de Estreno: {self.anio_estreno}, "
            f"Duración: {self.duracion} minutos, Existe: {'Sí' if self.existe else 'No'}"
        )
