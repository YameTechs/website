from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from src.config import Config

_bcrypt = Bcrypt()
_db = SQLAlchemy()
_login_manager = LoginManager()
_login_manager.login_view = "users.login"  # Redirect the user to f"/{login}"
_mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Need to be here to avoid circular imports
    from src.admin.routes import admin
    from src.main.routes import main
    from src.models import Role, User, user_role  # noqa
    from src.service.routes import service
    from src.users.routes import users

    app.register_blueprint(admin)
    app.register_blueprint(main)
    app.register_blueprint(service)
    app.register_blueprint(users)

    _db.init_app(app)
    _bcrypt.init_app(app)
    _login_manager.init_app(app)
    _mail.init_app(app)

    # Must have the models imported
    with app.app_context():
        _db.create_all()

    return app
