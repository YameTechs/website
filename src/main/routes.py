from flask import Blueprint, render_template
from flask_login import current_user

from src.main.utils import RedirBox

main = Blueprint("main", __name__)

USER = [RedirBox("Logout", redirect="users.logout")]

GUEST = [
    RedirBox("Login", redirect="users.login"),
    RedirBox("Register", redirect="users.register"),
]

BOXES = []


@main.route("/")
@main.route("/home/")
@main.route("/navigation/")
def home():
    boxes = BOXES[:]
    if current_user.is_authenticated:
        boxes.extend(USER)
    else:
        boxes.extend(GUEST)

    return render_template("home.html", boxes=boxes)
