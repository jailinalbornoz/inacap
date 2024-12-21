from dotenv import load_dotenv
import oracledb
import os


class OracleMetodos:
    def __init__(self, env_file=".env.development"):
        """Inicializa la clase cargando variables de entorno y configurando Oracle."""
        # Cargar las variables de entorno
        load_dotenv(env_file)

        # Configuración desde el archivo .env
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.dsn = os.getenv("DSN")
        self.config_dir = os.getenv("RUTA")  # Ruta al Wallet desde el archivo .env
        os.environ['TNS_ADMIN'] = self.config_dir
        # Validar configuración requerida
        if not all([self.user, self.password, self.dsn, self.config_dir]):
            raise ValueError("Faltan configuraciones requeridas (USER, PASSWORD, DSN, RUTA).")
        
    def connect(self):
        """Establece y retorna una conexión a la base de datos Oracle."""
        try:
            # Inicializar el cliente Oracle con la ruta del Wallet
            oracledb.init_oracle_client(config_dir=self.config_dir)
            connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            print("Conexión exitosa a la base de datos.")
            return connection
        except oracledb.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None    

    def create_ref_cursor(self, cursor):
        """
        Crea una variable de tipo SYS_REFCURSOR usando el cursor proporcionado.
        :param cursor: Cursor activo asociado a una conexión.
        :return: Variable de tipo SYS_REFCURSOR.
        """
        return cursor.var(oracledb.CURSOR)




"""
import oracledb

# Ruta al Wallet en tu sistema
config_dir = r"C:\web_api_jwt\Wallet"  # Usa 'r' para evitar problemas con las barras

try:
    # Inicializar el cliente Oracle con la ruta del Wallet
    oracledb.init_oracle_client(config_dir=config_dir)

    # Conexión a la base de datos
    connection = oracledb.connect(
        user="admin",  # Cambia si usas otro usuario
        password="Abcdefghijk11",  # Cambia por tu contraseña
        dsn="vncx26inp55ph37b_high",  # Alias desde tnsnames.ora
    )
    print("Conexión exitosa:", connection.version)

    # Realizar una consulta de prueba
    with connection.cursor() as cursor:
        cursor.execute("SELECT SYSDATE FROM DUAL")
        result = cursor.fetchone()
        print("Fecha actual en la base de datos:", result)

except oracledb.DatabaseError as e:
    print("Error al conectar a la base de datos:", e)

finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("Conexión cerrada.")

"""