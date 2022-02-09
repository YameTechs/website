from flask import url_for
from flask_mail import Message

from src import _mail


def send_user_email(user, msg_head, msg_body, route):
    token = user.get_verification_token()
    url = url_for(route, token=token, _external=True)

    msg = Message(msg_head, sender="noreply@demo.com", recipients=[user.email])

    msg.body = msg_body.format(url)

    _mail.send(msg)
