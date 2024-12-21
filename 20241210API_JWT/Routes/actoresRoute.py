from fastapi import APIRouter
from logging import getLogger  # Importa el logger configurado globalmente
logger = getLogger("RequestLogger")  # Usa el logger configurado en el middleware

# Crear el router para Actores
actores_router = APIRouter(prefix="/Actoreszaz", tags=["Actores"])

@actores_router.get("/")
async def metodoDummy():
    pass

@actores_router.get("/qwea")
async def metodoDummy22():
    pass