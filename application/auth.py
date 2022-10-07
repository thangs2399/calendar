from flask import Blueprint


############################## AUTH ##############################

auth = Blueprint("auth", __name__)



############### LOGIN ###############

@auth.route("/login")
def login():
    return "<h1>LOG IN</h1>"



############### SIGN UP ###############

@auth.route("/signup")
def signup():
    return "<h1>SIGN UP</h1>"



############### LOG OUT ###############

@auth.route("/logout")
def logout():
    return "<h1>LOG OUT</h1>"