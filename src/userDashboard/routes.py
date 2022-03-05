from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from src import _db
from src.models import User
from src.userDashboard.forms import EditUserDataForm, ResendEmailButton
from src.users.utils import send_user_email

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/account/", methods=["POST", "GET"])
@login_required
def index():
    editdata = EditUserDataForm()
    form = ResendEmailButton()
    return render_template(
        "account.html", getattr=getattr, form=form, editdata=editdata
    )


@dashboard.route("/account/verify/", methods=["POST", "GET"])
@login_required
def verify():
    form = ResendEmailButton()
    if not (form.validate_on_submit() and form.submit.data):
        return render_template(url_for(index), getattr=getattr, form=form)

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
    return redirect(url_for(index), getattr=getattr, form=form)


@dashboard.route("/account/edit-data/<int:id>", methods=["POST", "GET"])
@login_required
def edit_Data(id):
    editdata = EditUserDataForm()
    data = User.query.get_or_404(id)

    if editdata.validate_on_submit():
        data.username = request.username["username"]
        data.email = request.email["email"]
        try:
            _db.session.commit()
            flash("Updated Successfully")
            return redirect(
                url_for(index), getattr=getattr, editdata=editdata, data=data
            )
        except:
            flash("Something went wrong. Try again")
            return redirect(
                url_for(index), getattr=getattr, editdata=editdata, data=data
            )
    else:
        return redirect(url_for(index), getattr=getattr, editdata=editdata, data=data)
