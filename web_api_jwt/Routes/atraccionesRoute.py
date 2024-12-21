from typing import Optional
from fastapi import APIRouter, HTTPException, Security
from Metodos.jwtMetodos import jwtMetodos
from Clases.AtraccionesClass import AtraccionesClass
from Metodos.AtraccionesMetodos import AtraccionesMetodos
from logging import getLogger  # Importa el logger configurado globalmente
logger = getLogger("RequestLogger")  # Usa el logger configurado en el middleware


# Crear el router para atracciones
atracciones_router = APIRouter(prefix="/atracciones", tags=["Atracciones"])

@atracciones_router.get(
    "/{atraccion_id}",
    summary="Obtener información de una atracción por ID",
    description="Este endpoint permite a un usuario autenticado proporcionar un ID único para obtener la información detallada de una atracción específica.",
    responses={
        200: {"description": "Solicitud exitosa, retorna los detalles de la atracción."},
        400: {"description": "El ID de la atracción proporcionado no es válido."},
        401: {"description": "El usuario no está autenticado o el token es inválido."},
        404: {"description": "No se encontró una atracción con el ID proporcionado."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def get_attraction_by_id(atraccion_id: str):
    """
    Endpoint para obtener las Atracciones por ID.
    """
    try:
        
        if not atraccion_id.isdigit():
            logger.warning(f"ID de atracción no válido: {atraccion_id}")
            raise HTTPException(status_code=400, detail="El atraccion_id debe ser un número válido.")
        
        atraccion = AtraccionesMetodos.select_atraccion(atraccion_id)
        if atraccion.existe:
            logger.info(f"Atracción encontrada: {atraccion}")
            return {"success": True, "message": "Atracción encontrada", "data": atraccion}
        else:
            logger.warning(f"No se encontró atracción con ID: {atraccion_id}")
            return {"success": False, "message": "Atracción no encontrada"}
    except HTTPException as e:
        logger.error(f"HTTPException en /atracciones: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error inesperado en /atracciones: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado al obtener la atracción: {str(e)}")


# Ruta para crear o actualizar una atracción
@atracciones_router.put(
    "/save",
    summary="Crear o actualizar una atracción",
    description="Este endpoint permite a un usuario autenticado crear una nueva atracción o actualizar una atracción existente.",
    responses={
        200: {"description": "Atracción creada o actualizada con éxito."},
        400: {"description": "Los datos proporcionados no son válidos."},
        401: {"description": "El usuario no está autenticado o el token es inválido."},
        404: {"description": "No se encontró una atracción con el ID proporcionado."},
        500: {"description": "Error inesperado al procesar la solicitud."}
    }
)
async def save_attraction(
    nombre: str, 
    descripcion: str, 
    atraccion_id: Optional[str] = None,  # Atracción ID ahora es opcional
    current_user: str = Security(jwtMetodos.validate_token)
):
    """
    Endpoint para crear o actualizar una atracción.
    Si se pasa un `atraccion_id`, se actualizará la atracción. Si no, se creará una nueva.
    """
    try:
        logger.info(f"Usuario {current_user} intentó guardar o actualizar la atracción con ID: {atraccion_id}")

        # Si atraccion_id es None o 0, tratamos la solicitud como una creación
        if atraccion_id is None or atraccion_id == '0':
            logger.info("Creando una nueva atracción...")
        
        # Crear o actualizar la atracción utilizando el método correspondiente
        atraccion = AtraccionesClass(
            nombre=nombre,
            descripcion=descripcion,
            atraccion_id=atraccion_id if atraccion_id else 0  # Si no se pasa atraccion_id, se asigna 0
        )
        
        # Llamar al método para guardar la atracción (crear o actualizar)
        atraccion_id = AtraccionesMetodos.atraccion_guardar(atraccion)

        if atraccion_id:
            logger.info(f"Atracción guardada/actualizada con éxito. ID: {atraccion_id}")
            return {"success": True, "message": f"Atracción guardada con éxito. ID: {atraccion_id}", "data": {"atraccion_id": atraccion_id}}
        else:
            logger.warning(f"No se pudo guardar/actualizar la atracción con ID: {atraccion_id}")
            raise HTTPException(status_code=400, detail="Error al guardar o actualizar la atracción")

    except HTTPException as e:
        logger.error(f"HTTPException en /atracciones/save: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error inesperado en /atracciones/save: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado al guardar o actualizar la atracción: {str(e)}")
