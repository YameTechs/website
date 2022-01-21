from datetime import datetime

from flask_login import UserMixin
from itsdangerous.jws import TimedJSONWebSignatureSerializer as Serializer

from src import db, login_manager
from src.config import Config


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default="default.jpeg")
    password = db.Column(db.String(69), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False)

    def get_verification_token(self, expires_sec=1800):
        dictionary = {"user_id": self.id}
        s = Serializer(Config.SECRET_KEY, expires_sec)
        return s.dumps(dictionary).decode("utf-8")

    @staticmethod
    def get_user_by_token(token):
        s = Serializer(Config.SECRET_KEY)

        try:
            user_id = s.loads(token)["user_id"]
        except KeyError:
            return None

        return User.query.get(user_id)

    def __repr__(self):
        return f"User({self.id=}, {self.username=}, {self.email=})"


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69), unique=True, nullable=False)
    override = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Role({self.id=}, {self.name=}, {self.override=})"


class UserRole(db.Model):
    __tablename__ = "usersroles"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    role = db.Column(db.Integer, db.ForeignKey("roles.id"))

    users = db.relationship(User)
    roles = db.relationship(Role)

    def __repr__(self):
        return f"UserRole({self.id=}, {self.user=}, {self.role=})"


class Redirbox(db.Model):
    __tablename__ = "redirboxes"
    name = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    route = db.Column(db.String(69), unique=True, nullable=False)

    def __repr__(self):
        return f"RedirBox({self.id=}, {self.name=}, {self.route=})"
