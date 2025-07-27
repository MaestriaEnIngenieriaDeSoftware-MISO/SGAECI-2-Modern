from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import logging

from src.blueprints.afiliaciones import afiliaciones_blueprint
from .blueprints.health_check import health_check_blueprint
from .database import init_db
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException
from .errors.errors import ApiError

# Cargar variables de entorno
load_dotenv()

# Configurar logging según LOG_LEVEL del entorno
log_level = os.environ.get("LOG_LEVEL", "WARNING").upper()
logging.basicConfig(level=getattr(logging, log_level))

app = Flask(__name__)
init_db(app)
app.register_blueprint(health_check_blueprint)
app.register_blueprint(afiliaciones_blueprint)


@app.errorhandler(Exception)
def handle_exception(err):
    version = os.environ.get("VERSION", default="1.0")
    if isinstance(err, ApiError):
        response = {
            "msg": err.description,
            "version": version
        }
        return jsonify(response), err.code
    if isinstance(err, ValidationError):
        response = {
            "msg": err.messages_dict,
            "version": version
        }
        return jsonify(response), 400
    if isinstance(err, HTTPException):
        response = {
            "code": err.code,
            "name": err.name,
            "description": err.description,
            "version": version,
        }
        return jsonify(response), err.code
    response = {
        "msg": str(err),
        "version": version,
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run()
