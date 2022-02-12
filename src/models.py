from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from flask_sqlalchemy import event
from itsdangerous.jws import TimedJSONWebSignatureSerializer as Serializer

from src import _bcrypt, _db, _login_manager


@_login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user_role = _db.Table(
    "user_role",
    _db.Column("user_id", _db.Integer, _db.ForeignKey("users.id")),
    _db.Column("role_id", _db.Integer, _db.ForeignKey("roles.id")),
)


class User(_db.Model, UserMixin):
    __tablename__ = "users"
    id = _db.Column(_db.Integer, primary_key=True)
    date_joined = _db.Column(_db.DateTime, nullable=False, default=datetime.utcnow)
    email = _db.Column(_db.String(120), unique=True, nullable=False)
    image_file = _db.Column(_db.String(50), nullable=False, default="default.jpeg")
    password = _db.Column(_db.String(69), nullable=False)
    username = _db.Column(_db.String(20), unique=True, nullable=False)

    roles = _db.relationship(
        "Role", secondary=user_role, backref=_db.backref("users", lazy="dynamic")
    )

    def has_role(self, role):
        return role.lower() in {r.name.lower() for r in self.roles}

    def get_verification_token(self, expires_sec=1800):
        dictionary = {"user_id": self.id}
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps(dictionary).decode("utf-8")

    @staticmethod
    def get_user_by_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])

        try:
            user_id = s.loads(token)["user_id"]
        except KeyError:
            return None

        return User.query.get(user_id)

    def __repr__(self):
        return f"User({self.id=}, {self.username=}, {self.email=})"


class Role(_db.Model):
    __tablename__ = "roles"
    id = _db.Column(_db.Integer, primary_key=True)
    name = _db.Column(_db.String(69), unique=True, nullable=False)
    description = _db.Column(_db.Text)

    def __repr__(self):
        return f"Role({self.id=}, {self.name=})"


class Service(_db.Model):
    __tablename__ = "services"
    id = _db.Column(_db.Integer, primary_key=True)
    title = _db.Column(_db.String(69), nullable=False)
    description = _db.Column(_db.Text)
    price = _db.Column(_db.Integer, nullable=False)
    image_file = _db.Column(_db.String(50), nullable=False, default="default.jpeg")

    def __repr__(self):
        return f"Service({self.id=}, {self.name=}, {self.price=})"


@event.listens_for(Role.__table__, "after_create", once=True)
def add_initial_roles(*args, **kwargs):
    verified_role = Role(name="verified", description="Verified users")
    admin_role = Role(name="admin", description="Administrator")
    _db.session.add_all([verified_role, admin_role])
    _db.session.commit()


@event.listens_for(User.__table__, "after_create", once=True)
def add_initial_user(*args, **kwargs):
    password = _bcrypt.generate_password_hash(
        current_app.config["MAIN_ADMIN_PASSWORD"]
    ).decode("utf-8")

    user = User(
        email=current_app.config["MAIN_ADMIN_EMAIL"],
        username=current_app.config["MAIN_ADMIN_USERNAME"],
        password=password,
    )

    _db.session.add(user)
    _db.session.commit()


@event.listens_for(user_role, "after_create", once=True)
def add_initial_user_roles(*args, **kwargs):
    admin_role = Role.query.filter_by(name="admin").first()

    user = User.query.filter_by(email=current_app.config["MAIN_ADMIN_EMAIL"]).first()
    user.roles.append(admin_role)
    _db.session.commit()
