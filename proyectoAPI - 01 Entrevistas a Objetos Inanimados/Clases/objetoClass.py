from Clases.controlClass import ControlClass
class objetoClass(ControlClass):
    def __init__(self, nombre_objeto, descripcion_objeto, 
                 usuario_creacion = None, fecha_creacion = None, ip = None, 
                 usuario_modificacion = None, fecha_modificacion = None, existe=False):
        # Llamada al constructor de la super clase
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion, existe=existe)
        
        # Propios atributos de la clase Objeto
        self.nombre_objeto = nombre_objeto
        self.descripcion_objeto = descripcion_objeto
    
    def __str__(self):
        return (
            f"Nombre Objeto: {self.nombre_objeto}, "
            f"Descripción Objeto: {self.descripcion_objeto}, "
        )
