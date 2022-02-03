import os


class Config:
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ["EMAIL_USER"]
    MAIL_PASSWORD = os.environ["EMAIL_PASS"]
    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]

    TESTING = os.environ["DEVMODE"] == "True"
