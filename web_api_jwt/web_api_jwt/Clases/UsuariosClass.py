class UsuariosClass:
    def __init__(self, username, password, password_hash= None, id=None, existe = False):
        self.username = username
        self.password = password
        self.password_hash = password_hash
        self.id = id
        self.existe = existe

    def __str__(self):
        return f"ID: {self.id}, Nombre Usuario: {self.username}, Contraseña Encriptada: {self.password}, Existe: {self.existe}"