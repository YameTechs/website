from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .forms import UpdateAccountForm, ResendEmailButton
from src import _db
from src.users.utils import send_user_email


dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/account/", methods=["POST", "GET"])
@login_required
def index():
    update_account_form = UpdateAccountForm()
    resend_email_button_form = ResendEmailButton()

    # since resend email button form does not have an email we can use this to identify
    # which one is it.
    if request.form.get('email') is None and request.form.get('submit'):
        msg_body = (
            "To verify your account, visit the following link:\n"
            "{}\n\n"
            "If you did not make this request then simply ignore this email and no"
            "changes will be made"
        )

        send_user_email(
            current_user, "Account Verification", msg_body, "users.verify_token"
        )

        flash("An email has been sent to your account", "success")

    elif update_account_form.validate_on_submit():
        # if update_account_form.picture.data:
        #     delete_picture(current_user.image_file)
        #     picture_file = save_picture(update_account_form.picture.data)
        #     current_user.image_file = picture_file

        current_user.username = update_account_form.username.data
        current_user.email = update_account_form.email.data
        _db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("dashboard.index"))

    elif request.method == "GET":
        update_account_form.username.data = current_user.username
        update_account_form.email.data = current_user.email

    return render_template(
        "account.html",
        title="Account",
        update_account_form=update_account_form,
        resend_email_button_form=resend_email_button_form
    )

    # image_file = url_for("static", filename=f"profile_pics/{current_user.image_file}")
    # return render_template(
    #     "account.html", title="Account", image_file=image_file, form=form
    # )
