from flask import Blueprint, render_template, url_for, g
from werkzeug.utils import redirect

from numpy import dot
from numpy.linalg import norm
import os

from app import db
from app.models import Question, Answer
from app.load_model import model, train_data
from datetime import datetime

from gtts import gTTS
# from vocoding.waveglow.tacotron2.inference_1 import synthesizer
# from scipy.io.wavfile import write
import ftplib

from flask_socketio import send, emit
from app import socket_io


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

        return render_template('record.html',
        question_list=question_list, 
        g_user = g.user)
    else:
        return redirect(url_for('main.home'))


@socket_io.on("message")
def request(message):
    # print("message : ", message)
    to_client = dict()
    if not message == 'new_connect':

        question = Question.query.filter_by(id = message)
        question = question[0]

        contents = question.contents
        hour = str(question.create_date.hour)
        min = str(question.create_date.minute)
        if len(hour) == 1:
            hour = '0'+hour
        if len(min) == 1:
            min = '0'+min
        
        time = hour + ':' + min

        to_client['message'] = contents
        to_client['type'] = 'question'
        to_client['time'] = time
        send(to_client, broadcast = True)

        if not question.answer_set:
            answer = Answer(question = question,
                        contents=return_similar_answer(contents),
                        create_date = datetime.now())
            db.session.add(answer)
            db.session.commit()
        contents = answer.contents
        hour = str(answer.create_date.hour)
        min = str(answer.create_date.minute)
        if len(hour) == 1:
            hour = '0'+hour
        if len(min) == 1:
            min = '0'+min
        
        time = hour + ':' + min

        to_client['message'] = contents
        to_client['type'] = 'answer'
        to_client['time'] = time
        send(to_client, broadcast = True)

        if not answer.ftp_address:
            file_name = 'test_' + str(answer.question_id) + '.mp3'
            tts = gTTS(
                text = answer.contents,
                lang = 'ko', slow = False
            )
            tts.save(file_name)
            # audio, sampling_rate = synthesizer.inference(answer.contents)
            # write(file_name, sampling_rate, audio)

            try:
                # ftp 연결
                with ftplib.FTP() as ftp:
                    ftp.connect(host=host,port=21)
                    ftp.encoding = 'utf-8'
                    ftp.login(user=user,passwd=passwd)
                
                    ftp.cwd('/home')  # 현재 폴더 이동
                
                    # 파일업로드
                    with open(file=file_name, mode='rb') as wf:
                        ftp.storbinary('STOR '+file_name, wf)
                
                    # print(ftp.dir())
                    # print('업로드 완료')
                
            except Exception as e:
                print(e)
            
            else:
                answer.ftp_address = file_name
                db.session.commit()
                # print('db 기록 완료')
                # 파일 삭제
                # if os.path.exists(file_name):
                #     os.remove(file_name)

    emit('response', '응답 완료')