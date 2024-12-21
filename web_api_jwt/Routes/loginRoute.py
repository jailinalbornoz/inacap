from fastapi import APIRouter, HTTPException
from Metodos.jwtMetodos import jwtMetodos
from Metodos.UsuariosMetodos import UsuariosMetodos
from logging import getLogger  # Importa el logger configurado globalmente
logger = getLogger("RequestLogger")  # Usa el logger configurado en el middleware

# Crear el router para login
login_router = APIRouter(prefix="/login", tags=["Login"])

@login_router.post(
    "/",
    summary="Método para que el usuario haga el login",
    description="Este método permite que un usuario ingrese sus credenciales y obtenga un token de acceso JWT.",
    responses={
        200: {"description": "Login exitoso, retorna el token JWT"},
        401: {"description": "Credenciales inválidas"},
        500: {"description": "Error inesperado"}
    }
)
async def login(username: str, password: str):
    """
    Endpoint para login. Genera un token si las credenciales son válidas.
    """
    try:
        logger.info(f"Intento de login con username: {username}")
        
        if not username.isdigit():
            logger.warning(f"El username ingresado no es válido: {username}")
            raise HTTPException(status_code=400, detail="El nombre de usuario debe ser un número válido.")
        
        usuario = UsuariosMetodos.loginUsuarios(username, password)
        logger.info(f"Usuario encontrado: {usuario.existe}")
        
        if usuario.existe:
            token = jwtMetodos.create_access_token({"sub": username})
            logger.info(f"Token generado para el usuario: {username}")
            return {"success": True, "message": "Login exitoso", "data": {"token": token}}
        else:
            logger.warning(f"Intento de login fallido para el usuario: {username}")
            return {"success": False, "message": "Rut y/o contraseña inválida"}
    except HTTPException as e:
        logger.error(f"HTTPException en login: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error inesperado en login: {e}")
        raise HTTPException(status_code=500, detail=f"Error inesperado al generar el token: {str(e)}")
