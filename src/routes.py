from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from src import app, bcrypt, db
from src.forms import LoginForm, RegistrationForm
from src.models import User


class Box:
    def __init__(self, name, description=None, redirect=None) -> None:
        self.name = name

        if description is None:
            description = f"{name} related stuff"
        self.description = description

        if redirect is None:
            redirect = self.name.lower()
        self.redirect = redirect


BOXES = [
    Box("Portfolio"),
    Box("Contacts"),
    Box("Game"),
    Box("Services"),
    Box("Login"),
    Box("Register"),
    Box("Logout"),
]


@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", boxes=BOXES)


@app.route("/login/", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(url_for(next_page or "home"))
        else:
            flash("incorrect data!")

    return render_template("login.html", form=form)


@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/register/", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            email=form.email.data, username=form.username.data, password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("You have registered in!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/account/")
@login_required
def account():
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
