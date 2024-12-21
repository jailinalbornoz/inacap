import socket
from logging import getLogger  # Importa el logger configurado globalmente
logger = getLogger("RequestLogger")  # Usa el logger configurado en el middleware
from datetime import datetime

class generalesMetodos:

    @staticmethod
    def getIP():
        try:
            # Obtener el nombre de la máquina
            hostname = socket.gethostname()
            # Obtener la dirección IP
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except Exception as e:
            logger.error(f"Exception en getIP(): {e}")
            raise e
            
    @staticmethod
    def es_fecha_valida(texto, formato='%d-%m-%Y'):
        try:
            # Intentar convertir el texto a un objeto datetime con el formato 'dd-mm-yyyy'
            fecha = datetime.strptime(texto, formato)
            return fecha  # Si es válida, devolver el objeto datetime
        except ValueError:
            # Si ocurre un ValueError, el texto no es una fecha válida
            return False  # Si no es válida, devolver False

