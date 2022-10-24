
#################### IMPORTS ####################

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from capp.auth import login_required
from capp.db import get_db



#################### ACTIONS #########################

# 
def sessionExists():
    """
        > check user's session existence
    """
    user_id = session.get('user_id')

    if user_id is None:
        return False
    else:
        return True
