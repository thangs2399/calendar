#################### IMPORTS ####################

import os

from flask import Flask, render_template, g
from flask_mail import Mail, Message


mail = Mail()


#################### App Factory ####################

def create_app(test_config=None):

    ############### APP CONFIG ###############

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'capp.sqlite'),

        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 465,
        MAIL_USERNAME = 'capp.supp2022@gmail.com',
        MAIL_PASSWORD = 'gbmvlzxviioohyer',
        MAIL_USE_TLS = False,
        MAIL_USE_SSL = True,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    ############### EXTENSIONS ###############

    initialize_extensions(app) # for mailing, 

    ############### DATABASE ###############

    from . import db
    db.init_app(app)  # initialize database
    with app.app_context():
        db.init_db()


    ############### AUTH ###############

    from . import auth
    app.register_blueprint(auth.auth)  # register bp


    ############### ROUTES/VIEWS ###############

    from . import views
    app.register_blueprint(views.views)  # register bp


    ########################################

    return app # return the app




def email():
    """
        > store "mail instance" to g and returns it
    """
    if "ml" not in g:

        g.ml = mail
    
    return g.ml


def initialize_extensions(app):
    """
        for extensions
    """
    mail.init_app(app)