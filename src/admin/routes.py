from flask import Blueprint
from flask_admin import Admin

from src import _db
from src.admin.views import MyAdminIndexView, MyAdminView
from src.models import Role, User


# A class to make flask_admin work with flask Blueprints
class AdminBlueprint(Blueprint):
    views = []

    def __init__(self, *args, **kwargs):
        super(AdminBlueprint, self).__init__(*args, **kwargs)

        # Create admin
        self._admin = Admin(
            name="Database",
            index_view=MyAdminIndexView(url=f"{self.url_prefix}database"),
        )

    def add_view(self, view):
        self.views.append(view)

    def register(self, app, options):
        self._admin.init_app(app)

        for view in self.views:
            self._admin.add_view(view)

        return super(AdminBlueprint, self).register(app, options)


admin = AdminBlueprint("admin_hack", __name__, url_prefix="/admin/")
admin.add_view(MyAdminView(User, _db.session))
admin.add_view(MyAdminView(Role, _db.session))
