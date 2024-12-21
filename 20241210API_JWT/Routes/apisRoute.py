from fastapi import APIRouter
from logging import getLogger
logger = getLogger("RequestLogger") 

# Crear el router para apis
apis_router = APIRouter(prefix="/apis", tags=["Apis"])
urls =[
    "http://universities.hipolabs.com/search?country=Chile",
    "https://v2.jokeapi.dev/joke/Any?lang=es",
    "https://pokeapi.co/api/v2/pokemon/jigglypuff"
]

@apis_router.get("/")
async def metodoDummy():
    pass