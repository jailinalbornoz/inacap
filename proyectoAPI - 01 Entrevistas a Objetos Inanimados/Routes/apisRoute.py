import httpx
from fastapi import APIRouter, HTTPException, Security
from Config.jwtConfig import jwtConfig
import logging

# Configurar el logger
logger = logging.getLogger(__name__)

# Crear el router para apis
apis_router = APIRouter(prefix="/apis", tags=["Apis"])

# Endpoint que consume la API de universidades
@apis_router.get(
    "/getApiDummy",
    summary="Crear un recurso dummy",
    description="Este endpoint permite crear un recurso dummy en el sistema. Es útil para pruebas y validación del funcionamiento de la API.",
    responses={
        201: {"description": "Recurso dummy creado exitosamente."},
        400: {"description": "Los datos proporcionados son inválidos."},
        401: {"description": "El usuario no está autenticado o no tiene permisos para realizar esta acción."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def get_dummy(current_user: str = Security(jwtConfig.validate_token)):
    try:
        logger.info(f"Usuario {current_user} está intentando obtener datos de el endpoint Dummy.")
        pass    
    except httpx.RequestError as e:
        logger.error(f"Error de conexión con la API externa: {e}")
        raise HTTPException(status_code=500, detail="Error al conectar con el servidor externo")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")
    


# Endpoint que consume la URL externa para obtener un usuario aleatorio
@apis_router.get(
    "/getRandomUser",
    summary="Obtener usuario aleatorio",
    description="Este endpoint consume la API externa de Random User Generator.",
    responses={
        200: {"description": "Solicitud exitosa, devuelve un usuario aleatorio."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def get_random_user():
    """
    Consume la API externa de Random User Generator para obtener un perfil de usuario aleatorio.
    """
    url = "https://randomuser.me/api/"
    
    try:
        # Realizar la solicitud GET a la API externa
        logger.info(f"Realizando solicitud a la API externa: {url}")
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        
        # Verificar si la respuesta es exitosa
        if response.status_code != 200:
            logger.error(f"Error al obtener los datos de la API externa: {response.status_code} - {response.text}")
            raise HTTPException(status_code=response.status_code, detail="Error al obtener los datos del servidor externo")

        # Obtener los datos de la respuesta JSON
        response_data = response.json()
        user_data = response_data.get('results', [])[0]
        
        # Formatear los datos del usuario
        formatted_user = {
            "name": f"{user_data['name']['first']} {user_data['name']['last']}",
            "email": user_data['email'],
            "gender": user_data['gender'],
            "location": f"{user_data['location']['street']['name']} {user_data['location']['number']}, {user_data['location']['city']}, {user_data['location']['state']}",
            "dob": user_data['dob']['date'],
            "phone": user_data['phone'],
            "picture": user_data['picture']['large']
        }

        # Devolver los datos del usuario generado
        return {
            "success": True,
            "message": "Usuario aleatorio obtenido con éxito",
            "data": formatted_user
        }
    
    except httpx.RequestError as e:
        logger.error(f"Error de conexión con la API externa: {e}")
        raise HTTPException(status_code=500, detail="Error al conectar con el servidor externo")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")