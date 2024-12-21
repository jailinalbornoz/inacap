from Clases.AtraccionesClass import AtraccionesClass
from Metodos.OracleMetodos import OracleMetodos
import logging

# Configurar el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class AtraccionesMetodos:

    @staticmethod
    def select_atraccion(atraccion_id, connection=None):
        cursorPython = None
        db = OracleMetodos()  # Instancia de la clase para manejar Oracle       
        local_connection = False  # Indica si la conexión fue creada localmente  

        try:
            logger.info(f"Intentando obtener la atracción con ID: {atraccion_id}")

            if not connection:
                connection = db.connect()
                local_connection = True  # Marcar que la conexión fue creada localmente            

            cursorPython = connection.cursor()
            resultado_cursorOracle = db.create_ref_cursor(cursorPython)

            # Llamar al procedimiento almacenado
            cursorPython.callproc(
                "atracciones_prc_select_row",
                [atraccion_id, resultado_cursorOracle]
            )

            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                logger.info(f"Atracción encontrada con ID: {atraccion_id}")
                return AtraccionesClass(rows[1], rows[2], atraccion_id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            logger.warning(f"No se encontró atracción con ID: {atraccion_id}")
            return AtraccionesClass(None, None, atraccion_id=None, existe=False)

        except Exception as e:
            logger.error(f"Error al obtener la atracción con ID {atraccion_id}: {e}")
            raise
        finally:
            if cursorPython:
                cursorPython.close()
            if local_connection and connection:
                connection.close()

    @staticmethod
    def atraccion_guardar(atraccion, connection=None):
        cursor = None
        db = OracleMetodos()  # Instancia de la clase para manejar Oracle
        local_connection = False  # Indica si la conexión fue creada localmente

        try:
            # Crear conexión si no se proporcionó una
            if connection is None:
                connection = db.connect()
                local_connection = True

            logger.info(f"Verificando existencia de la atracción con ID: {atraccion.atraccion_id}")
            atraccion.existe = AtraccionesMetodos.select_atraccion(atraccion.atraccion_id, connection).existe

            cursorPython = connection.cursor()
            v_salida = cursorPython.var(int)  # Variable de salida para el ID generado o actualizado            

            # Determinar si es un INSERT o un UPDATE
            if atraccion.existe:
                procedimiento = "ATRACCIONES_PRC_UPDATE"
                params = [atraccion.atraccion_id, atraccion.nombre, atraccion.descripcion, v_salida]
                operacion = "actualizado"
                logger.info(f"Actualizando atracción con ID: {atraccion.atraccion_id}")
            else:
                procedimiento = "ATRACCIONES_PRC_INSERT"
                params = [atraccion.nombre, atraccion.descripcion, v_salida]
                operacion = "insertado"
                logger.info(f"Creando nueva atracción: {atraccion.nombre}")

            # Llamar al procedimiento almacenado
            cursorPython.callproc(procedimiento, params)

            # Obtener el ID generado o actualizado
            atraccion.atraccion_id = v_salida.getvalue()

            # Confirmar los cambios solo si la conexión fue creada localmente
            if local_connection:
                connection.commit()

            logger.info(f"Atracción {operacion} con éxito. ID: {atraccion.atraccion_id}")
            return atraccion.atraccion_id

        except Exception as e:
            # Hacer rollback si ocurre un error
            if connection and local_connection:
                connection.rollback()
            logger.error(f"Error al guardar o actualizar la atracción: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if local_connection and connection:
                connection.close()
