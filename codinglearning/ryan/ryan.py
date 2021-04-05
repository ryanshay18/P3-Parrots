from flask import Blueprint, render_template

ryan_blueprint = Blueprint("ryan_blueprint", __name__, static_folder="static", template_folder="templates")


@ryan_blueprint.route("/ryan")
def ryan():
    return render_template("ryanminilab1.html")
