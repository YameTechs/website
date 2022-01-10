from src import app
from flask import render_template


class Box:
    def __init__(self, name, description=None) -> None:
        self.name = name
        if description is None:
            description = f"{name} related stuff"
        self.description = description


BOXES = [Box("Portfolio"), Box("Contants"), Box("Game"), Box("Services")]


@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", boxes=BOXES)


@app.route("/admin/")
def admin():
    return render_template("home.html", boxes=BOXES)


@app.route("/about/")
def about():
    return render_template("home.html", boxes=BOXES)


@app.route("/contacts/")
def contacts():
    return render_template("home.html", boxes=BOXES)


@app.route("/game/")
def game():
    return render_template("home.html", boxes=BOXES)


@app.route("/portfolio/")
def portfolio():
    return render_template("home.html", boxes=BOXES)


@app.route("/portfolio/projects/")
def projects():
    return render_template("home.html", boxes=BOXES)


@app.route("/services/")
def services():
    return render_template("home.html", boxes=BOXES)


@app.route("/services/bots/")
def bots():
    return render_template("home.html", boxes=BOXES)


@app.route("/services/websites/")
def websites():
    return render_template("home.html", boxes=BOXES)
