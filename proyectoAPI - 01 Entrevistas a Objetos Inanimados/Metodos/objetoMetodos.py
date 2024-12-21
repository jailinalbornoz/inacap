from Metodos.logDataMetodos import logDataMetodos
from Config.oracleConfig import oracleConfig
from Clases.objetoClass import objetoClass
from Metodos.generalesMetodos import generalesMetodos

class objetoMetodos:

    @staticmethod
    def select_objeto_nombre(nombre_objeto, connection=None):
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
                "OBJETOS_PRC_SELECT_ROW_NOMBRE",
                [nombre_objeto, resultado_cursorOracle]
            )
        
            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                return objetoClass(rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            return objetoClass(None, None, None, None, None, existe=False)
        
        except Exception as e:
            print(f"Error al obtener el objeto: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursorPython:
                cursorPython.close()
            # Si la conexión fue creada localmente, cerrarla
            if local_connection and connection:
                connection.close()

    @staticmethod
    def objeto_guardar(objeto, connection=None):
        cursorPython = None
        db = oracleConfig()  # Instancia para manejar conexiones Oracle
        local_connection = False  # Indica si la conexión fue creada localmente.

        try:
            #Crear conexión si no se proporcionó una
            if connection is None:
                connection = db.connect()
                local_connection = True

            #Crear un cursor para la ejecución de SQL
            cursorPython = connection.cursor()
            v_salida = cursorPython.var(int)  # Variable de salida para el ID generado/actualizado.

            #Verificar si el objeto existe en la base de datos
            objetoDesdeBD = objetoMetodos.select_objeto_nombre(objeto.nombre_objeto, connection)

            #Determinar si es un INSERT o un UPDATE según la existencia del objeto
            if objetoDesdeBD.existe:
                # Config para UPDATE
                procedimiento = "OBJETOS_PRC_UPDATE"
                objeto.usuario_modificacion = objetoDesdeBD.usuario_modificacion
                objeto.fecha_modificacion = objetoDesdeBD.fecha_modificacion
                objeto.existe = objetoDesdeBD.existe
                valorAnterior = generalesMetodos.objeto_a_json(objetoDesdeBD)

                params = [
                    objeto.id,
                    objeto.nombre_objeto,
                    objeto.descripcion_objeto,
                    objeto.usuario_creacion,
                    objeto.fecha_creacion,
                    objeto.ip,
                    objeto.usuario_modificacion,
                    objeto.fecha_modificacion,
                    v_salida
                ]
                operacion = "actualizado" 

            else:
                # Config para INSERT
                procedimiento = "OBJETOS_PRC_INSERT"
                valorAnterior = "Nuevo Registro" 

                params = [
                    objeto.nombre_objeto,
                    objeto.descripcion_objeto,
                    objeto.usuario_creacion,
                    objeto.fecha_creacion,
                    objeto.ip,
                    objeto.usuario_modificacion,
                    objeto.fecha_modificacion,
                    v_salida
                ]
                operacion = "insertado" 

            #Ejecutar el procedimiento almacenado 
            cursorPython.callproc(procedimiento, params)

            #Obtener el ID generado o actualizado
            objeto.id = v_salida.getvalue()

            #Insertar un registro en el log
            valorNuevo = generalesMetodos.objeto_a_json(objeto)  # Estado actualizado del objeto.
            logDataMetodos.insertLog(valorAnterior, valorNuevo, connection)

            # 8. Confirmar los cambios si la conexión fue creada localmente
            if local_connection:
                connection.commit()

            print(f"Objeto {operacion} con éxito. ID: {objeto.id}")
            return objeto.id

        except Exception as e:
            # Hacer rollback si ocurre un error
            if connection and local_connection:
                connection.rollback()
            print(f"Error al guardar el objeto: {e}")
            raise
        finally:
            # 9. Cerrar el cursor si fue creado
            if cursorPython:
                cursorPython.close()

            # 10. Cerrar la conexión si fue creada localmente
            if local_connection and connection:
                connection.close()
