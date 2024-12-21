from fastapi import FastAPI
from Config.logMiddleware import LogMiddleware
from Routes.loginRoute import login_router
from Routes.atraccionesRoute import atracciones_router
from Routes.apisRoute import apis_router
from Config.settings import settings
from Metodos.UsuariosMetodos import UsuariosMetodos
import uvicorn

# Crear la aplicación
app = FastAPI(
    title="API con JWT",
    description="API simple con autenticación JWT usando FastAPI",
    version="1.1.0"
)

# Instanciar la clase de middleware
log_middleware = LogMiddleware()

# Registrar el middleware
@app.middleware("http")
async def log_requests_middleware(request, call_next):
    return await log_middleware.log_requests(request, call_next)

# Registrar routers
app.include_router(login_router)
app.include_router(atracciones_router)
app.include_router(apis_router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.APIHOST, port=int(settings.APIPORT))