from flask import Blueprint, flash, redirect, render_template, request, url_for

from src import _db
from src.models import Service
from src.service.forms import ServiceForm
from src.utils import admin_required

service = Blueprint("service", __name__)


@service.route("/services/")
def index():
    services = Service.query.all()
    return render_template("services.html", services=services)


@service.route("/services/<int:service_id>/view")
def view(service_id):
    services = [Service.query.get_or_404(service_id)]
    return render_template("services.html", services=services)


@service.route("/services/<int:service_id>/update/", methods=["GET", "POST"])
@admin_required
def update(service_id):
    form = ServiceForm()
    service = Service.query.get_or_404(service_id)

    if form.validate_on_submit():
        service.title = form.title.data
        service.description = form.description.data
        service.price = form.price.data
        # service.image_file = form.image_file.data
        _db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("service.view", service_id=service_id))
    elif request.method == "GET":
        form.title.data = service.title
        form.description.data = service.description
        form.price.data = service.price
        # form.image_file.data = service.image_file

    return render_template("new_service.html", form=form)


@service.route("/services/<int:service_id>/delete/", methods=["POST"])
@admin_required
def delete(service_id):
    service = Service.query.get_or_404(service_id)
    _db.session.delete(service)
    _db.session.commit()
    flash("Service post has been deleted!", "success")
    return redirect(url_for("service.index"))


@service.route("/services/new/", methods=["GET", "POST"])
@admin_required
def new():
    form = ServiceForm()
    if not form.validate_on_submit():
        return render_template("new_service.html", form=form)

    service = Service(
        title=form.title.data, description=form.description.data, price=form.price.data
    )
    _db.session.add(service)
    _db.session.commit()
    flash("Your post has been created!", "success")

    return redirect(url_for("service.index"))
