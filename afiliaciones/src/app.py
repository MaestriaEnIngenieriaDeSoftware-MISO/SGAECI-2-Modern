from flask import Flask
from .blueprints.health_check import health_check_blueprint
from .database import init_db

app = Flask(__name__)
init_db(app)
app.register_blueprint(health_check_blueprint)

if __name__ == '__main__':
    app.run()
