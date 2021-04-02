from flask import Blueprint, render_template

from codingexercises.pigeon import Pigeon

codingexercises_pigeon_bp = Blueprint('codingexercises_pigeon', __name__,
                                      template_folder='templates',
                                      static_folder='static', static_url_path='assets')


@codingexercises_pigeon_bp.route('/')
def index():
    return render_template("pigeon.html", pigeon=Pigeon(200))
