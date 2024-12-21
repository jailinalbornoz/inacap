from fastapi import APIRouter
from logging import getLogger
logger = getLogger("RequestLogger") 

# Crear el router para login
login_router = APIRouter(prefix="/login", tags=["Login"])

@login_router.get("/")
async def metodoDummy():
    pass