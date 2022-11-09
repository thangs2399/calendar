#################### IMPORTS ####################

import os

from flask import Flask, render_template, g
from flask_mail import Mail, Message
from flask_mysqldb import MySQL

mail = Mail()
mysql = MySQL()


#################### App Factory ####################

def create_app(test_config=None):

    ############### APP CONFIG ###############

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(

        #################### DEFAULT CONFIG ####################

        SECRET_KEY='dev',

        ############################################################


        #################### MAIL CONFIG ####################
        
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 465,
        MAIL_USERNAME = 'capp.supp2022@gmail.com',
        MAIL_PASSWORD = 'gbmvlzxviioohyer',
        MAIL_USE_TLS = False,
        MAIL_USE_SSL = True,

        ############################################################


        #################### MYSQL CONFIG ####################

        MYSQL_HOST = '127.0.0.1',
        MYSQL_USER = 'root',
        MYSQL_PASSWORD = 'red781',
        MYSQL_DB = 'capp',
        MYSQL_PORT = 4000,
        MYSQL_CURSORCLASS = 'DictCursor' # return rows as dictionary

        ############################################################
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    ############### EXTENSIONS ###############

    initialize_extensions(app) # for mailing, mysql


    ############### AUTH ###############

    from . import auth
    app.register_blueprint(auth.auth)  # register bp


    ############### ROUTES/VIEWS ###############

    from . import views
    app.register_blueprint(views.views)  # register bp


    ########################################

    return app # return the app



# need this to email
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
    mysql.init_app(app)