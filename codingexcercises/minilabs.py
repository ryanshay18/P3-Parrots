from flask import Blueprint, render_template

minilabs_blueprint = Blueprint("minilabs", __name__, static_folder="static", template_folder="templates")


@minilabs_blueprint.route("/minilabs")
def minilabs():
    return render_template("minilabs.html")
