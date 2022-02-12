from flask import Blueprint, abort
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MyAdminView(ModelView):
    def is_accessible(self):
        # The order of the if statements is important
        return current_user.is_authenticated and current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


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
