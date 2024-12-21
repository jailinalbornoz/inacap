from Clases.controlClass import ControlClass

class entrevistaClass(ControlClass):
    def __init__(self, tema, duracion_minutos, 
                 usuario_creacion=None, fecha_creacion=None, ip=None, 
                 usuario_modificacion=None, fecha_modificacion=None, existe=False):
        # Llamada al constructor de la super clase
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion, existe=existe)
        
        # Propios atributos de la clase Entrevista
        self.tema = tema
        self.duracion_minutos = duracion_minutos
    
    def __str__(self):
        return (
            f"Tema: {self.tema}, "
            f"Duración en minutos: {self.duracion_minutos}"
        )
