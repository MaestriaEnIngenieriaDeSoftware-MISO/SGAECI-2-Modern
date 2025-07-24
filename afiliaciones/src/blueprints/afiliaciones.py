from flask import Blueprint, jsonify

from src.commands.reset_database import ResetDatabase

afiliaciones_blueprint = Blueprint('afiliaciones', __name__, url_prefix='/afiliaciones')


@afiliaciones_blueprint.route('/reset', methods=['POST'])
def reset_database():
    # Reset the database
    ResetDatabase().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"}), 200
