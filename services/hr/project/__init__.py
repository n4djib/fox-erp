import os
from flask import Flask


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    # db.init_app(app)

    # register blueprints
    from project.api.hr import hr_blueprint
    app.register_blueprint(hr_blueprint, url_prefix='/hr')
    # from project.api.auth import auth_blueprint
    # app.register_blueprint(auth_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    # app.shell_context_processor({'app': app, 'db': db})

    return app
