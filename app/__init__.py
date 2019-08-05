from flask import Flask
import flask_cors
from flask_sqlalchemy import SQLAlchemy



cors = flask_cors.CORS()
db = SQLAlchemy()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)
    db.init_app(app)

    return app
