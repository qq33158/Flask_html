import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object): # Flask應用程式的設定
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-guess-what'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://user_name:password@IP:3306/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
