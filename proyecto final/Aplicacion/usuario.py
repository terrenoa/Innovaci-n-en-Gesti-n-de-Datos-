# usuario.py

class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Usuario(id={self.id}, username='{self.username}', email='{self.email}')"