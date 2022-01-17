from flask import url_for
from flask_mail import Message

from src import mail


def send_user_email(user, msg_head, msg_body):
    token = user.get_verification_token()
    url = url_for("users.verify_token", token=token, _external=True)

    msg = Message(msg_head, sender="noreply@demo.com", recipients=[user.email])

    msg.body = msg_body.format(url)

    mail.send(msg)
