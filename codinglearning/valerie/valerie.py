from flask import Blueprint, render_template

valerie_blueprint = Blueprint("valerie_blueprint", __name__, static_folder="static", template_folder="templates")


@valerie_blueprint.route("/valerie")
def valerie():
    return render_template("lolaminilab1.html")
