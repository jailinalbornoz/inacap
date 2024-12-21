
from Metodos.OracleMetodos import OracleMetodos
from Metodos.bcryptMetodos import bcryptMetodos
from Clases.UsuariosClass import UsuariosClass

class UsuariosMetodos:
    names = [
    "jailinAndrea",
    "keilaGenesis",
    "constanzaRocio",
    "sergioThomas",
    "andresDaniel",
    "francoAntonio",
    "benjaminGabriel",
    "macarenaGabriela",
    "johannaMaria",
    "leonardoJavier",
    "marcAnthony",
    "alejandroFidel",
    "haroldSebastian",
    "jacquesLapierre",
    "nicolasJosemaria",
    "benjaminIgnacio",
    "mariaCarmen",
    "camiloJuan",
    "diegoTomas",
    "kevinJonathan",
    "rigobertoAndres",
    "marlenAdriana",
    "mairaBelen",
    "joseGabriel",
    "jorgeIgnacio",
    "benjaminFrancisco",
    "jorgeRutherford"
]

    @staticmethod
    def login(self, username: str, password: str):
        """
        Valida las credenciales y genera un token si son válidas.
        """
        # if username != "admin" or password != "admin":
        #     raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        return self.jwt_manager.create_access_token({"sub": username})

    @staticmethod
    def getUsuariosDirectos():
        lista = [
            {
                "rut": "10101010",
                "nombre": "Clark",
                "apellido": "Kent",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_superman123"
            },
            {
                "rut": "20202020",
                "nombre": "Bruce",
                "apellido": "Wayne",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_batman456"
            },
            {
                "rut": "30303030",
                "nombre": "Diana",
                "apellido": "Prince",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_wonderwoman789"
            },
            {
                "rut": "40404040",
                "nombre": "Barry",
                "apellido": "Allen",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_flash123"
            },
            {
                "rut": "50505050",
                "nombre": "Hal",
                "apellido": "Jordan",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_greenlantern456"
            },
            {
                "rut": "60606060",
                "nombre": "Arthur",
                "apellido": "Curry",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_aquaman789"
            },
            {
                "rut": "70707070",
                "nombre": "Peter",
                "apellido": "Parker",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_spiderman123"
            },
            {
                "rut": "80808080",
                "nombre": "Tony",
                "apellido": "Stark",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_ironman456"
            },
            {
                "rut": "90909090",
                "nombre": "Steve",
                "apellido": "Rogers",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_captainamerica789"
            },
            {
                "rut": "10111213",
                "nombre": "Natasha",
                "apellido": "Romanoff",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_blackwidow123"
            },
            {
                "rut": "16014818",
                "nombre": "Jorge",
                "apellido": "Rutherford",
                "estado": 1,
                "password_hash": "",
                "password_plain": "hash_Kratos$"
            }
        ]
        # Convertir la lista de diccionarios en una lista de objetos PersonajesClass
        usuarios = [
            UsuariosClass(
                rut=usuario["rut"],
                nombre=usuario["nombre"],
                apellido=usuario["apellido"],
                estado=usuario["estado"],
                password_hash=usuario["password_hash"],
                password_plain=usuario["password_plain"]
            )
            for usuario in lista
        ]
        return usuarios

    @staticmethod
    def borrarTablaPrcDatos():
        # Lista de usuarios
        try:
            connection = OracleMetodos.connect()
            for item in UsuariosMetodos.names:
                cursor = connection.cursor()
                # Crear una query SQL para crear la tabla en la base de datos
                sql_query = f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE ' || '{item}.USUARIOS CASCADE CONSTRAINTS PURGE' ; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;"
                cursor.execute(sql_query)
                print(f"Tabla usuarios Borrada")
                # # Crear una query SQL para borrar la el PRC en la base de datos
                # sql_query = f'drop procedure {item}.USUARIOS_PRC_SELECT_ROW_RUT'
                # cursor.execute(sql_query)
                # sql_query = f'drop procedure {item}.USUARIOS_PRC_SELECT_ROW'
                # cursor.execute(sql_query)
                print(f"Procedimiento PROCEDURE Borrado")
            connection.commit()
        except Exception as e:
            print(f"Error al borrar: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def crearTablaPRC():
        # Lista de usuarios
        try:
            connection = OracleMetodos.connect()
            for item in UsuariosMetodos.names:
                cursor = connection.cursor()
                # Crear una query SQL para crear la tabla en la base de datos
                sql_query = f'CREATE TABLE {item}.usuarios (id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY, rut NUMBER UNIQUE NOT NULL, nombre VARCHAR2(100) NOT NULL, apellido VARCHAR2(100) NOT NULL, estado NUMBER(1) DEFAULT 1 NOT NULL, password_hash VARCHAR2(255) NOT NULL, password_plain VARCHAR2(100) NOT NULL)'            
                cursor.execute(sql_query)
                print(f"Tabla usuarios Creada")
                # Crear una query SQL para crear la el PRC en la base de datos
                sql_query = f"""
                    create or replace PROCEDURE {item}.USUARIOS_PRC_SELECT_ROW (
                        v_id IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN   
                        OPEN cursor_resultado FOR
                            SELECT id, rut, nombre,apellido, estado, password_hash, password_plain 
                            FROM {item}.usuarios
                            WHERE id = v_id;
                    END;
                """
                cursor.execute(sql_query)
                print(f"Procedimiento USUARIOS_PRC_SELECT_ROW_RUT creado")
                # Crear una query SQL para crear la el PRC en la base de datos
                sql_query = f"""
                    create or replace PROCEDURE {item}.USUARIOS_PRC_SELECT_ROW_RUT (
                        v_rut IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN   
                        OPEN cursor_resultado FOR
                            SELECT id, rut, nombre,apellido, estado, password_hash, password_plain 
                            FROM {item}.usuarios
                            WHERE rut = v_rut;
                    END;
                """
                cursor.execute(sql_query)
                print(f"Procedimiento USUARIOS_PRC_SELECT_ROW creado")
            connection.commit()
            print("Usuarios insertados correctamente.")
        except Exception as e:
            print(f"Error al insertar usuarios: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def insertarDatos():
        # Lista de usuarios
        try:            
            connection = OracleMetodos.connect()
            for item in UsuariosMetodos.names:
                for usuario in UsuariosMetodos.getUsuariosDirectos():         
                    cursor = connection.cursor()              
                    # Crear una consulta SQL para insertar en la base de datos
                    usuario.password_hash = bcryptMetodos.hash_password(usuario.password_plain)
                    sql_query = f"INSERT INTO {item}.usuarios (rut, nombre, apellido, estado, password_hash, password_plain) VALUES ({usuario.rut}, '{usuario.nombre}', '{usuario.apellido}', {usuario.estado}, '{usuario.password_hash}', '{usuario.password_plain}')"
                    cursor.execute(sql_query)
                    print(f"Usuarios {usuario.nombre} {usuario.apellido} insertado correctamente.")
            connection.commit()
        except Exception as e:
            print(f"Error al insertar usuarios: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def loginUsuariosDirectos():
        """
        Obtiene un personaje específico usando personajes_prc_select_row.
        :param personaje_id: ID del personaje a buscar.
        :return: Instancia de PersonajesClass con los datos obtenidos.
        """     
        cursorPython = None
        connection = OracleMetodos().connect()
        try:
            cursorPython = connection.cursor()
            resultado_cursorOracle = OracleMetodos().create_ref_cursor(cursorPython)
            usuarios = UsuariosMetodos.getUsuariosDirectos()
            for usuario in usuarios:
                # Llamar al procedimiento almacenado
                print(f"El rut del usuario seleccionado es el: {usuario.rut}")
                cursorPython.callproc(
                    "USUARIOS_PRC_SELECT_ROW_RUT",
                    [str(usuario.rut), resultado_cursorOracle]
                )
            
                # Obtener el cursor devuelto por el procedimiento
                cursor_resultadoIntermediario = resultado_cursorOracle.getvalue()

                # Verificar si hay filas en el cursor
                rows = cursor_resultadoIntermediario.fetchone()
                if rows:
                    stored_hash = rows[5]
                    if bcryptMetodos.verify_password(stored_hash, usuario.password_plain):
                        usuario.existe = True
                        usuario.id = rows[0]
            
            return usuarios
        except Exception as e:
            print(f"Error al obtener el personaje: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursorPython:
                cursorPython.close()
            connection.close()

    @staticmethod
    def loginUsuarios(rut, password):
        """
        Obtiene un personaje específico usando personajes_prc_select_row.
        :param personaje_id: ID del personaje a buscar.
        :return: Instancia de PersonajesClass con los datos obtenidos.
        """     
        cursorPython = None
        connection = OracleMetodos().connect()
        try:
            cursorPython = connection.cursor()
            resultado_cursorOracle = OracleMetodos().create_ref_cursor(cursorPython)

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
                if bcryptMetodos.verify_password(stored_hash, password):
                    return UsuariosClass(rows[1], rows[2], rows[3], rows[4], stored_hash, rows[6], id=rows[0], existe=True)
            
            # Retorna un objeto con existe=False si no hay datos
            return UsuariosClass(None, None, None, None, None, None, None, existe=False)
        except Exception as e:
            print(f"Error al obtener el personaje: {e}")
            raise
        finally:
            # Cerrar el cursor
            if cursorPython:
                cursorPython.close()
            connection.close()