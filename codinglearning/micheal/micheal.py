from flask import Blueprint, render_template

micheal_blueprint = Blueprint("micheal_blueprint", __name__, static_folder="static", template_folder="templates")


@micheal_blueprint.route("/micheal")
def micheal():
    return render_template("michealminilab1.html")
