from flask import Blueprint, render_template

minilabs = Blueprint("minilabs", __name__, static_folder="static", template_folder="templates")


@minilabs.route("/minilabs")
def minilabs():
    return render_template("minilabs.html")
