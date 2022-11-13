from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
     gaming_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=True)
     genre = db.Column(db.String, nullable=True)

class Account(db.Model): 
    account_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    gaming_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

class Community(db.Model): 
     community_id = db.Column(db.Integer, primary_key=True)
     community_name = db.Column(db.String, nullable=True)

#Posts and comments represent a many to many relationship. Include the table soon. 
class Post(db.Model): 
     post_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=False)
     author = db.Column(db.String, nullable=False)
     content = db.Column(db.String, nullable=False)
     #comment = db.relationship('Comment', secondary='', backref='Post')


class Comment(db.Model): 
     className_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=False)
     author = db.Column(db.String, nullable=False)
     content = db.Column(db.String, nullable=False)
     #post = db.relationship('Post', secondary='', backref='Comment')





