from tarfile import RECORDSIZE
from flask import Blueprint, render_template, url_for, flash, request, session, g
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from app import db
from app.forms import UserLoginForm
from app.models import User

from app.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    if g.user:
        return redirect(url_for('main.recode'))
    else:
        return redirect(url_for('main.home'))
@bp.route('/home', methods=('GET', 'POST'))
def home():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('home.html', form=form)

@bp.route('/recode')
def recode():
    if g.user:
        question_list = Question.query.order_by(Question.create_date)
        return render_template('recode.html', question_list=question_list)
    else:
        return redirect(url_for('main.home'))