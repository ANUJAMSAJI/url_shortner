from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import short
from .extentions import db

db = SQLAlchemy()
def create_app(config_file='settings.py'):

    app  = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)


    app.register_blueprint(short)
    return app



