from Config.oracleConfig import oracleConfig
from Config.bcryptConfig import bcryptConfig
from Clases.usuariosClass import usuariosClass
from Clases.peliculasClass import peliculasClass
from Clases.actoresClass import actoresClass
from Clases.peliculasActoresClass import peliculasActoresClass
from datetime import datetime
import subprocess
import sys

class initalBDGeneratorConfig:    

    lstPip =[
        "fastapi",
        "uvicorn",
        "python-dotenv",
        "pyjwt",
        "oracledb",
        "bcrypt",
        "httpx"
    ]

    lstUsuarios = [
        usuariosClass(rut="10101010", nombre="Clark", apellido="Kent", estado="1", password_hash="", password_plain="hash_superman123", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="20202020", nombre="Bruce", apellido="Wayne", estado="1", password_hash="", password_plain="hash_batman456", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="30303030", nombre="Diana", apellido="Prince", estado="1", password_hash="", password_plain="hash_wonderwoman789", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="40404040", nombre="Barry", apellido="Allen", estado="1", password_hash="", password_plain="hash_flash123", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="50505050", nombre="Hal", apellido="Jordan", estado="1", password_hash="", password_plain="hash_greenlantern456", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="60606060", nombre="Arthur", apellido="Curry", estado="1", password_hash="", password_plain="hash_aquaman789", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="70707070", nombre="Peter", apellido="Parker", estado="1", password_hash="", password_plain="hash_spiderman123", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="80808080", nombre="Tony", apellido="Stark", estado="1", password_hash="", password_plain="hash_ironman456", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="90909090", nombre="Steve", apellido="Rogers", estado="1", password_hash="", password_plain="hash_captainamerica789", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        usuariosClass(rut="10111213", nombre="Natasha", apellido="Romanoff", estado="1", password_hash="", password_plain="hash_blackwidow123", usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now())
    ]

    lstPeliculas = [
        peliculasClass(titulo='The Exorcist', anio_estreno=1973, duracion=122, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='A Nightmare on Elm Street', anio_estreno=1984, duracion=91, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='The Shining', anio_estreno=1980, duracion=146, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='Halloween', anio_estreno=1978, duracion=91, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='It Follows', anio_estreno=2014, duracion=100, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='Hereditary', anio_estreno=2018, duracion=127, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='The Babadook', anio_estreno=2014, duracion=94, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='The Texas Chain Saw Massacre', anio_estreno=1974, duracion=83, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='Get Out', anio_estreno=2017, duracion=104, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='Us', anio_estreno=2019, duracion=116, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='It', anio_estreno=2017, duracion=135, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='The Conjuring', anio_estreno=2013, duracion=112, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='Annabelle', anio_estreno=2014, duracion=99, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='Insidious', anio_estreno=2010, duracion=103, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasClass(titulo='The Ring', anio_estreno=2002, duracion=115, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
    ]

    lstActores = [
        actoresClass(nombre='Linda Blair', fecha_nacimiento=datetime(1959,1,22), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Robert Englund', fecha_nacimiento=datetime(1947,6,6), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Jack Nicholson', fecha_nacimiento=datetime(1937,4,22), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Jamie Lee Curtis', fecha_nacimiento=datetime(1958,11,22), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Maika Monroe', fecha_nacimiento=datetime(1993,5,29), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Toni Collette', fecha_nacimiento=datetime(1972,11,1), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Essie Davis', fecha_nacimiento=datetime(1970,1,19), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Marilyn Burns', fecha_nacimiento=datetime(1949,5,7), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Daniel Kaluuya', fecha_nacimiento=datetime(1989,2,24), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Lupita Nyong\'o', fecha_nacimiento=datetime(1983,3,1), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Bill Skarsgård', fecha_nacimiento=datetime(1990,8,9),usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Patrick Wilson', fecha_nacimiento=datetime(1973,7,3), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Vera Farmiga', fecha_nacimiento=datetime(1973,8,6), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Annabelle Wallis', fecha_nacimiento=datetime(1984,9,25), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Lin Shaye', fecha_nacimiento=datetime(1943,10,12), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Naomi Watts', fecha_nacimiento=datetime(1968,9,28), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='James Wan', fecha_nacimiento=datetime(1977,2,26), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        actoresClass(nombre='Alexandra Daddario', fecha_nacimiento=datetime(1986,3,16), usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now())
    ]   
    
    lstActoresPeliculas = [
        # "The Exorcist" (Linda Blair y James Wan como cameo)
        peliculasActoresClass(1, 1, 500000, datetime(1972, 1, 1), datetime(1972, 12, 31), 50, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(1, 17, 200000, datetime(1972, 1, 1), datetime(1972, 12, 31), 10, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "A Nightmare on Elm Street" (Robert Englund y Lin Shaye)
        peliculasActoresClass(2, 2, 400000, datetime(1983, 5, 1), datetime(1983, 10, 31), 45, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(2, 15, 250000, datetime(1983, 5, 1), datetime(1983, 10, 31), 20, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "The Shining" (Jack Nicholson y Alexandra Daddario como personaje secundario)
        peliculasActoresClass(3, 3, 700000, datetime(1979, 1, 1), datetime(1979, 12, 31), 60, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(3, 18, 300000, datetime(1979, 1, 1), datetime(1979, 12, 31), 15, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "Halloween" (Jamie Lee Curtis y Patrick Wilson)
        peliculasActoresClass(4, 4, 300000, datetime(1977, 3, 1), datetime(1977, 8, 31), 30, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(4, 12, 400000, datetime(1977, 3, 1), datetime(1977, 8, 31), 25, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "It Follows" (Maika Monroe y Vera Farmiga como personaje secundario)
        peliculasActoresClass(5, 5, 350000, datetime(2013, 2, 1), datetime(2013, 8, 31), 25, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(5, 13, 300000, datetime(2013, 2, 1), datetime(2013, 8, 31), 10, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "Hereditary" (Toni Collette, Essie Davis y Lupita Nyong'o)
        peliculasActoresClass(6, 6, 600000, datetime(2017, 1, 1), datetime(2017, 12, 31), 40, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(6, 7, 450000, datetime(2017, 1, 1), datetime(2017, 12, 31), 35, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(6, 10, 500000, datetime(2017, 1, 1), datetime(2017, 12, 31), 20, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "The Babadook" (Essie Davis y Naomi Watts)
        peliculasActoresClass(7, 7, 450000, datetime(2013, 3, 1), datetime(2013, 10, 31), 35, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(7, 16, 400000, datetime(2013, 3, 1), datetime(2013, 10, 31), 15, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "The Texas Chain Saw Massacre" (Marilyn Burns y Lin Shaye como personaje secundario)
        peliculasActoresClass(8, 8, 250000, datetime(1973, 4, 1), datetime(1973, 9, 30), 20, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(8, 15, 200000, datetime(1973, 4, 1), datetime(1973, 9, 30), 10, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "Get Out" (Daniel Kaluuya y Lupita Nyong'o)
        peliculasActoresClass(9, 9, 550000, datetime(2016, 2, 1), datetime(2016, 10, 31), 50, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(9, 10, 600000, datetime(2016, 2, 1), datetime(2016, 10, 31), 45, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "Us" (Lupita Nyong'o y Daniel Kaluuya)
        peliculasActoresClass(10, 10, 600000, datetime(2018, 4, 1), datetime(2018, 12, 31), 55, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(10, 9, 550000, datetime(2018, 4, 1), datetime(2018, 12, 31), 50, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "It" (Bill Skarsgård y Maika Monroe como personaje secundario)
        peliculasActoresClass(11, 11, 700000, datetime(2016, 3, 1), datetime(2016, 10, 31), 40, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(11, 5, 350000, datetime(2016, 3, 1), datetime(2016, 10, 31), 15, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "The Conjuring" (Patrick Wilson y Vera Farmiga)
        peliculasActoresClass(12, 12, 500000, datetime(2012, 5, 1), datetime(2012, 11, 30), 45, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(12, 13, 500000, datetime(2012, 5, 1), datetime(2012, 11, 30), 45, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "Annabelle" (Annabelle Wallis y Alexandra Daddario)
        peliculasActoresClass(13, 14, 350000, datetime(2013, 2, 1), datetime(2013, 8, 31), 30, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(13, 18, 300000, datetime(2013, 2, 1), datetime(2013, 8, 31), 25, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "Insidious" (Lin Shaye, Patrick Wilson y James Wan como cameo)
        peliculasActoresClass(14, 15, 400000, datetime(2009, 4, 1), datetime(2009, 12, 31), 35, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(14, 12, 450000, datetime(2009, 4, 1), datetime(2009, 12, 31), 30, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(14, 17, 200000, datetime(2009, 4, 1), datetime(2009, 12, 31), 5, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),

        # "The Ring" (Naomi Watts y Essie Davis como personaje secundario)
        peliculasActoresClass(15, 16, 450000, datetime(2001, 3, 1), datetime(2001, 11, 30), 40, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
        peliculasActoresClass(15, 7, 350000, datetime(2001, 3, 1), datetime(2001, 11, 30), 20, usuario_creacion="10101010", fecha_creacion=datetime.now(), ip='0.0.0.0', usuario_modificacion="10101010", fecha_modificacion=datetime.now()),
    ]


    @staticmethod
    def instalaDesinstalaPIP():
        try:
            """
            Actualiza PIP y Desinstala e instala paquetes usando pip desde la lista estática lstPip.
            """
            # Actualizar pip
            try:
                print("PIP: Actualizando pip...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
                print("PIP: pip actualizado correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"PIP: Error al actualizar pip: {e}")

            for paquete in initalBDGeneratorConfig.lstPip:
                # Desinstalar paquete
                try:
                    print(f"PIP: Desinstalando paquete: {paquete}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", paquete])
                    print(f"PIP: Paquete desinstalado correctamente: {paquete}")
                except subprocess.CalledProcessError as e:
                    print(f"PIP: Error al desinstalar el paquete {paquete}: {e}")

                # Instalar paquete
                try:
                    print(f"PIP: Instalando paquete: {paquete}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
                    print(f"PIP: Paquete instalado correctamente: {paquete}")
                except subprocess.CalledProcessError as e:
                    print(f"PIP: Error al instalar el paquete {paquete}: {e}")
        except Exception as e:
             raise Exception(f"PIP: Error -> {e}")

    @staticmethod
    def borrarTablaPrcDatos():
        # Lista de usuarios
        connection = None
        try:
            connection = oracleConfig.connect()
            cursor = connection.cursor()

            try:
                sql_query = f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE USUARIOS CASCADE CONSTRAINTS PURGE' ; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;"
                cursor.execute(sql_query)
                print(f"Borrado: Tabla USUARIOS")
            except Exception as e:
                print(f"Borrado: Error al borrar -> {e}")  

            try:
                sql_query = f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE PELICULAS CASCADE CONSTRAINTS PURGE' ; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;"
                cursor.execute(sql_query)
                print(f"Borrado: Tabla PELICULAS")
            except Exception as e:
                print(f"Borrado: Error al borrar -> {e}") 
          
            try:
                sql_query = f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE ACTORES CASCADE CONSTRAINTS PURGE' ; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;"
                cursor.execute(sql_query)
                print(f"Borrado: Tabla ACTORES")
            except Exception as e:
                print(f"Borrado: Error al borrar -> {e}") 
        
            try:
                sql_query = f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE PELICULAS_ACTORES CASCADE CONSTRAINTS PURGE' ; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;"
                cursor.execute(sql_query)
                print(f"Borrado: Tabla PELICULAS_ACTORES")
            except Exception as e:
                print(f"Borrado: Error al borrar -> {e}")

            try:
                sql_query = f'drop procedure USUARIOS_PRC_SELECT_ROW_RUT'
                cursor.execute(sql_query)
                print(f"Borrado: PRC USUARIOS_PRC_SELECT_ROW_RUT")
            except Exception as e:
                print(f"Borrado: Error al borrar -> {e}") 

            try:
                sql_query = f'drop procedure USUARIOS_PRC_SELECT_ROW'
                cursor.execute(sql_query)
                print(f"Borrado: PRC USUARIOS_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Borrado: Error al borrar -> {e}")

            try:
                sql_query = f'DROP PROCEDURE PELICULAS_PRC_SELECT_ROW'
                cursor.execute(sql_query)
                print("Borrado: PRC PELICULAS_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Error al borrar PELICULAS_PRC_SELECT_ROW: {e}")

            try:
                sql_query = f'DROP PROCEDURE PELICULAS_PRC_INSERT'
                cursor.execute(sql_query)
                print("Borrado: PRC PELICULAS_PRC_INSERT")
            except Exception as e:
                print(f"Error al borrar PELICULAS_PRC_INSERT: {e}")

            try:
                sql_query = f'DROP PROCEDURE ACTORES_PRC_SELECT_ROW'
                cursor.execute(sql_query)
                print("Borrado: PRC ACTORES_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Error al borrar ACTORES_PRC_SELECT_ROW: {e}")

            try:
                sql_query = f'DROP PROCEDURE ACTORES_PRC_INSERT'
                cursor.execute(sql_query)
                print("Borrado: PRC ACTORES_PRC_INSERT")
            except Exception as e:
                print(f"Error al borrar ACTORES_PRC_INSERT: {e}")

            try:
                sql_query = f'DROP PROCEDURE PELICULAS_ACTORES_PRC_SELECT_ROW'
                cursor.execute(sql_query)
                print("Borrado: PRC PELICULAS_ACTORES_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Error al borrar PELICULAS_ACTORES_PRC_SELECT_ROW: {e}")

            try:
                sql_query = f'DROP PROCEDURE PELICULAS_ACTORES_PRC_INSERT'
                cursor.execute(sql_query)
                print("Borrado: PRC PELICULAS_ACTORES_PRC_INSERT")
            except Exception as e:
                print(f"Error al borrar PELICULAS_ACTORES_PRC_INSERT: {e}")

            connection.commit()
        except Exception as e:
            if connection:
                connection.rollback()
            raise Exception(f"Borrado: Error -> {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def crearTablaPRC():
        # Lista de usuarios
        connection = None
        try:
            connection = oracleConfig.connect()           
            cursor = connection.cursor()

            try:
                sql_query = f'''
                    CREATE TABLE usuarios (
                        id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
                        rut NUMBER UNIQUE NOT NULL,
                        nombre VARCHAR2(100) NOT NULL,
                        apellido VARCHAR2(100) NOT NULL,
                        estado NUMBER(1) DEFAULT 1 NOT NULL,
                        password_hash VARCHAR2(255) NOT NULL,
                        password_plain VARCHAR2(100) NOT NULL,
                        usuario_creacion NUMBER NOT NULL,
                        fecha_creacion DATE NOT NULL,
                        ip VARCHAR2(45) NOT NULL,
                        usuario_modificacion NUMBER NOT NULL,
                        fecha_modificacion DATE NOT NULL
                    )
                '''
                cursor.execute(sql_query)
                print(f"Creación: Tabla usuarios")
            except Exception as e:
                print(f"Creación: Error al crear TABLE usuarios -> {e}") 

            try:
                sql_query = f'''
                    CREATE TABLE peliculas (
                        id_pelicula NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        titulo VARCHAR(255) NOT NULL,
                        anio_estreno NUMBER NOT NULL,
                        duracion NUMBER NOT NULL,
                        usuario_creacion NUMBER NOT NULL,
                        fecha_creacion DATE NOT NULL,
                        ip VARCHAR2(45) NOT NULL,
                        usuario_modificacion NUMBER NOT NULL,
                        fecha_modificacion DATE NOT NULL
                    )
                '''
                cursor.execute(sql_query)
                print(f"Creación: Tabla peliculas")
            except Exception as e:
                print(f"Creación: Error al crear TABLE peliculas -> {e}")

            try:
                sql_query = f'''
                    CREATE TABLE actores (
                        id_actor NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        nombre VARCHAR(255) NOT NULL,
                        fecha_nacimiento DATE NOT NULL,
                        usuario_creacion NUMBER NOT NULL,
                        fecha_creacion DATE NOT NULL,
                        ip VARCHAR2(45) NOT NULL,
                        usuario_modificacion NUMBER NOT NULL,
                        fecha_modificacion DATE NOT NULL
                    )
                '''
                cursor.execute(sql_query)
                print(f"Creación: Tabla actores")
            except Exception as e:
                print(f"Creación: Error al crear TABLE actores -> {e}")

            try:
                sql_query = f'''
                    CREATE TABLE peliculas_actores (
                        id_pelicula_actor NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        id_pelicula NUMBER NOT NULL,
                        id_actor NUMBER NOT NULL,
                        sueldo NUMBER(15, 0),
                        fecha_inicio_grabacion DATE,
                        fecha_fin_grabacion DATE,
                        escenas_participadas NUMBER,
                        usuario_creacion NUMBER NOT NULL,
                        fecha_creacion DATE NOT NULL,
                        ip VARCHAR2(45) NOT NULL,
                        usuario_modificacion NUMBER NOT NULL,
                        fecha_modificacion DATE NOT NULL,
                        CONSTRAINT fk_pelicula FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula),
                        CONSTRAINT fk_actor FOREIGN KEY (id_actor) REFERENCES actores(id_actor)
                    )
                '''
                cursor.execute(sql_query)
                print(f"Creación: Tabla peliculas_actores")
            except Exception as e:
                print(f"Creación: Error al crear TABLE peliculas_actores -> {e}")

            try:
                sql_query = f"""
                    create or replace PROCEDURE USUARIOS_PRC_SELECT_ROW (
                        v_id IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN   
                        OPEN cursor_resultado FOR
                            SELECT id, rut, nombre, apellido, estado, password_hash, password_plain,
                                usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                            FROM usuarios
                            WHERE id = v_id;
                    END;
                """
                cursor.execute(sql_query)
                print(f"Creación: PRC USUARIOS_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Creación: Error al crear USUARIOS_PRC_SELECT_ROW -> {e}")


            try:
                sql_query = f"""
                    create or replace PROCEDURE USUARIOS_PRC_SELECT_ROW_RUT (
                        v_rut IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN   
                        OPEN cursor_resultado FOR
                            SELECT id, rut, nombre, apellido, estado, password_hash, password_plain,
                                usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                            FROM usuarios
                            WHERE rut = v_rut;
                    END;
                """
                cursor.execute(sql_query)
                print(f"Creación: PRC USUARIOS_PRC_SELECT_ROW_RUT")
            except Exception as e:
                print(f"Creación: Error al Crear USUARIOS_PRC_SELECT_ROW_RUT -> {e}")

            try:
                sql_query = f"""
                    CREATE OR REPLACE PROCEDURE USUARIOS_PRC_INSERT(
                        p_rut               NUMBER,
                        p_nombre            VARCHAR2,
                        p_apellido          VARCHAR2,
                        p_estado            NUMBER DEFAULT 1,
                        p_password_hash     VARCHAR2,
                        p_password_plain    VARCHAR2,
                        p_usuario_creacion  NUMBER,
                        p_fecha_creacion    DATE,
                        p_ip                VARCHAR2,
                        p_usuario_modificacion NUMBER,
                        p_fecha_modificacion DATE,
                        v_salida            OUT NUMBER
                    ) IS
                    BEGIN
                        INSERT INTO usuarios (
                            rut, nombre, apellido, estado, password_hash, password_plain,
                            usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        ) VALUES (
                            p_rut, p_nombre, p_apellido, p_estado, p_password_hash, p_password_plain,
                            p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                        )
                        RETURNING id INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print(f"Creación: PRC USUARIOS_PRC_INSERT")
            except Exception as e:
                print(f"Creación: Error al Crear USUARIOS_PRC_INSERT -> {e}")

            try:
                sql_query = f"""
                    CREATE OR REPLACE PROCEDURE USUARIOS_PRC_UPDATE(
                        p_id                    NUMBER,
                        p_rut                   NUMBER,
                        p_nombre                VARCHAR2,
                        p_apellido              VARCHAR2,
                        p_estado                NUMBER DEFAULT 1,
                        p_password_hash         VARCHAR2,
                        p_password_plain        VARCHAR2,
                        p_usuario_creacion      NUMBER,
                        p_fecha_creacion        DATE,
                        p_ip                    VARCHAR2,
                        p_usuario_modificacion  NUMBER,
                        p_fecha_modificacion    DATE,
                        v_salida                OUT NUMBER
                    ) IS
                    BEGIN
                        UPDATE usuarios
                        SET 
                            rut = p_rut,
                            nombre = p_nombre,
                            apellido = p_apellido,
                            estado = p_estado,
                            password_hash = p_password_hash,
                            password_plain = p_password_plain,
                            usuario_creacion = p_usuario_creacion,
                            fecha_creacion = p_fecha_creacion,
                            ip = p_ip,
                            usuario_modificacion = p_usuario_modificacion,
                            fecha_modificacion = p_fecha_modificacion
                        WHERE id = p_id
                        RETURNING id INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print(f"Actualización: PRC USUARIOS_PRC_UPDATE")
            except Exception as e:
                print(f"Actualización: Error al Crear USUARIOS_PRC_UPDATE -> {e}")

            
            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE PELICULAS_PRC_SELECT_ROW(
                        v_id IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN
                        OPEN cursor_resultado FOR
                            SELECT id_pelicula, titulo, anio_estreno, duracion,
                                usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                            FROM peliculas
                            WHERE id_pelicula = v_id;
                    END;
                """
                cursor.execute(sql_query)
                print("Creación: PRC PELICULAS_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Creación: Error al Crear PELICULAS_PRC_SELECT_ROW -> {e}")


            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE ACTORES_PRC_SELECT_ROW(
                        v_id IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN
                        OPEN cursor_resultado FOR
                            SELECT id_actor, nombre, fecha_nacimiento,
                                usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                            FROM actores
                            WHERE id_actor = v_id;
                    END;
                """
                cursor.execute(sql_query)
                print("Creación: PRC ACTORES_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Creación: Error al Crear ACTORES_PRC_SELECT_ROW -> {e}")

            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE PELICULAS_ACTORES_PRC_SELECT_ROW(
                        v_id IN NUMBER,
                        cursor_resultado OUT SYS_REFCURSOR
                    ) AS
                    BEGIN
                        OPEN cursor_resultado FOR
                            SELECT id_pelicula_actor, id_pelicula, id_actor, sueldo, fecha_inicio_grabacion, 
                                fecha_fin_grabacion, escenas_participadas,
                                usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                            FROM peliculas_actores
                            WHERE id_pelicula_actor = v_id;
                    END;
                """
                cursor.execute(sql_query)
                print("Creación: PRC PELICULAS_ACTORES_PRC_SELECT_ROW")
            except Exception as e:
                print(f"Creación: Error al Crear PELICULAS_ACTORES_PRC_SELECT_ROW -> {e}")

            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE PELICULAS_PRC_INSERT(
                        p_titulo                VARCHAR2,
                        p_anio_estreno          NUMBER,
                        p_duracion              NUMBER,
                        p_usuario_creacion      NUMBER,
                        p_fecha_creacion        DATE,
                        p_ip                    VARCHAR2,
                        p_usuario_modificacion  NUMBER,
                        p_fecha_modificacion    DATE,
                        v_salida                OUT NUMBER
                    ) IS
                    BEGIN
                        INSERT INTO peliculas (
                            titulo, anio_estreno, duracion,
                            usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        ) VALUES (
                            p_titulo, p_anio_estreno, p_duracion,
                            p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                        )
                        RETURNING id_pelicula INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print("Creación: PRC PELICULAS_PRC_INSERT")
            except Exception as e:
                print(f"Creación: Error al Crear PELICULAS_PRC_INSERT -> {e}")

            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE PELICULAS_PRC_UPDATE(
                        p_id_pelicula           NUMBER,
                        p_titulo                VARCHAR2,
                        p_anio_estreno          NUMBER,
                        p_duracion              NUMBER,
                        p_usuario_creacion      NUMBER,
                        p_fecha_creacion        DATE,
                        p_ip                    VARCHAR2,
                        p_usuario_modificacion  NUMBER,
                        p_fecha_modificacion    DATE,
                        v_salida                OUT NUMBER
                    ) IS
                    BEGIN
                        UPDATE peliculas
                        SET 
                            titulo = p_titulo,
                            anio_estreno = p_anio_estreno,
                            duracion = p_duracion,
                            usuario_creacion = p_usuario_creacion,
                            fecha_creacion = p_fecha_creacion,
                            ip = p_ip,
                            usuario_modificacion = p_usuario_modificacion,
                            fecha_modificacion = p_fecha_modificacion
                        WHERE id_pelicula = p_id_pelicula
                        RETURNING id_pelicula INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print("Actualización: PRC PELICULAS_PRC_UPDATE")
            except Exception as e:
                print(f"Actualización: Error al Crear PELICULAS_PRC_UPDATE -> {e}")


            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE ACTORES_PRC_INSERT(
                        p_nombre                VARCHAR2,
                        p_fecha_nacimiento      DATE,
                        p_usuario_creacion      NUMBER,
                        p_fecha_creacion        DATE,
                        p_ip                    VARCHAR2,
                        p_usuario_modificacion  NUMBER,
                        p_fecha_modificacion    DATE,
                        v_salida                OUT NUMBER
                    ) IS
                    BEGIN
                        INSERT INTO actores (
                            nombre, fecha_nacimiento,
                            usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        ) VALUES (
                            p_nombre, p_fecha_nacimiento,
                            p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                        )
                        RETURNING id_actor INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print("Creación: PRC ACTORES_PRC_INSERT")
            except Exception as e:
                print(f"Creación: Error al Crear ACTORES_PRC_INSERT -> {e}")

            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE ACTORES_PRC_UPDATE(
                        p_id_actor              NUMBER,
                        p_nombre                VARCHAR2,
                        p_fecha_nacimiento      DATE,
                        p_usuario_creacion      NUMBER,
                        p_fecha_creacion        DATE,
                        p_ip                    VARCHAR2,
                        p_usuario_modificacion  NUMBER,
                        p_fecha_modificacion    DATE,
                        v_salida                OUT NUMBER
                    ) IS
                    BEGIN
                        UPDATE actores
                        SET 
                            nombre = p_nombre,
                            fecha_nacimiento = p_fecha_nacimiento,
                            usuario_creacion = p_usuario_creacion,
                            fecha_creacion = p_fecha_creacion,
                            ip = p_ip,
                            usuario_modificacion = p_usuario_modificacion,
                            fecha_modificacion = p_fecha_modificacion
                        WHERE id_actor = p_id_actor
                        RETURNING id_actor INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print("Actualización: PRC ACTORES_PRC_UPDATE")
            except Exception as e:
                print(f"Actualización: Error al Crear ACTORES_PRC_UPDATE -> {e}")


            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE PELICULAS_ACTORES_PRC_INSERT(
                        p_id_pelicula            NUMBER,
                        p_id_actor               NUMBER,
                        p_sueldo                 NUMBER,
                        p_fecha_inicio_grabacion DATE,
                        p_fecha_fin_grabacion    DATE,
                        p_escenas_participadas   NUMBER,
                        p_usuario_creacion       NUMBER,
                        p_fecha_creacion         DATE,
                        p_ip                     VARCHAR2,
                        p_usuario_modificacion   NUMBER,
                        p_fecha_modificacion     DATE,
                        v_salida                 OUT NUMBER
                    ) IS
                    BEGIN
                        INSERT INTO peliculas_actores (
                            id_pelicula, id_actor, sueldo, fecha_inicio_grabacion, 
                            fecha_fin_grabacion, escenas_participadas, 
                            usuario_creacion, fecha_creacion, ip, usuario_modificacion, fecha_modificacion
                        ) VALUES (
                            p_id_pelicula, p_id_actor, p_sueldo, p_fecha_inicio_grabacion, 
                            p_fecha_fin_grabacion, p_escenas_participadas, 
                            p_usuario_creacion, p_fecha_creacion, p_ip, p_usuario_modificacion, p_fecha_modificacion
                        )
                        RETURNING id_pelicula_actor INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print("Creación: PRC PELICULAS_ACTORES_PRC_INSERT")
            except Exception as e:
                print(f"Creación: Error al Crear PELICULAS_ACTORES_PRC_INSERT -> {e}")

            try:
                sql_query = """
                    CREATE OR REPLACE PROCEDURE PELICULAS_ACTORES_PRC_UPDATE(
                        p_id_pelicula_actor      NUMBER,
                        p_id_pelicula            NUMBER,
                        p_id_actor               NUMBER,
                        p_sueldo                 NUMBER,
                        p_fecha_inicio_grabacion DATE,
                        p_fecha_fin_grabacion    DATE,
                        p_escenas_participadas   NUMBER,
                        p_usuario_creacion       NUMBER,
                        p_fecha_creacion         DATE,
                        p_ip                     VARCHAR2,
                        p_usuario_modificacion   NUMBER,
                        p_fecha_modificacion     DATE,
                        v_salida                 OUT NUMBER
                    ) IS
                    BEGIN
                        UPDATE peliculas_actores
                        SET 
                            id_pelicula = p_id_pelicula,
                            id_actor = p_id_actor,
                            sueldo = p_sueldo,
                            fecha_inicio_grabacion = p_fecha_inicio_grabacion,
                            fecha_fin_grabacion = p_fecha_fin_grabacion,
                            escenas_participadas = p_escenas_participadas,
                            usuario_creacion = p_usuario_creacion,
                            fecha_creacion = p_fecha_creacion,
                            ip = p_ip,
                            usuario_modificacion = p_usuario_modificacion,
                            fecha_modificacion = p_fecha_modificacion
                        WHERE id_pelicula_actor = p_id_pelicula_actor
                        RETURNING id_pelicula_actor INTO v_salida;
                    END;
                """
                cursor.execute(sql_query)
                print("Actualización: PRC PELICULAS_ACTORES_PRC_UPDATE")
            except Exception as e:
                print(f"Actualización: Error al Crear PELICULAS_ACTORES_PRC_UPDATE -> {e}")



            connection.commit()
        except Exception as e:
            if connection:
                connection.rollback()
            raise Exception(f"Creación: Error -> {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def insertarDatos():
        connection = None
        try: 
            connection = oracleConfig.connect()
            try:
                for usuario in initalBDGeneratorConfig.lstUsuarios:         
                    cursor = connection.cursor()                  
                    usuario.password_hash = bcryptConfig.hash_password(usuario.password_plain)
                    v_salida = cursor.var(int)  # Variable de salida para el ID generado o actualizado
                    cursor.callproc(
                        "USUARIOS_PRC_INSERT",
                        [usuario.rut, usuario.nombre, usuario.apellido, usuario.estado, usuario.password_hash, usuario.password_plain, usuario.usuario_creacion, usuario.fecha_creacion, usuario.ip, usuario.usuario_modificacion, usuario.fecha_modificacion, v_salida]
                    )
                    usuario.id = v_salida.getvalue()
                    print(f"Insert: Tabla USUARIOS: Nombre: {usuario.nombre} - Apellido: {usuario.apellido}.")                
            except Exception as e:
                print(f"Insert: Error Tabla USUARIOS -> {e}")

            try:
                for pelicula in initalBDGeneratorConfig.lstPeliculas:         
                    cursor = connection.cursor()                  
                    v_salida = cursor.var(int)  # Variable de salida para el ID generado o actualizado
                    cursor.callproc(
                        "PELICULAS_PRC_INSERT",
                        [pelicula.titulo, pelicula.anio_estreno, pelicula.duracion, pelicula.usuario_creacion, pelicula.fecha_creacion, pelicula.ip, pelicula.usuario_modificacion, pelicula.fecha_modificacion, v_salida]
                    )
                    pelicula.id = v_salida.getvalue()
                    print(f"Insert: Tabla PELICULAS: Titulo: {pelicula.titulo}.")              
            except Exception as e:
                print(f"Insert: Error Tabla PELICULAS -> {e}")

            try:
                for actor in initalBDGeneratorConfig.lstActores:         
                    cursor = connection.cursor()                  
                    v_salida = cursor.var(int)  # Variable de salida para el ID generado o actualizado
                    cursor.callproc(
                        "ACTORES_PRC_INSERT",
                        [
                            actor.nombre,
                            actor.fecha_nacimiento,
                            actor.usuario_creacion,
                            actor.fecha_creacion,
                            actor.ip,
                            actor.usuario_modificacion,
                            actor.fecha_modificacion,
                            v_salida
                        ]
                    )
                    actor.id = v_salida.getvalue()
                    print(f"Insert: Tabla ACTORES: Nombre: {actor.nombre}.")
            except Exception as e:
                print(f"Insert: Error Tabla ACTORES -> {e}")

            try:
                for relacion in initalBDGeneratorConfig.lstActoresPeliculas:
                    cursor = connection.cursor()
                    v_salida = cursor.var(int)  # Variable de salida para el ID generado
                    cursor.callproc(
                        "PELICULAS_ACTORES_PRC_INSERT",
                        [
                            relacion.id_pelicula, 
                            relacion.id_actor,
                            relacion.sueldo,
                            relacion.fecha_inicio_grabacion,
                            relacion.fecha_fin_grabacion,
                            relacion.escenas_participadas,
                            relacion.usuario_creacion, relacion.fecha_creacion, relacion.ip, relacion.usuario_modificacion, relacion.fecha_modificacion, 
                            v_salida
                        ]
                    )
                    relacion.id = v_salida.getvalue()
                    print(f"Insert: Tabla PELICULAS_ACTORES: id {relacion.id}")
            except Exception as e:
                print(f"Insert: Error Tabla PELICULAS_ACTORES -> {e}")

            connection.commit()
        except Exception as e:
            if connection:
                connection.rollback()
            raise Exception(f"Insert: Error -> {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()