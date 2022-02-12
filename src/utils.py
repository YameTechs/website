from functools import wraps

from flask import abort, redirect, url_for
from flask_login import current_user

MAIN_VIEW = "main.home"


def logout_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for(MAIN_VIEW))
        return func(*args, **kwargs)

    return decorated_function


def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.has_role("admin"):
            return func(*args, **kwargs)
        abort(404)

    return decorated_function
