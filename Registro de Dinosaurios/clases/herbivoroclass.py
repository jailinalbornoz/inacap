from .dinosaurioclass import dinosaurioclass

class herbivoroclass(dinosaurioclass):
    def __init__(self, nombre, especie, nivel_agresividad, preferencia_vegetal, ultima_revision):
        super().__init__(nombre, especie, nivel_agresividad, ultima_revision)
        self.preferencia_vegetal = preferencia_vegetal

def detalle_herbivoro(self):
        return (f"{dinosaurioclass.detalle()}\n"
                f"Nivel de caza: {herbivoroclass.preferencia_vegetal}")