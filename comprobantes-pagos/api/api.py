### import saludtechalpes.seedwork.presentacion.api as api
from flask import request, jsonify
from flask import (Blueprint, flash) #g, redirect, render_template, request, session, url_for)
##from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
##from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
##from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson
## from saludtechalpes.modulos.imagenes.infraestructura.despachadores import Despachador

def crear_blueprint(identificador: str, prefijo_url: str):
    return Blueprint(identificador, __name__, url_prefix=prefijo_url)

bp = crear_blueprint('comprobantes-pagos', '/comprobantes-pagos')

@bp.route("", methods=["POST"])
def registrar_comprobante():
    return "", 200