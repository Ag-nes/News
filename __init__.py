# from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config
#
# bootstrap = Bootstrap()
#
#
# def create_app(config_name, request=None):
#     app = Flask(__name__)
#
#     # Creating the app configurations
#     app.config.from_object(config[config_name])
#
#     # Initializing flask extensions
#     bootstrap.init_app(app)
#
#     # Registering the blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     # setting config
#     from .request import configure_request
#     configure_request(app)
#
#     # Will add the views and forms
#
#     return app
