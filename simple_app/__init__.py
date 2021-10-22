import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from simple_app import calculator


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    csrf = CSRFProtect(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import calculator

    app.register_blueprint(calculator.bp)

    return app
