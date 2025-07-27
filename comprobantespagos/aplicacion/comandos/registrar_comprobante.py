
from comprobantespagos.seedwork.aplicacion.comandos import Comando, ComandoHandler, ejecutar_commando as comando
from comprobantespagos.aplicacion.dto import PagoAfiliacionDTO

class RegistrarComprobante(Comando):
    request: any

class RegistrarComprobanteHandler(ComandoHandler):
    def handle(self, comando: RegistrarComprobante):
        pagoAfiliacionDTO = PagoAfiliacionDTO().load(comando.request.get_json())
        ...

@comando.register(RegistrarComprobante)
def ejecutar_comando_registrar_comprobante(comando: RegistrarComprobante):
    handler = RegistrarComprobanteHandler()
    handler.handle(comando)