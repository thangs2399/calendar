
#################### IMPORTS ####################


import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from capp.db import get_db
from capp import email
from flask_mail import Message

import random

#################### BLUEPRINTS ( AUTH ) ####################

auth = Blueprint('auth', __name__, url_prefix='/auth')



######################## AUTH ROUTES ########################


##### SIGN UP #####
@auth.route('/signup', methods=('GET', 'POST'))
def register():
    """
        -> sign up user 
        -> store user info to the database
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        dob = request.form["dob"]
        gender = request.form["gender"]

        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO users (username, email, password, dob, gender) VALUES (?, ?, ?, ?, ?)",
                    (username, email, generate_password_hash(password), dob, gender),
                )
                db.commit()

            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/signup.html')



##### Log In #####
@auth.route('/login', methods=('GET', 'POST'))
def login():
    """
        -> log in existing user 
        -> store user's session using the user's id
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user'] =  user['user_id']
            return redirect("/auth/verification")

        flash(error)

    return render_template("auth/login.html")


@auth.route("/verification", methods=('GET', 'POST'))
def verification():
    """
        -> send verification code to user's email
        -> user put in the code
        -> take user to homepage if successful, else back to login page
    """
    db = get_db()


    if (request.method == "POST"):

        entered_code = request.form["vcode"]
        
        user_info = db.execute(
            'SELECT * FROM users WHERE user_id = ?', (session["user"],)
        ).fetchone()

        actual_code = user_info["code"]

        # if entered code matches, redirect to homepage
        if str(entered_code) == str(actual_code):

            session['user_id'] =  user_info['user_id']

            return redirect("/")

        else:

            return redirect("/auth/login")


    # fetch user's email from database
    user = db.execute(
        'SELECT * FROM users WHERE user_id = ?', (session["user"],)
    ).fetchone()

    user_email = user["email"]

    # generate random code
    code = random.randint(10000,100000)

    # store the code in the database
    db.execute(
        "UPDATE users SET code = ? WHERE user_id = ?", (code, session["user"])
    )
    db.commit()

    # send verification code
    message = Message( "Verification Code for CAPP", sender = 'capp.supp2022@gmail.com', recipients = ['capp.supp2022@gmail.com', user_email])
    message.body = str(code)
    mail = email()
    mail.send(message)


    return render_template("auth/2fa.html")

##### LOG OUT #####
@auth.route('/logout')
def logout():
    """
        -> logout user 
        -> clears session
        -> takes to log in page
    """
    session.clear()
    return redirect("/auth/login")





# ????????????????????????????????????????? #

##### runs before every url request #####
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE user_id = ?', (user_id,)
        ).fetchone()


## ????
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view