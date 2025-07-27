
from comprobantespagos.seedwork.aplicacion.comandos import Comando, ComandoHandler, ejecutar_commando as comando
from comprobantespagos.aplicacion.dto import PagoAfiliacionDTO

class RegistrarComprobante(Comando):
    request: any

class RegistrarComprobanteHandler(ComandoHandler):
    def fromRequestToDTO(self, comando: RegistrarComprobante):
        return PagoAfiliacionDTO().load(comando.request.get_json())

    def handle(self, comando: RegistrarComprobante):
        pagoAfiliacionDTO = PagoAfiliacionDTO().load(comando.request.get_json())
        return pagoAfiliacionDTO

@comando.register(RegistrarComprobante)
def ejecutar_comando_registrar_comprobante(comando: RegistrarComprobante):
    handler = RegistrarComprobanteHandler()
    return handler.handle(comando)

@comando.register(RegistrarComprobante)
def ejecutar_comando_obtener_comprobante(comando: RegistrarComprobante):
    handler = RegistrarComprobanteHandler()
    return handler.fromRequestToDTO(comando)