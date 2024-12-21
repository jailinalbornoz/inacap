from fastapi import APIRouter
from logging import getLogger  # Importa el logger configurado globalmente
logger = getLogger("RequestLogger")  # Usa el logger configurado en el middleware

# Crear el router para PeliculasActores
peliculasActores_router = APIRouter(prefix="/PeliculasActores", tags=["PeliculasActores"])

@peliculasActores_router.get("/")
async def metodoDummy():
    pass