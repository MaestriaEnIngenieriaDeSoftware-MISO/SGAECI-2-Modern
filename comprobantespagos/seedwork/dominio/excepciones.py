from .reglas import ReglaNegocio

class ExcepcionDominio(Exception):
    ...

class ErrorGeneralExcepcion(ExcepcionDominio):
    def __init__(self, mensaje=''):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)