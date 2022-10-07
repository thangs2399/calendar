from flask import Blueprint, request, render_template
import functools

############################## VIEWS ##############################

views = Blueprint("views", __name__)



############### HOMEPAGE/Calendar ###############

@views.route("/")
@views.route("/calendar-monthly")
def homepage():
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
    return render_template('profile.html')



############### GROUPS ###############

@views.route("/groups")
def gorups():
    return render_template('groups.html')



############### HELP ###############

@views.route("/help")
def help():
    return render_template('help.html')



############### SETTINGS ###############

@views.route("/settings")
def settings():
    return render_template('settings.html')




# PAGE NOT FOUND
@views.errorhandler(404)
def not_found(e):
    return "<h1>PAGE NOT FOUND</h2>"
