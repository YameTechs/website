from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from src.config import Config


_admin = Admin()
_bcrypt = Bcrypt()
_db = SQLAlchemy()
_login_manager = LoginManager()
_login_manager.login_view = "users.login"  # Redirect the user to f"/{login}"
_mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    _admin.init_app(app)
    _db.init_app(app)
    _bcrypt.init_app(app)
    _login_manager.init_app(app)
    _mail.init_app(app)

    from src.main.routes import main
    from src.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    from src.models import User, Role, user_role  # noqa

    _admin.add_view(ModelView(User, _db.session))
    _admin.add_view(ModelView(Role, _db.session))

    with app.app_context():
        _db.create_all()

    return app
