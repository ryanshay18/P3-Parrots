from flask import Blueprint, render_template

lola_blueprint = Blueprint("lola_blueprint", __name__, static_folder="static", template_folder="templates")


@lola_blueprint.route("/lola")
def lola():
    return render_template("lolaminilab1.html")
