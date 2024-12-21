from Metodos.logDataMetodos import logDataMetodos
from Config.oracleConfig import oracleConfig
from Clases.objetoEntrevistaRelClass import objetoEntrevistaRelClass
from Metodos.generalesMetodos import generalesMetodos

class objetoEntrevistaRelMetodos:

    @staticmethod
    def select_objeto_entrevista_rel(id_objeto, id_entrevista, connection=None):
    
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
                "OBJETOS_ENTREVISTAS_PRC_SELECT_ROW",
                [id_objeto, id_entrevista, resultado_cursorOracle]
            )
        
            # Obtener el cursor devuelto por el procedimiento
            cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

            # Verificar si hay filas en el cursor
            rows = cursor_resultadoIntermediario.fetchone()
            if rows:
                return objetoEntrevistaRelClass(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            return objetoEntrevistaRelClass(None, None, None, None, None, None, None, existe=False)
        
        except Exception as e:
            print(f"Error al obtener la relación objeto-entrevista: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursorPython:
                cursorPython.close()
            # Si la conexión fue creada localmente, cerrarla
            if local_connection and connection:
                connection.close()

    @staticmethod
    def objeto_entrevista_rel_guardar(objeto_entrevista_rel, connection=None):
        cursorPython = None
        db = oracleConfig()  # Instancia para manejar conexiones Oracle
        local_connection = False  # Indica si la conexión fue creada localmente.

        try:
            #Crear conexión
            if connection is None:
                connection = db.connect()
                local_connection = True

            #Crear un cursor
            cursorPython = connection.cursor()
            v_salida = cursorPython.var(int)  # Variable de salida para el ID generado/actualizado.

            #Verificar si la relacion existe
            objetoEntrevistaRelDesdeBD = objetoEntrevistaRelMetodos.select_objeto_entrevista_rel(objeto_entrevista_rel.id_objeto, objeto_entrevista_rel.id_entrevista, connection)

            #Determinar si es un INSERT o un UPDATE
            if objetoEntrevistaRelDesdeBD.existe:
                # Config UPDATE
                procedimiento = "OBJETOS_ENTREVISTAS_PRC_UPDATE"
                objeto_entrevista_rel.usuario_modificacion = objetoEntrevistaRelDesdeBD.usuario_modificacion
                objeto_entrevista_rel.fecha_modificacion = objetoEntrevistaRelDesdeBD.fecha_modificacion
                objeto_entrevista_rel.existe = objetoEntrevistaRelDesdeBD.existe
                valorAnterior = generalesMetodos.objeto_a_json(objetoEntrevistaRelDesdeBD)

                params = [
                    objeto_entrevista_rel.id_objeto,
                    objeto_entrevista_rel.id_entrevista,
                    objeto_entrevista_rel.fecha_entrevista,
                    objeto_entrevista_rel.usuario_creacion,
                    objeto_entrevista_rel.fecha_creacion,
                    objeto_entrevista_rel.ip,
                    objeto_entrevista_rel.usuario_modificacion,
                    objeto_entrevista_rel.fecha_modificacion,
                    v_salida
                ]
                operacion = "actualizada"  

            else:
                # Config INSERT
                procedimiento = "OBJETOS_ENTREVISTAS_PRC_INSERT"
                valorAnterior = "Nuevo Registro"

                params = [
                    objeto_entrevista_rel.id_objeto,
                    objeto_entrevista_rel.id_entrevista,
                    objeto_entrevista_rel.fecha_entrevista,
                    objeto_entrevista_rel.usuario_creacion,
                    objeto_entrevista_rel.fecha_creacion,
                    objeto_entrevista_rel.ip,
                    objeto_entrevista_rel.usuario_modificacion,
                    objeto_entrevista_rel.fecha_modificacion,
                    v_salida
                ]
                operacion = "insertada"

            #Ejecutar el procedimiento almacenado
            cursorPython.callproc(procedimiento, params)

            #Obtener el ID generado o actualizado
            objeto_entrevista_rel.id = v_salida.getvalue()

            #Insertar un registro en el log
            valorNuevo = generalesMetodos.objeto_a_json(objeto_entrevista_rel) 
            logDataMetodos.insertLog(valorAnterior, valorNuevo, connection)

            #Confirmar los cambios si la conexión fue creada localmente
            if local_connection:
                connection.commit()

            print(f"Relación entre objeto y entrevista {operacion} con éxito. ID: {objeto_entrevista_rel.id}")
            return objeto_entrevista_rel.id

        except Exception as e:
            # Hacer rollback si ocurre un error
            if connection and local_connection:
                connection.rollback()
            print(f"Error al guardar la relación objeto-entrevista: {e}")
            raise
        finally:
            # Cerrar el cursor si fue creado
            if cursorPython:
                cursorPython.close()

            # Cerrar la conexión si fue creada localmente
            if local_connection and connection:
                connection.close()
