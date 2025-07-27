from comprobantespagos.seedwork.aplicacion.comandos import Comando, ComandoHandler, ejecutar_commando as comando
from comprobantespagos.aplicacion.dto import PagoAfiliacionDTO

class ActualizarAfiliacion(Comando):
    request: any

class ActualizarAfiliacionHandler(ComandoHandler):
    def handle(self, comando: ActualizarAfiliacion):
        ...

@comando.register(ActualizarAfiliacion)
def ejecutar_comando_actualizar_afiliacion(comando: ActualizarAfiliacion):
    handler = ActualizarAfiliacionHandler()
    handler.handle(comando)