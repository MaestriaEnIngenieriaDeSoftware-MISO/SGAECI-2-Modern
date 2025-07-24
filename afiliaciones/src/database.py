import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Cargar configuración desde variables de entorno
DB_NAME = os.environ.get('DB_NAME', 'app.db')

# Para SQLite, solo se usa el nombre del archivo
DATABASE_URI = f'sqlite:///{DB_NAME}'

db = SQLAlchemy()


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'
    db.init_app(app)
