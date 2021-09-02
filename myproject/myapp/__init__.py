# Flask application instance
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)             # __name__ = myapp; 以目錄來建立
app.config.from_object(Config)    # 抓config.py設定
db = SQLAlchemy(app)              # 產生app的database
from myapp import routes, models  # 從myapp的module匯入routes功能; 資料庫的models

