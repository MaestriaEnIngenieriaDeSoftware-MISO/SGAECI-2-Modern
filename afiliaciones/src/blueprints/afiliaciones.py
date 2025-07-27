from flask import Blueprint, jsonify, request
import logging

from src.commands.reset_database import ResetDatabase
from src.commands.create_afiliacion import CreateAfiliacion
from src.schemas.afiliacion import AfiliacionRequestSchema, AfiliacionUpdateSchema, AfiliacionConsultaSchema
from src.utils.mapeadores import map_externo_to_dto
from src.models.afiliacion import Afiliacion
from src import database
from src.queries.consulta_afiliacion import ConsultaAfiliacion
from src.queries.actualizar_afiliacion import ActualizarAfiliacion

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


@afiliaciones_blueprint.route('/<int:afiliacion_id>', methods=['GET'])
def consultar_afiliacion(afiliacion_id):
    afiliacion = ConsultaAfiliacion().execute(afiliacion_id)
    if not afiliacion:
        return jsonify({'msg': 'Afiliación no encontrada'}), 404
    schema = AfiliacionConsultaSchema()
    result = schema.dump(afiliacion)
    return jsonify(result), 200


@afiliaciones_blueprint.route('/<int:afiliacion_id>', methods=['PUT'])
def actualizar_afiliacion(afiliacion_id):
    data = request.get_json()
    schema = AfiliacionUpdateSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    afiliacion = ActualizarAfiliacion().execute(afiliacion_id, data)
    if not afiliacion:
        return jsonify({'msg': 'Afiliación no encontrada'}), 404
    return jsonify({'msg': 'Afiliación actualizada'}), 200
