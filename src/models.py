from datetime import datetime

from src import db

VERIFIED = bool
PEASANT = bool
STAFF = bool
ADMIN = bool


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default="default.jpeg")
    password = db.Column(db.String(69), nullable=False)
    # role = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"User({self.id=}, {self.username=}, {self.email=})"


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69), unique=True, nullable=False)
    override = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Role({self.id=}, {self.name=}, {self.override=})"


class UsersRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    role = db.Column(db.Integer, db.ForeignKey("roles.id"))

    users = db.relationship(Users)
    roles = db.relationship(Roles)

    def __repr__(self):
        return f"UserRole({self.id=}, {self.user=}, {self.role=})"


class Redirboxes(db.Model):
    name = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    route = db.Column(db.String(69), unique=True, nullable=False)
    role_required = None

    def __repr__(self):
        return f"RedirBox({self.id=}, {self.name=}, {self.route=})"
