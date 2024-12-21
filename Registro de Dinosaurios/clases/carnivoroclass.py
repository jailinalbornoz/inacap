from .dinosaurioclass import dinosaurioclass

class carnivoroclass(dinosaurioclass):
    def __init__(self, nombre, especie, nivel_agresividad, nivel_caza, ultima_revision):
        super().__init__(nombre, especie, nivel_agresividad, ultima_revision)
        self.nivel_caza = nivel_caza

def detalle_carnivoro(self):
        return (f"{dinosaurioclass.detalle()}\n"
                f"Nivel de caza: {carnivoroclass.nivel_caza}")

