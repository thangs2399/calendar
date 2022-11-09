
############################## IMPORTS ##############################

# 1
from xmlrpc.client import Boolean
from flask import Blueprint, request, render_template, session, g, redirect, flash
import functools

from capp.actions import sessionExists, sendEmail
from capp import email, mysql
from flask_mail import Message

############################## VIEWS ##############################

views = Blueprint("views", __name__)



############### HOMEPAGE/Calendar ###############

@views.route("/")
@views.route("/calendar-monthly")
def homepage():

    if (not sessionExists()):

        return redirect("/auth/login")

    return render_template("homepage.html")

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

    # get username and email from session
    username = session["user"]["username"]
    email = session["user"]["email"]

    return render_template('profile.html', username = username , email = email)



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

        # get user's email and message from the form
        user_email = request.form["email"]
        user_message = request.form["message"]

        
        messageStatus = sendEmail("Help Needed - " + user_email, user_message, user_email, 'capp.supp2022@gmail.com')
    
        if messageStatus:

            flash("Message successfully delivered!", "s-message")
        
        else:

            flash("Message delivery failed!", "e-message")

        return render_template('help.html')

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



