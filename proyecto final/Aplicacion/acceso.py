class Acceso:
    def __init__(self, id, fecha_ingreso, fecha_salida, usuario_logueado):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.usuario_logueado = usuario_logueado

    def __repr__(self):
        return f"Acceso(id={self.id}, usuario='{self.usuario_logueado}', ingreso='{self.fecha_ingreso}', salida='{self.fecha_salida}')"