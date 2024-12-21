from Config.oracleConfig import oracleConfig
from Config.bcryptConfig import bcryptConfig
from Clases.usuariosClass import usuariosClass

class usuariosMetodos:

    @staticmethod
    def loginUsuarios(rut, password):
        """
        Obtiene un personaje específico usando personajes_prc_select_row.
        :param personaje_id: ID del personaje a buscar.
        :return: Instancia de PersonajesClass con los datos obtenidos.
        """     
        cursorPython = None
        connection = oracleConfig().connect()
        try:
            cursorPython = connection.cursor()
            resultado_cursorOracle = oracleConfig().create_ref_cursor(cursorPython)

            cursorPython.callproc(
                "USUARIOS_PRC_SELECT_ROW_RUT",
                [rut, resultado_cursorOracle]
            )
        
            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                stored_hash = rows[5]
                if bcryptConfig.verify_password(stored_hash, password):
                    return usuariosClass(rows[1], rows[2], rows[3], rows[4], stored_hash, rows[6], id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            return usuariosClass(None, None, None, None, None, None, None, existe=False)
        except Exception as e:
            print(f"Error al obtener el personaje: {str(e).split("\n")[0]}")
            raise
        finally:
            # Cerrar el cursor
            if cursorPython:
                cursorPython.close()
            connection.close()