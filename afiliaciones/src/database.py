import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Cargar configuración desde variables de entorno
DB_NAME = os.environ.get('DB_NAME', 'app.db')
DB_HOST = os.environ.get('DB_HOST', '')
DB_USER = os.environ.get('DB_USER', '')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_PORT = os.environ.get('DB_PORT', '')

# Para SQLite, solo se usa el nombre del archivo
DATABASE_URI = f'sqlite:///{DB_NAME}'

db = SQLAlchemy()


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'
    db.init_app(app)

    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()
