import os
from flask import Flask
from instance.config import Config
from decouple import config
from flask_babel import Babel
from flask_mongoengine import MongoEngine


db = MongoEngine()
babel = Babel()


def create_app(config_class=Config):

    app = Flask(__name__)

    # app_settings = config('APP_SETTINGS', 'instance.config.Config')

    app.config.from_object(config_class)

    db.init_app(app)
    babel.init_app(app)

    from .meta_data import meta_data_blueprint
    app.register_blueprint(meta_data_blueprint)

    return app
