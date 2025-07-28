class ExcepcionDominio(Exception):
    ...

class FechaDePagoDebeEstarEnFuturo(ExcepcionDominio):
    def __init__(self, mensaje = ""):
        self.mensaje = mensaje

    def __str__(self):
        return str(self.mensaje)