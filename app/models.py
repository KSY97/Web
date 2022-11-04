from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.String(11), unique=True, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('question_set'))
    contents = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    contents = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# class QandA(db.Model):
#     question_id = db.Column(db.Integer, db.ForeignKey('answer.question_id', ondelete='CASCADE'), primary_key=True)
#     answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'))
#     user_id = db.Column(db.Integer, db.ForeignKey('question.user_id', ondelete='CASCADE'))
    
