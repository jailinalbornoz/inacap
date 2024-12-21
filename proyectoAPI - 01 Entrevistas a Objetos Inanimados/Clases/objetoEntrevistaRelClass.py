from Clases.controlClass import ControlClass

class objetoEntrevistaRelClass(ControlClass):
    def __init__(self, id_objeto, id_entrevista, 
                 fecha_entrevista, usuario_creacion=None, fecha_creacion=None, 
                 ip=None, usuario_modificacion=None, fecha_modificacion=None, existe=False):
        # Llamada al constructor de la super clase
        super().__init__(usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion, existe=existe)
        
        # Propios atributos de la clase ObjetoEntrevistaRel
        self.id_objeto = id_objeto
        self.id_entrevista = id_entrevista
        self.fecha_entrevista = fecha_entrevista
    
    def __str__(self):
        return (
            f"ID Objeto: {self.id_objeto}, "
            f"ID Entrevista: {self.id_entrevista}, "
            f"Fecha Entrevista: {self.fecha_entrevista}"
        )
