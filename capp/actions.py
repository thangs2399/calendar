
#################### IMPORTS ####################

# 1
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

# 2
from capp.auth import login_required
from capp.db import get_db



#################### ACTIONS #########################

# check user's session existence
def sessionExists():

    user_id = session.get('user_id')

    if user_id is None:
        return False
    else:
        return True