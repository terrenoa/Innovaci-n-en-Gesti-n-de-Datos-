# usuario.py
#creo que este es el modulo que hay que eliminar y concentrar todo en el de mododelos.py
class Usuario:
    def __init__(self, id, dni, username, password, email):
        self.id = id
        self.dni = dni
        self.username = username
        self.password = password
        self.email = email

#agregue esta en modelos.py que es la unica diferencia
    def __repr__(self):
        return f"Usuario(id={self.id}, username='{self.username}', email='{self.email}')"