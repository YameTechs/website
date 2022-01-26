from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from src import bcrypt, db
from src.models import User
from src.users.forms import (LoginForm, RegistrationForm, RequestResetFrom,
                             ResendEmailButton, ResetPasswordForm)
from src.users.utils import send_user_email

users = Blueprint("users", __name__)


@users.route("/account/", methods=["POST", "GET"])
@login_required
def account():
    form = ResendEmailButton()

    if form.validate_on_submit():
        if form.submit.data:
            msg_body = (
                "To verify your account, visit the following link:\n"
                "{}\n"
                "If you did not make this request then simply ignore this email and no"
                "changes will be made"
            )
            send_user_email(current_user, "Account Verification", msg_body, "users.verify_token")
            flash('An email has been send with your verification link!')

    return render_template("account.html", getattr=getattr, form=form)


@users.route("/login/", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.home"))
        else:
            flash("incorrect data!")

    return render_template("login.html", form=form)


@users.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@users.route("/register/", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template("register.html", form=form)

    hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
    user = User(
        email=form.email.data,
        username=form.username.data,
        password=hashed_password,
        is_verified=False,
    )

    msg_body = (
        "To verify your account, visit the following link:\n"
        "{}\n\n"
        "If you did not make this request then simply ignore this email and no"
        "changes will be made"
    )

    send_user_email(user, "Account Verification", msg_body, "users.verify_token")

    db.session.add(user)
    db.session.commit()

    flash("You have registered in!")
    return redirect(url_for("users.login"))


@users.route("/request_token/", methods=["POST", "GET"])
def request_token():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash("that email seems to be invalid!")
            return redirect(url_for('users.request_token'))

        msg_body = (
            "To change your password, visit the following link:\n"
            "{}\n\n"
            "If you did not make this request then simply ignore this email and no"
            "changes will be made"
        )

        send_user_email(user, "Forgotten Password", msg_body, "users.reset_password")
        flash("an email has been sent!")
        return redirect(url_for('users.login'))
    return render_template("request_token.html", form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    user = User.get_user_by_token(token)
    if user is None:
        flash('That is an invalid or expired token')
        return redirect(url_for('users.request_token'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', title='Reset Password', form=form)


@users.route("/verify_token/<token>/", methods=["POST", "GET"])
def verify_token(token):
    user = User.get_user_by_token(token)
    if user is None:
        msg = "that's an invalid token lul, please request a new verification token"
        return render_template("verify_token.html", msg=msg)

    user.is_verified = True
    db.session.commit()
    msg = "Congratulation you have been verified"
    return render_template("verify_token.html", msg=msg)

@users.route("/about/")
def about():
    about()
    return redirect(url_for("main.home"))