from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
     gaming_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=True)
     genre = db.Column(db.String, nullable=True)


communities = db.Table('communities', 
     db.Column('community_id', db.Integer, db.ForeignKey('community.community_id'), primary_key=True),
     db.Column('account_id', db.Integer, db.ForeignKey('account.account_id'), primary_key=True),
)


class Account(db.Model): 
    account_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    gaming_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    #one to many relationship. Represents all of the posts that the author has made. 
    posts = db.relationship('Post', backref='account', lazy=True)
    #One to many relationship. Represents all of the comments that the author has made. 
    comments = db.relationship('Comment', backref='account', lazy=True)
    #Makes a subquery to the Community Table and then makes all of the posts regarding to that community
    communities = db.relationship('Community', secondary=communities, lazy='subquery', 
          backref=db.backref('accounts', lazy=True))


class Community(db.Model): 
     community_id = db.Column(db.Integer, primary_key=True)
     community_name = db.Column(db.String, nullable=True)
     #Many posts belong to a single community
     posts = db.relationship('Post', backref='community' ,lazy=True)


class Post(db.Model): 
     post_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=False)
     author = db.Column(db.String, nullable=False)
     content = db.Column(db.String, nullable=False)
     date_posted = db.Column(db.String, nullable=False)
     #references the foreign key of the account id. In other words, who it belongs to
     account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)
     #All the comments on this one post. 
     comments = db.relationship('Comment', backref='post', lazy=True)
     #Where the post belongs to in the community. 
     community_id = db.Column(db.Integer, db.ForeignKey('community.community_id'), nullable=False)


class Comment(db.Model): 
     comment_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=False)
     author = db.Column(db.String, nullable=False)
     content = db.Column(db.String, nullable=False)
     #The post_id of the comment. Where the comment belongs to. 
     post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
     #The account_id of the comment. Who the comment belongs to. 
     account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)





