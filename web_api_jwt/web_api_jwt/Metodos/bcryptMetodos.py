import bcrypt

class bcryptMetodos:
    # Hashear la contraseña
    @staticmethod
    def hash_password(password: str) -> str:
        # Hashear la contraseña con una sal aleatoria y devolver el hash como cadena
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    # Verificar la contraseña
    def verify_password(stored_hash: str, password: str) -> bool:
        try:
            print(f"stored_hash: {stored_hash}")
            print(f"password{password}")
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
        except Exception as e:
            print(f"Error al obtener el personaje: {e}")
            raise
        