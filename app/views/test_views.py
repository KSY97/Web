from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('main.home'))
@bp.route('/home')
def home():
    return render_template('HTML_test1.html')
@bp.route('/notice')
def notice():
    return render_template('HTML_test2.html')
@bp.route('/introduce')
def introduce():
    return render_template('HTML_test3.html')
@bp.route('/free')
def free():
    return render_template('HTML_test4.html')
