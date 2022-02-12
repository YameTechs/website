from flask import abort, render_template
from flask_login import current_user

from src import _db
from src.admin.views import AdminBlueprint, MyAdminView
from src.models import Role, Service, User

admin = AdminBlueprint("admin_hack", __name__, url_prefix="/admin/")
admin.add_view(MyAdminView(User, _db.session))
admin.add_view(MyAdminView(Role, _db.session))
# admin.add_view(MyAdminView(Service, _db.session))


@admin.route("/")
def index():
    return render_template("admin/home.html")


@admin.before_request
def abort_if_peasant():
    if current_user.is_authenticated and current_user.has_role("admin"):
        return
    abort(404)
