import os
import sqlite3

from flask import Flask
from flask import current_app



def create_app():

    ################### APP CONFIG ####################

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "fjdlsajf324r"

    # # for database
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE}"
    # db.init_app(app) # initialize database


    #################### VIEWS ####################

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    #################### AUTH ####################

    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")


    #################### DATABASE ####################


    ##################################################

    return app # return app