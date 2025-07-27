from comprobantespagos.seedwork.aplicacion.queries import Query, QueryResultado
from .base import ConsultarAfiliacionBaseHandler
from dataclasses import dataclass
from comprobantespagos.seedwork.aplicacion.queries import ejecutar_query as query

"""
from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
import uuid
"""

@dataclass
class ConsultarAfiliacion(Query):
    id: str

class ConsultarAfiliacionHandler(ConsultarAfiliacionBaseHandler):
    def handle(self, query: ConsultarAfiliacion) -> QueryResultado:
        ...
        ## repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        ## reserva =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorReserva())
        ## return QueryResultado(resultado=reserva)

@query.register(ConsultarAfiliacion)
def ejecutar_query_consultar_afiliacion(query: ConsultarAfiliacion):
    ...
    # handler = ObtenerReservaHandler()
    # return handler.handle(query)