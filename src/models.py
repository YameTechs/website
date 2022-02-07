from datetime import datetime

from flask_login import UserMixin
from itsdangerous.jws import TimedJSONWebSignatureSerializer as Serializer

from src import db, login_manager
from src.config import Config


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user_role = db.Table(
    "user_role",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id")),
)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default="default.jpeg")
    password = db.Column(db.String(69), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False)

    roles = db.relationship(
        "Role", secondary=user_role, backref=db.backref("users", lazy="dynamic")
    )

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
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Role({self.id=}, {self.name=})"
