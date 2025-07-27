### import saludtechalpes.seedwork.presentacion.api as api
from flask import request, jsonify
from flask import (Blueprint, flash) 
from comprobantespagos.aplicacion.comandos.registrar_comprobante import RegistrarComprobante, ejecutar_comando_registrar_comprobante
from comprobantespagos.aplicacion.comandos.actualizar_afiliacion import ActualizarAfiliacion, ejecutar_comando_actualizar_afiliacion
from comprobantespagos.aplicacion.queries.consultar_afiliacion import ejecutar_query_consultar_afiliacion, ConsultarAfiliacion
from comprobantespagos.dominio.constants import ERROR_GENERAL
#g, redirect, render_template, request, session, url_for)
##from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
##from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
##from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson
## from saludtechalpes.modulos.imagenes.infraestructura.despachadores import Despachador

def crear_blueprint(identificador: str, prefijo_url: str):
    return Blueprint(identificador, __name__, url_prefix=prefijo_url)

bp = crear_blueprint('comprobantes-pagos', '/comprobantes-pagos')

@bp.route("", methods=["POST"])
def registrar_comprobante():
    try:
        comandoActualizarAfiliacion = ActualizarAfiliacion()
        comando = RegistrarComprobante()
        comando.request = request
        comprobante = ejecutar_comando_registrar_comprobante(comando)
        ejecutar_comando_actualizar_afiliacion(comandoActualizarAfiliacion)
        queryConsultarAfiliacion = ConsultarAfiliacion("123123")
        ejecutar_query_consultar_afiliacion(queryConsultarAfiliacion)
        return "", 200
    except Exception:
        return { "msg": ERROR_GENERAL }, 500