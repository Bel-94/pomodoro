from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import config_options 


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
   
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # configure_uploads(app,photos)

    # Initializing flask extensions
    # bootstrap.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app