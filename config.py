import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:6245@127.0.0.1:3306/app'
# 'mysql+pymysql://root:6245@127.0.0.1:3306/pybo'.format(os.path.join(BASE_DIR, 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"