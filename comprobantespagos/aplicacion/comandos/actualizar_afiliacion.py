from comprobantespagos.seedwork.aplicacion.comandos import Comando, ComandoHandler, ejecutar_commando as comando
from comprobantespagos.aplicacion.dto import PagoAfiliacionDTO
from comprobantespagos.infraestructura.despachadores import DespachadorRedis

class ActualizarAfiliacion(Comando):
    afiliacion_id: str

class ActualizarAfiliacionHandler(ComandoHandler):
    def handle(self, comando: ActualizarAfiliacion):
        update_data = {
                "estado_solicitud": "en revision",
                "comentario": "Solicitud revisada y aprobada.",
                "estado": "activo"
        }
        despachador = DespachadorRedis()
        despachador.publicar_evento(comando.afiliacion_id, update_data)


@comando.register(ActualizarAfiliacion)
def ejecutar_comando_actualizar_afiliacion(comando: ActualizarAfiliacion):
    handler = ActualizarAfiliacionHandler()
    handler.handle(comando)