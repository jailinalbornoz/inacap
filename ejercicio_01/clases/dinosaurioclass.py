class dinosaurioclass:
    def __init__(self, nombre, especie, nivel_agresividad, ultima_revision):
        self.nombre = nombre
        self.especie = especie
        self.nivel_agresividad = nivel_agresividad
        self.ultima_revision = ultima_revision

#Fecha de la ultima revision
    def revisar(self, fecha):
        self.ultima_revision = fecha

#Mostrar la informacion del dinosaurio
    def detalle(self):
        return (f"Dinosaurio: {self.nombre}\n"
                f"Especie: {self.especie}\n"
                f"Nivel de agresividad: {self.nivel_agresividad}\n"
                f"Ultima revision medica: {self.ultima_revision}")
    