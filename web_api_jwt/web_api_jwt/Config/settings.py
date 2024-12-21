from dotenv import load_dotenv
import os

# Carga las variables de entorno
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DSN = os.getenv("DSN")