from flaskr import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Artical(db.Model):
    __tablename__ = 'artical_p'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    time = db.Column(db.String(15))
    preview = db.Column(db.String(255))

class ArticalContent(db.Model):
    __tablename__ = 'artical_c'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text)

class ArticalLabel(db.Model):
    __tablename__ = 'artical_l'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artical_id = db.Column(db.Integer)
    label_id = db.Column(db.Integer)

class Label(db.Model):
    __tablename__ = 'label'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    number = db.Column(db.Integer)

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(128))

    def setPassword(self, password):
        self.password = generate_password_hash(password)
    
    def checkPassword(self, password):
        return check_password_hash(self.password, password)