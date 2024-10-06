# utilidades.py

import pickle

def cargar_usuarios():
    try:
        with open('usuarios.ispc', 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return {}

def guardar_usuarios(usuarios):
    with open('usuarios.ispc', 'wb') as f:
        pickle.dump(usuarios, f)

def cargar_accesos():
    try:
        with open('accesos.ispc', 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

def guardar_accesos(acceso):
    accesos = cargar_accesos()
    accesos.append(acceso)

    with open('accesos.ispc', 'wb') as f:
        pickle.dump(accesos, f)
