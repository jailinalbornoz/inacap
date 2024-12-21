from Metodos.OracleMetodos import OracleMetodos
from Clases.UsuariosClass import UsuariosClass
from Metodos.bcryptMetodos import bcryptMetodos
class UsuariosMetodos:

    @staticmethod
    def select_usuario(usuario_id, connection=None):
        """
        Obtiene un usuario específico usando usuarios_prc_select_row.
        :param usuario_id: ID del usuario a buscar.
        :return: Instancia de UsuariosClass con los datos obtenidos.
        """     
        cursor = None
        db = OracleMetodos()  # Instancia de la clase para manejar Oracle       
        local_connection = False  # Indica si la conexión fue creada localmente  
        try:
            if not connection:
                connection = db.connect()
                local_connection = True  # Marcar que la conexión fue creada localmente           
            
            cursorPython = connection.cursor()
            resultado_cursorOracle = db.create_ref_cursor(cursorPython)

            # Llamar al procedimiento almacenado
            cursorPython.callproc(
                "usuarios_prc_select_row",
                [usuario_id, resultado_cursorOracle]
            )
            
            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                return UsuariosClass(rows[1], rows[2], id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            return UsuariosClass(None, None, id=None, existe=False)
            
        except Exception as e:
            print(f"Error al obtener el personaje: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursor:
                cursor.close()
            # Si la conexión fue creada localmente, cerrarla
            if local_connection and connection:
                connection.close()

    @staticmethod
    def select_usuario_pass(usuario, connection=None):
        """
        Obtiene un usuario específico usando usuarios_prc_select_row.
        :param usuario_id: ID del usuario a buscar.
        :return: Instancia de UsuariosClass con los datos obtenidos.
        """     
        cursor = None
        db = OracleMetodos()  # Instancia de la clase para manejar Oracle       
        local_connection = False  # Indica si la conexión fue creada localmente  
        try:
            if not connection:
                connection = db.connect()
                local_connection = True  # Marcar que la conexión fue creada localmente           
            
            cursorPython = connection.cursor()
            resultado_cursorOracle = db.create_ref_cursor(cursorPython)

            # Llamar al procedimiento almacenado
            cursorPython.callproc(
                "USUARIOS_PRC_SELECT_USER",
                [usuario.username, resultado_cursorOracle]
            )
            
            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                stored_hash = rows[2]
                
                # Verificar si la contraseña proporcionada coincide con el hash almacenado
                if bcryptMetodos.verify_password(stored_hash, usuario.password):
                    # La contraseña es correcta
                    return UsuariosClass(rows[1], rows[2], id=rows[0], existe=True)
                else:
                    # La contraseña es incorrecta
                    return UsuariosClass(None, None, id=None, existe=False)
            
            # Retorna un objeto con existe=False si no hay datos
            return UsuariosClass(None, None, id=None, existe=False)
            
        except Exception as e:
            print(f"Error al obtener el personaje: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursor:
                cursor.close()
            # Si la conexión fue creada localmente, cerrarla
            if local_connection and connection:
                connection.close()

    @staticmethod
    def usuario_guardar(usuario, connection=None):
        """
        Inserta o actualiza un usuario según el valor de `usuario.existe`.
        :param usuario: Instancia de UsuarioClass.
        :param connection: Conexión activa opcional.
        :return: ID generado o actualizado del Usuario.
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

            # Hashear la contraseña del usuario con bcrypt
            usuario.password_hash = bcryptMetodos.hash_password(usuario.password)
            usuario.existe = False
            # Determinar si es un INSERT o un UPDATE
            if usuario.existe:
                procedimiento = "USUARIOS_PRC_UPDATE"
                params = [usuario.usuario_id, usuario.username, usuario.password_hash, v_salida]
                operacion = "actualizado"
            else:
                procedimiento = "USUARIOS_PRC_INSERT"
                params = [usuario.username, usuario.password_hash, v_salida]
                operacion = "insertado"

            # Llamar al procedimiento almacenado
            cursorPython.callproc(procedimiento, params)

            # Obtener el ID generado o actualizado
            usuario.usuario_id = v_salida.getvalue()

            # Confirmar los cambios solo si la conexión fue creada localmente
            if local_connection:
                connection.commit()

            print(f"Personaje {operacion} con éxito. ID: {usuario.usuario_id}")
            return usuario.usuario_id

        except Exception as e:
            # Hacer rollback si ocurre un error
            if connection and local_connection:
                connection.rollback()
            print(f"Error al guardar el personaje: {e}")
            raise
        finally:
            # Cerrar el cursor si fue creado
            if cursor:
                cursor.close()

            # Cerrar la conexión si fue creada localmente
            if local_connection and connection:
                connection.close()