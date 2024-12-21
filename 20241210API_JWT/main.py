from fastapi import FastAPI
from Config.logMiddlewareConfig import logMiddlewareConfig
from Routes.loginRoute import login_router
from Routes.actoresRoute import actores_router
from Routes.peliculasRoute import peliculas_router
from Routes.peliculasActoresRoute import peliculasActores_router
from Routes.apisRoute import apis_router
from Config.settingsConfig import settings
from Config.initalBDGeneratorConfig import initalBDGeneratorConfig
import uvicorn

# Crear la aplicación
app = FastAPI(
    title="API con JWT",
    description="API simple con autenticación JWT usando FastAPI",
    version="1.1.0"
)

# Instanciar la clase de middleware
log_middleware = logMiddlewareConfig()

# Registrar el middleware
@app.middleware("http")
async def log_requests_middleware(request, call_next):
    return await log_middleware.log_requests(request, call_next)

# Registrar routers
app.include_router(login_router)
app.include_router(actores_router)
app.include_router(peliculas_router)
app.include_router(peliculasActores_router)
app.include_router(apis_router)

if __name__ == "__main__":
    try:
        uvicorn.run(app, host=settings.APIHOST, port=int(settings.APIPORT)+6)
    except Exception as e:
        print(f"{e}")
        raise Exception(f"Error general en la aplicación: {e}")