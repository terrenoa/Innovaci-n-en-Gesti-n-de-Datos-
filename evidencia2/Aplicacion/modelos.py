# Archivo: modelos.py

class Usuario:
    def __init__(self, user_id, username, password, email):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email
    
    # Getters y Setters
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

class Acceso:
    def __init__(self, acceso_id, fechaIngreso, usuarioLogueado, fechaSalida=None):
        self._acceso_id = acceso_id
        self._fechaIngreso = fechaIngreso
        self._fechaSalida = fechaSalida
        self._usuarioLogueado = usuarioLogueado
    
    # Getters y Setters
    @property
    def acceso_id(self):
        return self._acceso_id

    @acceso_id.setter
    def acceso_id(self, value):
        self._acceso_id = value

    @property
    def fechaIngreso(self):
        return self._fechaIngreso

    @fechaIngreso.setter
    def fechaIngreso(self, value):
        self._fechaIngreso = value

    @property
    def fechaSalida(self):
        return self._fechaSalida

    @fechaSalida.setter
    def fechaSalida(self, value):
        self._fechaSalida = value

    @property
    def usuarioLogueado(self):
        return self._usuarioLogueado

    @usuarioLogueado.setter
    def usuarioLogueado(self, value):
        self._usuarioLogueado = value
