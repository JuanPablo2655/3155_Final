from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
     gaming_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=True)
     genre = db.Column(db.String, nullable=True)

class Account(db.Model): 
    account_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    gaming_password = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)

class Community(db.Model): 
     className_id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=True)

