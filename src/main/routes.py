from flask import Blueprint, render_template
from flask_login import current_user

from src.main.utils import RedirBox

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home/")
def home():
    return render_template("home.html")
