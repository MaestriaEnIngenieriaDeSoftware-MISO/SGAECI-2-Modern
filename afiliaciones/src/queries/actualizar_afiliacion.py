from src.queries.base_query import BaseQuery
from src.models.afiliacion import Afiliacion
from src import database

class ActualizarAfiliacion(BaseQuery):
    def execute(self, afiliacion_id, data):
        afiliacion = Afiliacion.query.get(afiliacion_id)
        if not afiliacion:
            return None
        if 'estado_solicitud' in data:
            afiliacion.estado_solicitud = data['estado_solicitud']
        if 'comentario' in data:
            afiliacion.comentario = data['comentario']
        if 'estado' in data:
            afiliacion.estado = data['estado']
        database.db.session.commit()
        return afiliacion

