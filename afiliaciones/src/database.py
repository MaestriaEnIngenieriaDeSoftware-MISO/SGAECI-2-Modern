import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Cargar configuración desde variables de entorno
DB_NAME = os.environ.get('DB_NAME', 'app.db')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '3306')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')

# Para SQLite, solo se usa el nombre del archivo, pero se leen todas las variables para compatibilidad
if DB_HOST and DB_USER and DB_PASSWORD and DB_PORT:
    DATABASE_URI = f'sqlite:///{DB_HOST}:{DB_PORT}/{DB_NAME}'
else:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, DB_NAME)
    DATABASE_URI = f'sqlite:///{DATABASE_PATH}'

db = SQLAlchemy()


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'
    db.init_app(app)
