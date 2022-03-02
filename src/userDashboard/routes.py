from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from src import _bcrypt, _db
from src.models import Role, User
from src.userDashboard.forms import EditUserDataForm, ResendEmailButton
from src.users.utils import send_user_email

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/account/", methods=["POST", "GET"])
@login_required
def index():
    return render_template("account.html")


@dashboard.route("/account/verify/", methods=["POST", "GET"])
@login_required
def verify():
    form = ResendEmailButton()
    if not (form.validate_on_submit() and form.submit.data):
        return render_template("account.html", getattr=getattr, form=form)

    msg_body = (
        "To verify your account, visit the following link:\n"
        "{}\n"
        "If you did not make this request then simply ignore this email and no "
        "changes will be made"
    )

    send_user_email(
        current_user, "Account Verification", msg_body, "users.verify_token"
    )

    flash("An email has been send with your verification link!")
    return redirect("account.html", getattr=getattr, form=form)
