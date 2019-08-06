from flask import Flask
import flask_cors
from flask_sqlalchemy import SQLAlchemy



cors = flask_cors.CORS()
db = SQLAlchemy()


def create_app(config_class):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)

    cors.init_app(flask_app)
    db.init_app(flask_app)

    from app.routes import health_check
    flask_app.register_blueprint(health_check.bp)

    from app.routes import person
    flask_app.register_blueprint(person.bp)

    return flask_app
