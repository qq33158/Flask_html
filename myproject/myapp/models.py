# User database model
from myapp import db

class MLTrain(db.Model): # db.Model是SQLAlchemy的功能
    __tablename__ = 'mltrain' # SQLAlchemy定義的內部變數(__tablename__)
    id = db.Column(db.Integer, primary_key=True) # 自動編號
    model = db.Column(db.String(10), 
            index=True, unique=True)
    weight1 = db.Column(db.Float())
    weight2 = db.Column(db.Float())

    def __repr__(self): # 相當於Java的toString()
        return f'<Model:{self.model},weight1:{self.weight1},weight2:{self.weight2}>'
