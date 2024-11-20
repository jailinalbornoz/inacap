from .dinosaurioclass import dinosaurioclass

class omnivoroclass(dinosaurioclass):
    def __init__(self, nombre, especie, nivel_agresividad, versatilidad, ultima_revision):
        super().__init__(nombre, especie, nivel_agresividad, ultima_revision)
        self.versatilidad = versatilidad

def detalle_omnivoro(self):
        return (f"{dinosaurioclass.detalle()}\n"
                f"Nivel de caza: {omnivoroclass.versatilidad}")