from flask import Blueprint, render_template
from src.models import Project

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home/")
def home():
    projects = Project.query.all()[:2]
    return render_template("home.html", projects=projects)


@main.route("/abouts/")
def about():
    return render_template("about.html")
