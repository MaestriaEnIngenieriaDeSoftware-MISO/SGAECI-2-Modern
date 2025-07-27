from abc import ABC, abstractmethod
from datetime import datetime
from .excepciones import FechaDePagoDebeEstarEnFuturo
import pytz

utc=pytz.UTC

class ReglaNegocio(ABC):

    __mensaje: str ='La regla de negocio es invalida'

    def __init__(self, mensaje):
        self.__mensaje = mensaje

    def mensaje_error(self) -> str:
        return self.__mensaje

    @abstractmethod
    def es_valido(self) -> bool:
        ...

    def __str__(self):
        return f"{self.__class__.__name__} - {self.__mensaje}"


class FechaDePagoEsInalido(ReglaNegocio):

    entidad: object

    def __init__(self, entidad, mensaje='El pago de la afiliacion no puede realizarse despues del día de hoy'):
        super().__init__(mensaje)
        self.entidad = entidad

    def es_valido(self) -> bool:
        try:
            fecha_pago = self.entidad["fecha_pago"]
            current_date = utc.localize(datetime.now())
            if (fecha_pago > current_date):
                 raise FechaDePagoDebeEstarEnFuturo()
        except AttributeError as error:
            return True
