from flask import Blueprint, jsonify, request
import logging

from src.commands.reset_database import ResetDatabase
from src.commands.create_afiliacion import CreateAfiliacion
from src.schemas.afiliacion import AfiliacionRequestSchema
from src.utils.mapeadores import map_externo_to_dto

afiliaciones_blueprint = Blueprint('afiliaciones', __name__, url_prefix='/afiliaciones')


@afiliaciones_blueprint.route('/reset', methods=['POST'])
def reset_database():
    # Reset the database
    ResetDatabase().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"}), 200


@afiliaciones_blueprint.route('/', methods=['POST'])
def crear_afiliacion():
    data = request.get_json()
    afiliacion_obj = map_externo_to_dto(data, AfiliacionRequestSchema)
    result = CreateAfiliacion().execute(afiliacion_obj)
    return jsonify(result), 201
