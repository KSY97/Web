from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_socketio import SocketIO

import config

# from app import app

db = SQLAlchemy()
migrate = Migrate()

socket_io = SocketIO()

def create_app():

    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = "pswd"

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    # from . import models
    # from .load_model import load_model

    #소켓통신
    socket_io.init_app(app)

    # 블루프린트
    from .views import main_views, auth_views, record_views, analysis_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(record_views.bp)
    app.register_blueprint(analysis_views.bp)

    # def cos_sim(A, B):
    #     return dot(A, B)/(norm(A)*norm(B))

    # def return_similar_answer(input):
    #     embedding = model.encode(input)
    #     train_data['score'] = train_data.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    #     return train_data.loc[train_data['score'].idxmax()]['A']

    # path = 'C:/Users/AI8_KSY/Desktop/Web/app/'

    # with open(path + 'data.pkl','rb') as f:
    #     df = pickle.load(f)

    # with open(path + 'model.pkl','rb') as f:
    #     model = pickle.load(f)

    # train_data = df.copy()

    
    return app