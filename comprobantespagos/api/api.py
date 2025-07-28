from flask import request, jsonify
from flask import (Blueprint, flash) 
from comprobantespagos.aplicacion.comandos.registrar_comprobante import RegistrarComprobante, ejecutar_comando_registrar_comprobante
from comprobantespagos.aplicacion.comandos.actualizar_afiliacion import ActualizarAfiliacion, ejecutar_comando_actualizar_afiliacion
from comprobantespagos.aplicacion.comandos.registrar_comprobante import ejecutar_comando_obtener_comprobante
from comprobantespagos.aplicacion.queries.consultar_afiliacion import ejecutar_query_consultar_afiliacion, ConsultarAfiliacion
from comprobantespagos.dominio.constants import ERROR_GENERAL, ERROR_GENERAL_HTTP, ERROR_AFILIACION_HTTP, VALIDACION_COMPROBANTE_EXITOSA
import requests
from comprobantespagos.seedwork.dominio.excepciones import FechaDePagoDebeEstarEnFuturo

def crear_blueprint(identificador: str, prefijo_url: str):
    return Blueprint(identificador, __name__, url_prefix=prefijo_url)

bp = crear_blueprint('comprobantes-pagos', '/comprobantes-pagos')

@bp.route("", methods=["POST"])
def registrar_comprobante():
   try:
        comando = RegistrarComprobante()
        comando.request = request
        comprobante = ejecutar_comando_obtener_comprobante(comando)

        queryConsultarAfiliacion = ConsultarAfiliacion(comprobante["afiliacion_id"])
        ejecutar_query_consultar_afiliacion(queryConsultarAfiliacion)

        ejecutar_comando_registrar_comprobante(comando)

        comandoActualizarAfiliacion = ActualizarAfiliacion()
        comandoActualizarAfiliacion.afiliacion_id = comprobante["afiliacion_id"]        
        ejecutar_comando_actualizar_afiliacion(comandoActualizarAfiliacion)

        return {"msg": VALIDACION_COMPROBANTE_EXITOSA}, 200
   except FechaDePagoDebeEstarEnFuturo:
        return { "msg": "Fecha no puede estar en el futuro" }, 500
   except requests.exceptions.HTTPError as HTTPError:
        return { "msg": ERROR_AFILIACION_HTTP  }, HTTPError.response.status_code 
   except requests.exceptions.RequestException as HTTPError:
        return { "msg": ERROR_GENERAL_HTTP}, HTTPError.response.status_code 
   except Exception:
        return { "msg": ERROR_GENERAL }, 500