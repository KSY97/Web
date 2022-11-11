from flask import Blueprint, render_template, url_for, g
from werkzeug.utils import redirect

from numpy import dot
from numpy.linalg import norm

from app import db
from app.models import Question, Answer, User
from app.load_model import model, train_data
from datetime import datetime

from gtts import gTTS
import ftplib

# ftp 정보
host = '192.168.3.46'
user = 'voco-test1'
passwd = 'etevers1123!!'

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

def return_similar_answer(input):
    embedding = model.encode(input)
    train_data['score'] = train_data.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    return train_data.loc[train_data['score'].idxmax()]['A']

bp = Blueprint('record', __name__, url_prefix='/record')

@bp.route('/')
def record():
    if g.user:
        question_list = Question.query.order_by(Question.create_date)
        answer_list = Answer.query.order_by(Answer.create_date)
                
        for question in question_list:
            # answer = Answer.query.filter_by(username=form.username.data).first()
            if not question.answer_set:            
                answer = Answer(question = question,
                            contents=return_similar_answer(question.contents),
                            create_date = datetime.now())
                db.session.add(answer)
                db.session.commit()

        for answer in answer_list:
            if not answer.ftp_address:
                file_name = 'test_' + str(answer.question_id) + '.mp3'
                tts = gTTS(
                    text = answer.contents,
                    lang = 'ko', slow = False
                )
                tts.save(file_name)

                uploadFile = file_name

                try:
                    # ftp 연결
                    with ftplib.FTP() as ftp:
                        ftp.connect(host=host,port=21)
                        ftp.encoding = 'utf-8'
                        ftp.login(user=user,passwd=passwd)
                    
                        ftp.cwd('/home')  # 현재 폴더 이동
                    
                        # 파일업로드
                        with open(file=uploadFile, mode='rb') as wf:
                            ftp.storbinary('STOR '+file_name, wf)
                    
                        print(ftp.dir())
                    
                except Exception as e:
                    print(e)
                
                else:
                    answer.ftp_address = file_name
                    db.session.commit()
                    print('생성완료')
        return render_template('record.html',
        question_list=question_list, 
        g_user = g.user)
    else:
        return redirect(url_for('main.home'))