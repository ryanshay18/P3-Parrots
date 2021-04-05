from flask import Blueprint, render_template

nick_blueprint = Blueprint("nick_blueprint", __name__, static_folder="static", template_folder="templates")


@nick_blueprint.route("/nick")
def nick():
    return render_template("nickminilab1.html")
