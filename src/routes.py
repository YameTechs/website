from src import app
from flask import render_template


class Box:
    def __init__(self, name, description=None) -> None:
        self.name = name
        if description is None:
            description = f"{name} related stuff"
        self.description = description

BOXES = [Box("Discord"), Box("Game"), Box("Portfolio"), Box("Services")]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", boxes=BOXES)

@app.route("/admin")
def admin():
    return render_template("home.html", boxes=BOXES)

@app.route("/discord")
def discord():
    return render_template("home.html", boxes=BOXES)

@app.route("/game")
def game():
    return render_template("home.html", boxes=BOXES)

@app.route("/portfolio")
def portfolio():
    return render_template("home.html", boxes=BOXES)

@app.route("/services")
def services():
    return render_template("home.html", boxes=BOXES)
