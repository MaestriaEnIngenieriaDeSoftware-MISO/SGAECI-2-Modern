from flask import Blueprint

health_check_blueprint = Blueprint('health_check', __name__, url_prefix='/afiliaciones')

@health_check_blueprint.route('/health', methods=['GET'])
def health():
    return {"status": "up"}, 200