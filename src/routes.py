from src import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    return render_template("home.html")

@app.route("/discord")
def discord():
    return render_template("home.html", boxes=BOXES)

@app.route("/game")
def game():
    return render_template("home.html")

@app.route("/portfolio")
def portfolio():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("home.html")
