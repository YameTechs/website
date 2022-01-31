from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home/")
def home():
    return render_template("home.html")

@main.route("/services/")
def services():
    return render_template("services.html")