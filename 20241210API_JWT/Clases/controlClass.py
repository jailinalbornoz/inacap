class ControlClass:
    def __init__(self, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion):
        self.usuario_creacion = usuario_creacion
        self.fecha_creacion = fecha_creacion
        self.ip = ip
        self.usuario_modificacion = usuario_modificacion
        self.fecha_modificacion = fecha_modificacion

    def __str__(self):
        return (
            f"Usuario Creación: {self.usuario_creacion}, Fecha Creación: {self.fecha_creacion}, "
            f"IP: {self.ip}, Usuario Modificación: {self.usuario_modificacion}, "
            f"Fecha Modificación: {self.fecha_modificacion}"
        )
