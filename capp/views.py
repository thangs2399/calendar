
############################## IMPORTS ##############################

# 1
from xmlrpc.client import Boolean
from flask import Blueprint, request, render_template, session, g, redirect
import functools
from capp.db import get_db
from capp.actions import sessionExists
from capp import email
from flask_mail import Message

############################## VIEWS ##############################

views = Blueprint("views", __name__)



############### HOMEPAGE/Calendar ###############

@views.route("/")
@views.route("/calendar-monthly")
def homepage():
    
    if (not sessionExists()):

        return redirect("/auth/login")

    return render_template('homepage.html')

@views.route("/calendar-weekly")
def weeklyView():
    return "weekly view"

@views.route("/calendar-daily")
def dailyView():
    return "daily view"



############### PROFILE ###############

@views.route("/profile")
def profile():

    if (not sessionExists()):

        return redirect("/auth/login")

    user_id = session.get('user_id')

    db = get_db()

    user =  db.execute(
            'SELECT username, email FROM users WHERE user_id = ?', (user_id,)
        ).fetchone()

    return render_template('profile.html', username = user["username"] , email = user["email"])



############### GROUPS ###############

@views.route("/groups")
def gorups():

    if (not sessionExists()):

        return redirect("/auth/login")

    return render_template('groups.html')



############### HELP ###############

@views.route("/help", methods=["GET", "POST"])
def help():

    if (not sessionExists()):

        return redirect("/auth/login")

    if (request.method == "POST"):

        user_email = request.form["email"]
        user_message = request.form["message"]

        message = Message( "FlaskApp Help", sender = user_email, recipients = ['capp.supp2022@gmail.com', 'slmthang23@gmail.com', 'thangs@my.canisius.edu'])
        message.body = user_message 

        mail = email()

        mail.send(message)

        return render_template('help-sent.html')

    return render_template('help.html')



############### SETTINGS ###############

@views.route("/settings")
def settings():

    if (not sessionExists()):

        return redirect("/auth/login")

    return render_template('settings.html')




# PAGE NOT FOUND
@views.errorhandler(404)
def not_found(e):
    return "<h1>PAGE NOT FOUND</h2>"



