
from comprobantespagos.seedwork.aplicacion.comandos import Comando, ComandoHandler, ejecutar_commando as comando
from comprobantespagos.aplicacion.dto import PagoAfiliacionDTO
from comprobantespagos.seedwork.dominio.reglas import FechaDePagoEsInalido

class RegistrarComprobante(Comando):
    request: any

class RegistrarComprobanteHandler(ComandoHandler):

    def fromRequestToDTO(self, comando: RegistrarComprobante):
        return PagoAfiliacionDTO().load(comando.request.get_json())

    def handle(self, comando: RegistrarComprobante):
        pagoAfiliacionDTO = self.fromRequestToDTO(comando)
        FechaDePagoEsInalido(pagoAfiliacionDTO).es_valido()

@comando.register(RegistrarComprobante)
def ejecutar_comando_registrar_comprobante(comando: RegistrarComprobante):
    handler = RegistrarComprobanteHandler()
    return handler.handle(comando)

@comando.register(RegistrarComprobante)
def ejecutar_comando_obtener_comprobante(comando: RegistrarComprobante):
    handler = RegistrarComprobanteHandler()
    return handler.fromRequestToDTO(comando)