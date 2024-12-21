from fastapi import APIRouter
from logging import getLogger  # Importa el logger configurado globalmente
logger = getLogger("RequestLogger")  # Usa el logger configurado en el middleware

# Crear el router para Peliculas
peliculas_router = APIRouter(prefix="/Peliculas", tags=["Peliculas"])

@peliculas_router.get("/")
async def metodoDummy():
    pass