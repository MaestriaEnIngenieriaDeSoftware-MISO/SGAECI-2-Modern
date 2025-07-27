from comprobantespagos.seedwork.aplicacion.queries import Query, QueryResultado
from .base import ConsultarAfiliacionBaseHandler
from dataclasses import dataclass
from comprobantespagos.seedwork.aplicacion.queries import ejecutar_query as query
import requests
import os

"""
from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
import uuid
"""

AFILIACIONES_URL = os.environ.get('AFILIACIONES_URL', default="")
AFILIACIONES_URL_ENDPOINT = AFILIACIONES_URL + "/afiliaciones/"

@dataclass
class ConsultarAfiliacion(Query):
    id: str

class ConsultarAfiliacionHandler(ConsultarAfiliacionBaseHandler):
    def handle(self, query: ConsultarAfiliacion) -> QueryResultado:
        response = requests.get(AFILIACIONES_URL_ENDPOINT + query.id, verify=False)
        response.raise_for_status()
        ## repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        ## reserva =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorReserva())
        ## return QueryResultado(resultado=reserva)

@query.register(ConsultarAfiliacion)
def ejecutar_query_consultar_afiliacion(query: ConsultarAfiliacion):
    handler = ConsultarAfiliacionHandler()
    return handler.handle(query)