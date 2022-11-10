from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
     gaming_id = db.column(db.Integer, primary_key=True)
     title = db.column(db.String, nullable=True)
     genre = db.column(db.String, nullable=True)

class Account(db.Model): 
    account_id = db.column(db.Integer, primary_key=True)
    user_name = db.column(db.String, nullable=True)
    first_name = db.column(db.String, nullable=True)
    last_name = db.column(db.String, nullable=True)
    password = db.column(db.String, nullable=True)
    email = db.column(db.String, nullable=True)

class Community(db.Model): 
     className_id = db.column(db.Integer, primary_key=True)
     name = db.column(db.String, nullable=True)

