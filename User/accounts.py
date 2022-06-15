from flask import Blueprint, render_template

bp = Blueprint('registration', __name__, url_prefix='/templates')

@bp.route('/<id>')
def register(id):
    return render_template('templates/registration.html')