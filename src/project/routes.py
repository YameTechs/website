from flask import Blueprint, render_template, request, redirect, url_for, flash
from src import _db
from src.utils import admin_required
from src.models import Project
from src.project.forms import ProjectForm


project = Blueprint("project", __name__)


@project.route("/projects/")
def index():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)


@project.route("/projects/<int:project_id>/view")
def view(project_id):
    projects = [Project.query.get_or_404(project_id)]
    return render_template("projects.html", projects=projects)


@project.route("/projects/<int:project_id>/update/", methods=["GET", "POST"])
@admin_required
def update(project_id):
    form = ProjectForm()
    project = Project.query.get_or_404(project_id)

    if form.validate_on_submit():
        project.title = form.title.data
        project.description = form.description.data
        project.github_url = form.github_url.data
        project.site_url = form.site_url.data
        # project.image_file = form.image_file.data
        _db.session.commit()
        flash("Your project post has been updated!", "success")
        return redirect(url_for("project.view", project_id=project_id))
    elif request.method == "GET":
        project.image_file = form.image_file.data

        form.title.data = project.title
        form.description.data = project.description
        form.github_url.data = project.github_url
        form.site_url.data = project.site_url
        # form.image_file.data = project.image_file

    return render_template("new_project.html", form=form)


@project.route("/projects/<int:project_id>/delete/", methods=["POST"])
@admin_required
def delete(project_id):
    project = Project.query.get_or_404(project_id)
    _db.session.delete(project)
    _db.session.commit()
    flash("Project post has been deleted!", "success")
    return redirect(url_for("project.index"))


@project.route("/projects/new/", methods=["GET", "POST"])
@admin_required
def new():
    form = ProjectForm()
    if not form.validate_on_submit():
        return render_template("new_project.html", form=form)

    project = Project(
        title=form.title.data,
        description=form.description.data,
        github_url=form.github_url.data,
        site_url=form.site_url.data,
        image_file=form.image_file.data,
    )
    _db.session.add(project)
    _db.session.commit()
    flash("Your project post has been created!", "success")

    return redirect(url_for("project.index"))
