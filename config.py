import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ksy:!a41096245@127.0.0.1:3306/app'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"