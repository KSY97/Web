from flask import Blueprint, url_for, render_template, g
from werkzeug.utils import redirect

from app import db
from app.models import Survey

bp = Blueprint('analysis', __name__, url_prefix='/record')


@bp.route('/analysis')
def analysis():
    if g.user:
        surveydb_list = Survey.query.order_by(Survey.create_date)
        survey_list = []
        for survey in surveydb_list:
            if survey.user_id == g.user.id:
                hour = str(survey.create_date.hour)
                min = str(survey.create_date.minute)
                if len(hour) == 1:
                    hour = '0' + str(survey.create_date.hour)
                if len(min) == 1:
                    min = '0' + str(survey.create_date.minute)
                date = str(survey.create_date.year) + '/' + str(survey.create_date.month) + '/' \
                    + str(survey.create_date.day) + ' ' + hour + ':' + min
                survey_list.append([survey.score, date])

        print(date)

        return render_template('analysis.html', survey_list = survey_list, g_user = g.user)
    else:
        return redirect(url_for('main.home'))