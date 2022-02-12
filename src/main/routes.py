from flask import Blueprint, render_template
from src.models import Service

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home/")
def home():
    services = Service.query.all()
    return render_template("home.html", services=services)


@main.route("/about/")
def about():
    return render_template("about.html")
