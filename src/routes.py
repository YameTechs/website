from src import app
from flask import render_template, redirect, url_for
from src.forms import RegistrationForm, LoginForm

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/login/")
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email == "test@test.com" and form.password == "password":
            return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route("/logout/")
def logout():
    return render_template("home.html")


@app.route("/register/", methods=["POST", "GET"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        return redirect(url_for('home'))

    return render_template("register.html", form=form)


@app.route("/account/")
def account():
    return render_template("home.html")


@app.route("/admin/")
def admin():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("home.html")


@app.route("/contacts/")
def contacts():
    return render_template("home.html")


@app.route("/game/")
def game():
    return render_template("home.html")


@app.route("/portfolio/")
def portfolio():
    return render_template("home.html")


@app.route("/portfolio/projects/")
def projects():
    return render_template("home.html")


@app.route("/services/")
def services():
    return render_template("home.html")



@app.route("/services/bots/")
def bots():
    return render_template("home.html")


@app.route("/services/websites/")
def websites():
    return render_template("home.html")
