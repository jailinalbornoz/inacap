from dotenv import load_dotenv
import oracledb
import os


class OracleMetodos:
    
    @staticmethod
    def connect():
        """Inicializa las  variables de entorno y configurando Oracle."""
        # Cargar las variables de entorno
        load_dotenv(".env.development")

        # Configuración desde el archivo .env
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        host = os.getenv("HOST")
        service_name = os.getenv("SERVICE_NAME")
        port = os.getenv("PORT")
        """Establece y retorna una conexión a la base de datos Oracle."""
        try:
            # Crear el DSN manualmente con formato correcto
            dsn = (
                "(DESCRIPTION="
                "(ADDRESS=(PROTOCOL=tcps)(HOST={host})(PORT={port}))"
                "(CONNECT_DATA=(SERVICE_NAME={service_name}))"
                "(SECURITY=(SSL_SERVER_CERT_DN_MATCH=yes))"
                ")"
            ).format(host=host, port=port, service_name=service_name)

            connection = oracledb.connect(user=user, password=password, dsn=dsn)
            print(f"Conexión exitosa a la base de datos.")
            return connection
        except oracledb.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise   

    @staticmethod
    def create_ref_cursor(cursor):
        """
        Crea una variable de tipo SYS_REFCURSOR usando el cursor proporcionado.
        :param cursor: Cursor activo asociado a una conexión.
        :return: Variable de tipo SYS_REFCURSOR.
        """
        return cursor.var(oracledb.CURSOR)




# """
# import oracledb

# # Ruta al Wallet en tu sistema
# config_dir = r"C:\web_api_jwt\Wallet"  # Usa 'r' para evitar problemas con las barras

# try:
#     # Inicializar el cliente Oracle con la ruta del Wallet
#     oracledb.init_oracle_client(config_dir=config_dir)

#     # Conexión a la base de datos
#     connection = oracledb.connect(
#         user="admin",  # Cambia si usas otro usuario
#         password="Abcdefghijk11",  # Cambia por tu contraseña
#         dsn="vncx26inp55ph37b_high",  # Alias desde tnsnames.ora
#     )
#     print("Conexión exitosa:", connection.version)

#     # Realizar una consulta de prueba
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT SYSDATE FROM DUAL")
#         result = cursor.fetchone()
#         print("Fecha actual en la base de datos:", result)

# except oracledb.DatabaseError as e:
#     print("Error al conectar a la base de datos:", e)

# finally:
#     if 'connection' in locals() and connection:
#         connection.close()
#         print("Conexión cerrada.")

# """