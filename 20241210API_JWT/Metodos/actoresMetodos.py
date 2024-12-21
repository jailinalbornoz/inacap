from Clases.actoresClass import actoresClass
from Config import oracleConfig

class actoresMetodos:

    @staticmethod
    def select_actor(id, connection = None):
        """
        Obtiene un personaje específico usando personajes_prc_select_row.
        :param personaje_id: ID del personaje a buscar.
        :return: Instancia de PersonajesClass con los datos obtenidos.
        """     
        cursorPython = None
        db = oracleConfig()  # Instancia de la clase para manejar Oracle       
        
        local_connection = False  # Indica si la conexión fue creada localmente  
        try:
            if not connection:
                connection = db.connect()
                local_connection = True  # Marcar que la conexión fue creada localmente           
            
            cursorPython = connection.cursor()
            resultado_cursorOracle = db.create_ref_cursor(cursorPython)

            # Llamar al procedimiento almacenado
            cursorPython.callproc(
                "personajes_prc_select_row",
                [personaje_id, resultado_cursorOracle]
            )
            
            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                return PersonajesClass(rows[1], rows[2], rows[3], personaje_id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            return PersonajesClass(None, None, None, personaje_id=None, existe=False)
            
        except Exception as e:
            print(f"Error al obtener el personaje: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursorPython:
                cursorPython.close()
            # Si la conexión fue creada localmente, cerrarla
            if local_connection and connection:
                connection.close()
    
    @staticmethod
    def personaje_guardar(personaje, connection=None):
        """
        Inserta o actualiza un personaje según el valor de `personaje.existe`.
        :param personaje: Instancia de PersonajesClass.
        :param connection: Conexión activa opcional.
        :return: ID generado o actualizado del personaje.
        """
        cursor = None
        db = OracleMetodos()  # Instancia de la clase para manejar Oracle
        local_connection = False  # Indica si la conexión fue creada localmente

        try:
            # Crear conexión si no se proporcionó una
            if connection is None:
                connection = db.connect()
                local_connection = True

            # Crear el cursor
            cursorPython = connection.cursor()
            v_salida = cursorPython.var(int)  # Variable de salida para el ID generado o actualizado

            # Determinar si es un INSERT o un UPDATE
            if personaje.existe:
                procedimiento = "PERSONAJES_PRC_UPDATE"
                params = [personaje.personaje_id, personaje.nombre, personaje.especialidad, personaje.nivel_locura, v_salida]
                operacion = "actualizado"
            else:
                procedimiento = "PERSONAJES_PRC_INSERT"
                params = [personaje.nombre, personaje.especialidad, personaje.nivel_locura, v_salida]
                operacion = "insertado"

            # Llamar al procedimiento almacenado
            cursorPython.callproc(procedimiento, params)

            # Obtener el ID generado o actualizado
            personaje.personaje_id = v_salida.getvalue()

            # Confirmar los cambios solo si la conexión fue creada localmente
            if local_connection:
                connection.commit()

            print(f"Personaje {operacion} con éxito. ID: {personaje.personaje_id}")
            return personaje.personaje_id

        except Exception as e:
            # Hacer rollback si ocurre un error
            if connection and local_connection:
                connection.rollback()           
            raise
        finally:
            # Cerrar el cursor si fue creado
            if cursor:
                cursor.close()

            # Cerrar la conexión si fue creada localmente
            if local_connection and connection:
                connection.close()