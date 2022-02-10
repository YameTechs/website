from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home/")
def home():
    return render_template("home.html")


@main.route("/services/")
def services():
    return render_template("services.html")


@main.route("/abouts/")
def about():
    return render_template("about.html")


@main.route("/projects/")
def projects():
  return render_template("projects.html")
