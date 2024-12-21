from oracleConfig import oracleConfig
class initalBDGeneratorConfigPrueba:    
    @staticmethod
    def iniciaDataBase():
        # Lista de usuarios
        print(f"\033[92minitalBDGeneratorConfigPrueba: Proceso INICIADO\033[0m")
        connection = None
        try:
            connection = oracleConfig.connect()
            cursor = connection.cursor()
            drop_commands = [
                "BEGIN EXECUTE IMMEDIATE 'DROP TABLE objeto_entrevista_rel CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN NULL; END;",
                "BEGIN EXECUTE IMMEDIATE 'DROP TABLE objetos CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN NULL; END;",
                "BEGIN EXECUTE IMMEDIATE 'DROP TABLE entrevistas CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN NULL; END;",
                "DROP PROCEDURE objetos_PRC_INSERT",
                "DROP PROCEDURE objetos_PRC_UPDATE",
                "DROP PROCEDURE objetos_PRC_SELECT_ROW",
                "DROP PROCEDURE entrevistas_PRC_INSERT",
                "DROP PROCEDURE entrevistas_PRC_UPDATE",
                "DROP PROCEDURE entrevistas_PRC_SELECT_ROW",
                "DROP PROCEDURE objeto_entrevista_rel_PRC_INSERT",
                "DROP PROCEDURE objeto_entrevista_rel_PRC_UPDATE",
                "DROP PROCEDURE objeto_entrevista_rel_PRC_SELECT_ROW"
            ]
            
            create_commands = [
                """
                CREATE TABLE objetos (
                    id_objeto NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    nombre_objeto VARCHAR2(100) NOT NULL,
                    descripcion_objeto VARCHAR2(255) NOT NULL,
                    usuario_creacion VARCHAR2(50) NOT NULL,
                    fecha_creacion DATE NOT NULL,
                    ip VARCHAR2(50) NOT NULL,
                    usuario_modificacion VARCHAR2(50) NOT NULL,
                    fecha_modificacion DATE NOT NULL
                )
                """,
                """
                CREATE TABLE entrevistas (
                    id_entrevista NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    tema VARCHAR2(100) NOT NULL,
                    duracion_minutos NUMBER NOT NULL,
                    usuario_creacion VARCHAR2(50) NOT NULL,
                    fecha_creacion DATE NOT NULL,
                    ip VARCHAR2(50) NOT NULL,
                    usuario_modificacion VARCHAR2(50) NOT NULL,
                    fecha_modificacion DATE NOT NULL
                )
                """,
                """
                CREATE TABLE objeto_entrevista_rel (
                    id_relacional NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    id_objeto NUMBER NOT NULL,
                    id_entrevista NUMBER NOT NULL,
                    fecha_entrevista DATE NOT NULL,
                    usuario_creacion VARCHAR2(50) NOT NULL,
                    fecha_creacion DATE NOT NULL,
                    ip VARCHAR2(50) NOT NULL,
                    usuario_modificacion VARCHAR2(50) NOT NULL,
                    fecha_modificacion DATE NOT NULL,
                    CONSTRAINT fk_objeto FOREIGN KEY (id_objeto) REFERENCES objetos(id_objeto),
                    CONSTRAINT fk_entrevista FOREIGN KEY (id_entrevista) REFERENCES entrevistas(id_entrevista)
                )
                """
            ]

            procedures_commands = [
                # PROCEDIMIENTO: objetos_PRC_INSERT
                """
                CREATE OR REPLACE PROCEDURE objetos_PRC_INSERT (
                    p_nombre_objeto IN VARCHAR2,
                    p_descripcion_objeto IN VARCHAR2,
                    p_usuario_creacion IN VARCHAR2,
                    p_fecha_creacion IN DATE,
                    p_ip IN VARCHAR2,
                    p_usuario_modificacion IN VARCHAR2,
                    p_fecha_modificacion IN DATE,
                    v_salida OUT NUMBER
                ) AS
                BEGIN
                    INSERT INTO objetos (
                        nombre_objeto, descripcion_objeto, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                    ) VALUES (
                        p_nombre_objeto, p_descripcion_objeto, p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                    )
                    RETURNING id_objeto INTO v_salida;
                END;
                """,

                # PROCEDIMIENTO: objetos_PRC_UPDATE
                """
                CREATE OR REPLACE PROCEDURE objetos_PRC_UPDATE (
                    p_id_objeto IN NUMBER,
                    p_nombre_objeto IN VARCHAR2,
                    p_descripcion_objeto IN VARCHAR2,
                    p_usuario_creacion IN VARCHAR2,
                    p_fecha_creacion IN DATE,
                    p_ip IN VARCHAR2,
                    p_usuario_modificacion IN VARCHAR2,
                    p_fecha_modificacion IN DATE,
                    v_salida OUT NUMBER
                ) AS
                BEGIN
                    UPDATE objetos
                    SET 
                        nombre_objeto = p_nombre_objeto,
                        descripcion_objeto = p_descripcion_objeto,
                        usuario_creacion = p_usuario_creacion,
                        fecha_creacion = p_fecha_creacion,
                        ip = p_ip,
                        usuario_modificacion = p_usuario_modificacion,
                        fecha_modificacion = p_fecha_modificacion
                    WHERE id_objeto = p_id_objeto
                    RETURNING id_objeto INTO v_salida;
                END;
                """,

                # PROCEDIMIENTO: objetos_PRC_SELECT_ROW
                """
                CREATE OR REPLACE PROCEDURE objetos_PRC_SELECT_ROW (
                    v_id IN NUMBER,
                    cursor_resultado OUT SYS_REFCURSOR
                ) AS
                BEGIN   
                    OPEN cursor_resultado FOR
                        SELECT id_objeto, nombre_objeto, descripcion_objeto, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        FROM objetos
                        WHERE id_objeto = v_id;
                END;
                """,

                # PROCEDIMIENTO: entrevistas_PRC_INSERT
                """
                CREATE OR REPLACE PROCEDURE entrevistas_PRC_INSERT (
                    p_tema IN VARCHAR2,
                    p_duracion_minutos IN NUMBER,
                    p_usuario_creacion IN VARCHAR2,
                    p_fecha_creacion IN DATE,
                    p_ip IN VARCHAR2,
                    p_usuario_modificacion IN VARCHAR2,
                    p_fecha_modificacion IN DATE,
                    v_salida OUT NUMBER
                ) AS
                BEGIN
                    INSERT INTO entrevistas (
                        tema, duracion_minutos, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                    ) VALUES (
                        p_tema, p_duracion_minutos, p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                    )
                    RETURNING id_entrevista INTO v_salida;
                END;
                """,

                # PROCEDIMIENTO: entrevistas_PRC_UPDATE
                """
                CREATE OR REPLACE PROCEDURE entrevistas_PRC_UPDATE (
                    p_id_entrevista IN NUMBER,
                    p_tema IN VARCHAR2,
                    p_duracion_minutos IN NUMBER,
                    p_usuario_creacion IN VARCHAR2,
                    p_fecha_creacion IN DATE,
                    p_ip IN VARCHAR2,
                    p_usuario_modificacion IN VARCHAR2,
                    p_fecha_modificacion IN DATE,
                    v_salida OUT NUMBER
                ) AS
                BEGIN
                    UPDATE entrevistas
                    SET 
                        tema = p_tema,
                        duracion_minutos = p_duracion_minutos,
                        usuario_creacion = p_usuario_creacion,
                        fecha_creacion = p_fecha_creacion,
                        ip = p_ip,
                        usuario_modificacion = p_usuario_modificacion,
                        fecha_modificacion = p_fecha_modificacion
                    WHERE id_entrevista = p_id_entrevista
                    RETURNING id_entrevista INTO v_salida;
                END;
                """,

                # PROCEDIMIENTO: entrevistas_PRC_SELECT_ROW
                """
                CREATE OR REPLACE PROCEDURE entrevistas_PRC_SELECT_ROW (
                    v_id IN NUMBER,
                    cursor_resultado OUT SYS_REFCURSOR
                ) AS
                BEGIN   
                    OPEN cursor_resultado FOR
                        SELECT id_entrevista, tema, duracion_minutos, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        FROM entrevistas
                        WHERE id_entrevista = v_id;
                END;
                """,

                # PROCEDIMIENTO: objeto_entrevista_rel_PRC_INSERT
                """
                CREATE OR REPLACE PROCEDURE objeto_entrevista_rel_PRC_INSERT (
                    p_id_objeto IN NUMBER,
                    p_id_entrevista IN NUMBER,
                    p_fecha_entrevista IN DATE,
                    p_usuario_creacion IN VARCHAR2,
                    p_fecha_creacion IN DATE,
                    p_ip IN VARCHAR2,
                    p_usuario_modificacion IN VARCHAR2,
                    p_fecha_modificacion IN DATE,
                    v_salida OUT NUMBER
                ) AS
                BEGIN
                    INSERT INTO objeto_entrevista_rel (
                        id_objeto, id_entrevista, fecha_entrevista, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                    ) 
                    VALUES (
                        p_id_objeto, p_id_entrevista, p_fecha_entrevista, p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                    )
                    RETURNING id_relacional INTO v_salida;
                END;
                """,

                # PROCEDIMIENTO: objeto_entrevista_rel_PRC_UPDATE
                """
                CREATE OR REPLACE PROCEDURE objeto_entrevista_rel_PRC_UPDATE (
                    p_id_relacional IN NUMBER,
                    p_id_objeto IN NUMBER,
                    p_id_entrevista IN NUMBER,
                    p_fecha_entrevista IN DATE,
                    p_usuario_creacion IN VARCHAR2,
                    p_fecha_creacion IN DATE,
                    p_ip IN VARCHAR2,
                    p_usuario_modificacion IN VARCHAR2,
                    p_fecha_modificacion IN DATE,
                    v_salida OUT NUMBER
                ) AS
                BEGIN
                    UPDATE objeto_entrevista_rel
                    SET 
                        id_objeto = p_id_objeto,
                        id_entrevista = p_id_entrevista,
                        fecha_entrevista = p_fecha_entrevista,
                        usuario_creacion = p_usuario_creacion,
                        fecha_creacion = p_fecha_creacion,
                        ip = p_ip,
                        usuario_modificacion = p_usuario_modificacion,
                        fecha_modificacion = p_fecha_modificacion
                    WHERE id_relacional = p_id_relacional
                    RETURNING id_relacional INTO v_salida;
                END;
                """,

                # PROCEDIMIENTO: objeto_entrevista_rel_PRC_SELECT_ROW
                """
                CREATE OR REPLACE PROCEDURE objeto_entrevista_rel_PRC_SELECT_ROW (
                    v_id IN NUMBER,
                    cursor_resultado OUT SYS_REFCURSOR
                ) AS
                BEGIN   
                    OPEN cursor_resultado FOR
                        SELECT id_objeto, id_entrevista, fecha_entrevista, usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        FROM objeto_entrevista_rel
                        WHERE id_relacional = v_id;
                END;
                """
            ]

            data_inserts = [
                # Insert en la tabla 'objetos'
                "BEGIN objetos_PRC_INSERT('Lámpara', 'Lámpara de mesa antigua', 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objetos_PRC_INSERT('Silla', 'Silla de madera con respaldo alto', 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objetos_PRC_INSERT('Espejo', 'Espejo grande con marco dorado', 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",

                # Insert en la tabla 'entrevistas'
                "BEGIN entrevistas_PRC_INSERT('Entrevista sobre Tecnología', 60, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN entrevistas_PRC_INSERT('Entrevista sobre Historia', 90, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN entrevistas_PRC_INSERT('Entrevista sobre Arte', 75, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",

                # Insert en la tabla 'objeto_entrevista_rel'
                "BEGIN objeto_entrevista_rel_PRC_INSERT(1, 1, SYSDATE, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objeto_entrevista_rel_PRC_INSERT(2, 2, SYSDATE, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objeto_entrevista_rel_PRC_INSERT(3, 3, SYSDATE, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objeto_entrevista_rel_PRC_INSERT(1, 2, SYSDATE, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objeto_entrevista_rel_PRC_INSERT(2, 3, SYSDATE, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;",
                "BEGIN objeto_entrevista_rel_PRC_INSERT(3, 1, SYSDATE, 'admin', SYSDATE, '192.168.1.1', 'admin', SYSDATE, :v_salida); END;"
            ]
            
            # Ejecutar los comandos DROP
            for drop in drop_commands:
                try:
                    cursor.execute(drop)
                    print(f"Dropped: Ejecutado correctamente")
                except Exception as e:
                    print(f"Dropped: Error al borrar -> {e}")

            # Ejecutar los comandos CREATE
            for create in create_commands:
                try:
                    cursor.execute(create)
                    print(f"Create: Ejecutado correctamente")
                except Exception as e:
                    print(f"Create: Error al Crear -> {e}")

            # Ejecutar los comandos PRC
            for prc in procedures_commands:
                try:
                    cursor.execute(prc)
                    print(f"PRC: Ejecutado correctamente")
                except Exception as e:
                    print(f"PRC: Error en el PRC -> {e}")
            
            # Ejecutar los comandos INSERT
            for ins in data_inserts:
                try:
                    v_salida = cursor.var(int)  # Crear una variable de salida para recibir el ID generado
                    cursor.execute(ins, v_salida=v_salida)
                    print(f"INSERT: Ejecutado correctamente")
                except Exception as e:
                    print(f"INSERT: Error en el insert -> {e}")
           
            connection.commit()
            print(f"\033[92minitalBDGeneratorConfigPrueba: Proceso TERMINADO exitosamente\033[0m")
        except Exception as e:
            if connection:
                connection.rollback()
            raise Exception(f"iniciaDataBase: Error -> {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()