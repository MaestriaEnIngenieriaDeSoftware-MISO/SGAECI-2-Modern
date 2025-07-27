from src.queries.base_query import BaseQuery
from src.models.afiliacion import Afiliacion

class ConsultaAfiliacion(BaseQuery):
    def execute(self, afiliacion_id):
        return Afiliacion.query.get(afiliacion_id)
