import uvicorn
from fastapi import FastAPI, Form, HTTPException, Header, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta, timezone
import jwt
from functools import wraps
from Metodos.UsuariosMetodos import UsuariosMetodos
from Clases.UsuariosClass import UsuariosClass

app = FastAPI(
    title="API con JWT",
    description="Una API simple con autenticación JWT usando FastAPI con conexión a Oracle BD Cloud via EASY WAY.",
    version="1.1.0",    
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

SECRET_KEY = "4f4c62f7c89eaa2b12df2c82d39d6b9b881d62b15ff8069e9d14d45c85a7123b"

# Configuración de la seguridad con OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Decorador para validar JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Accede a la solicitud desde FastAPI usando Request
        request = kwargs.get('request')  # Asegúrate de recibir el request en la función
        token = request.headers.get('Authorization')
        if not token:
            return JSONResponse(status_code=403, content={"message": "Token es requerido"})
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return JSONResponse(status_code=403, content={"message": "El token ha expirado"})
        except jwt.InvalidTokenError:
            return JSONResponse(status_code=403, content={"message": "Token inválido"})
        return f(*args, **kwargs)
    return decorated

# Función para crear un token JWT
def create_access_token(data: dict):
    try:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return encoded_jwt
    except Exception as e:
        raise

@app.post("/token")
def login_for_access_token(username: str, password: str):
    try:
        usuario = UsuariosClass("JRK","Abcdefghijk11")
        #usuario = UsuariosClass(username, password)
        UsuariosMetodos.select_usuario_pass(usuario)
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error al obtener el token")

# Ruta protegida que requiere token JWT
@app.get("/protected")
async def usuarioGet(id: str, token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = decoded_token.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Token inválido")
        usuario = UsuariosMetodos.select_usuario(id)
        return {"message": f"Hello {username}, you have access to this route!"}
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Token inválido")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8081)