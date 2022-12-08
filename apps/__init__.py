# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask,request,g
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from flask_babel import Babel, _
import os

base_dir = os.getcwd()
app = Flask(__name__)
app.config["BABEL_TRANSLATION_DIRECTORIES"] = os.path.join(base_dir, "locale")

print("i18n folder: ",app.config["BABEL_TRANSLATION_DIRECTORIES"])
db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel(app)






def register_extensions(app:Flask):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app:Flask):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)



def configure_database(app:Flask):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


#  Babel Language Selector
@babel.localeselector
def get_locale()->str:
    lang = ''
    if request.args.get('lang')!=None: 
        return request.args.get('lang')  # return language passed as lang query string if present
    else:
        try:
            lang = app.config['LANG']  # return language defined by LANG config variable if defined. Returns KeyError if not defined
        except KeyError:  
            lang = request.accept_languages.best_match(app.config['LANGUAGES'])  # return language from the client browser if all the above options are not defined
        return lang


def create_app(config):
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app

