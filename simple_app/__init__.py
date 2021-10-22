import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    csrf = CSRFProtect(app)

    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    else:
        import flask_monitoringdashboard as dashboard
        dashboard.config.init_from(file=os.getcwd() + '/setup.cfg')
        dashboard.bind(app)
        csrf.exempt(dashboard.blueprint)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import calculator
    app.register_blueprint(calculator.bp)

    return app
