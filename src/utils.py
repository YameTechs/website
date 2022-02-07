from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


MAIN_VIEW = 'main.home'


def logout_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for(MAIN_VIEW))
        return func(*args, **kwargs)
    return decorated_function
