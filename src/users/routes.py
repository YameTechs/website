from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from src import _bcrypt, _db
from src.models import Role, User
from src.users.forms import (
    LoginForm,
    RegistrationForm,
    RequestResetFrom,
    ResetPasswordForm,
)
from src.users.utils import send_user_email
from src.utils import logout_required

users = Blueprint("users", __name__)


@users.route("/login/", methods=["POST", "GET"])
@logout_required
def login():
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template("login.html", form=form)

    user = User.query.filter_by(email=form.email.data).first()
    if user and _bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get("next")
        flash("You're logged in!")
        return redirect(next_page or url_for("main.home"))

    flash("incorrect data!")
    return render_template("login.html", form=form)


@users.route("/logout/")
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for("main.home"))


@users.route("/register/", methods=["POST", "GET"])
@logout_required
def register():
    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template("register.html", form=form)

    hashed_password = _bcrypt.generate_password_hash(form.password.data).decode("utf-8")
    user = User(
        email=form.email.data,
        username=form.username.data,
        password=hashed_password,
    )

    msg_body = (
        "To verify your account, visit the following link:\n"
        "{}\n\n"
        "If you did not make this request then simply ignore this email and no"
        "changes will be made"
    )

    send_user_email(user, "Account Verification", msg_body, "users.verify_token")

    _db.session.add(user)
    _db.session.commit()

    flash("You have registered in!")
    return redirect(url_for("users.login"))


@users.route("/request_token/", methods=["POST", "GET"])
@logout_required
def request_token():
    form = RequestResetFrom()
    if not form.validate_on_submit():
        return render_template("request_token.html", form=form)

    user = User.query.filter_by(email=form.email.data).first()
    if user is None:
        flash("that email seems to be invalid!")
        return redirect(url_for("users.request_token"))

    msg_body = (
        "To change your password, visit the following link:\n"
        "{}\n\n"
        "If you did not make this request then simply ignore this email and no"
        "changes will be made"
    )

    send_user_email(user, "Forgotten Password", msg_body, "users.reset_password")
    flash("an email has been sent!")
    return redirect(url_for("users.login"))


@users.route("/reset_password/<token>", methods=["GET", "POST"])
@logout_required
def reset_password(token):
    user = User.get_user_by_token(token)
    if user is None:
        flash("That is an invalid or expired token")
        return redirect(url_for("users.request_token"))

    form = ResetPasswordForm()
    if not form.validate_on_submit():
        return render_template("reset_password.html", title="Reset Password", form=form)

    user.password = _bcrypt.generate_password_hash(form.password.data).decode("utf-8")
    _db.session.commit()
    flash("Your password has been updated! You are now able to log in", "success")
    return redirect(url_for("users.login"))


@users.route("/settings/", methods=["POST", "GET"])
@login_required
def settings():
    return render_template("settings.html")


@users.route("/verify_token/<token>/", methods=["POST", "GET"])
def verify_token(token):
    user = User.get_user_by_token(token)
    if user is None:
        return render_template("verify_token.html", success=False)

    verified_role = Role.query.filter_by(name="verified").first()
    user.roles.append(verified_role)
    _db.session.commit()
    return render_template("verify_token.html", success=True)
