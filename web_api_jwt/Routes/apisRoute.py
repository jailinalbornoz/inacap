import httpx
from fastapi import APIRouter, HTTPException, Security
from Metodos.jwtMetodos import jwtMetodos
import logging

# Configurar el logger
logger = logging.getLogger(__name__)

# Crear el router para apis
apis_router = APIRouter(prefix="/apis", tags=["Apis"])

# Endpoint que consume la URL externa para obtener farmacias de turno
@apis_router.get(
    "/getLocalesTurnos",
    summary="Obtener farmacias de turno del MINSAL",
    description="Este endpoint consume la API externa del MINSAL para obtener la información de las farmacias que están de turno, en base a los parámetros proporcionados.",
    responses={
        200: {"description": "Solicitud exitosa, devuelve los turnos de las farmacias."},
        401: {"description": "Token inválido o no proporcionado."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def get_local_turnos(current_user: str = Security(jwtMetodos.validate_token)):
    """
    Consume la API externa del MINSAL para obtener los datos de las farmacias de turno.
    """
    logger.info(f"Usuario {current_user} está intentando obtener las farmacias de turno.")

    url = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
    
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
        filtered_data = [item for item in response_data if item.get('fk_region') == "7" and item.get('fk_comuna') == '102']

        # Devolver los datos obtenidos de la API externa (farmacias de turno)
        return {"success": True, "message": "Datos de farmacias de turno obtenidos con éxito", "data": filtered_data}
    
    except httpx.RequestError as e:
        logger.error(f"Error de conexión con la API externa: {e}")
        raise HTTPException(status_code=500, detail="Error al conectar con el servidor externo")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")

# Endpoint que consume la URL externa para obtener los indicadores económicos
@apis_router.get(
    "/getIndicadoresEconomicos",
    summary="Consultar indicadores económicos",
    description="Este endpoint consulta los indicadores económicos de la API de Mindicador.",
    responses={
        200: {"description": "Solicitud exitosa, devuelve los indicadores económicos."},
        401: {"description": "Token inválido o no proporcionado."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def get_indicadores_economicos(current_user: str = Security(jwtMetodos.validate_token)):
    """
    Consume la API de Mindicador para obtener los indicadores económicos.
    """
    logger.info(f"Usuario {current_user} está intentando obtener los indicadores económicos.")

    url = "https://mindicador.cl/api"
    
    try:
        # Realizar la solicitud GET a la API externa
        logger.info(f"Realizando solicitud a la API externa: {url}")
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        
        # Verificar si la respuesta es exitosa
        if response.status_code != 200:
            logger.error(f"Error al obtener los indicadores económicos de la API externa: {response.status_code} - {response.text}")
            raise HTTPException(status_code=response.status_code, detail="Error al obtener los indicadores económicos del servidor externo")

        # Obtener los datos de la respuesta JSON
        response_data = response.json()
        logger.info(f"Datos recibidos de la API externa: {response_data}")
        
        # Devolver los datos obtenidos de la API externa (indicadores económicos)
        return {"success": True, "message": "Indicadores económicos obtenidos con éxito", "data": response_data}
    
    except httpx.RequestError as e:
        logger.error(f"Error de conexión con la API externa: {e}")
        raise HTTPException(status_code=500, detail="Error al conectar con el servidor externo")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")

# Endpoint que consume la URL externa para obtener los datos de la IP
@apis_router.get(
    "/getIpData",
    summary="Obtener datos de la IP del usuario",
    description="Este endpoint consulta la API externa para obtener información sobre la IP del usuario.",
    responses={
        200: {"description": "Solicitud exitosa, devuelve los datos de la IP."},
        401: {"description": "Token inválido o no proporcionado."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def get_ip_data(current_user: str = Security(jwtMetodos.validate_token)):
    """
    Consume la API de ipapi.co para obtener los datos relacionados con la IP del usuario.
    """
    logger.info(f"Usuario {current_user} está intentando obtener los datos de su IP.")

    url = "https://ipapi.co/json"
    
    try:
        # Realizar la solicitud GET a la API externa
        logger.info(f"Realizando solicitud a la API externa: {url}")
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        
        # Verificar si la respuesta es exitosa
        if response.status_code != 200:
            logger.error(f"Error al obtener los datos de la IP de la API externa: {response.status_code} - {response.text}")
            raise HTTPException(status_code=response.status_code, detail="Error al obtener los datos de la IP del servidor externo")

        # Obtener los datos de la respuesta JSON
        response_data = response.json()
        logger.info(f"Datos recibidos de la API externa: {response_data}")
        
        # Devolver los datos obtenidos de la API externa (datos de la IP)
        return {"success": True, "message": "Datos de IP obtenidos con éxito", "data": response_data}
    
    except httpx.RequestError as e:
        logger.error(f"Error de conexión con la API externa: {e}")
        raise HTTPException(status_code=500, detail="Error al conectar con el servidor externo")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")