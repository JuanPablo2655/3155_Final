from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    gaming_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    genre = db.Column(db.String, nullable=True)

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre


communities = db.Table('account_community',
                       db.Column('community_id', db.Integer, db.ForeignKey(
                           'community.community_id'), primary_key=True),
                       db.Column('account_id', db.Integer, db.ForeignKey(
                           'account.account_id'), primary_key=True),
                       )


class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    gaming_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    # one to many relationship. Represents all of the posts that the author has made.
    posts = db.relationship('Post', backref='account', lazy=True)
    # One to many relationship. Represents all of the comments that the author has made.
    comments = db.relationship('Comment', backref='account', lazy=True)
    # Makes a subquery to the Community Table and then makes all of the posts regarding to that community
    communities = db.relationship('Community', secondary=communities, lazy='subquery',
                                  backref=db.backref('accounts', lazy=True))

    def __init__(self, user_name, full_name, gaming_password, email):
        self.user_name = user_name
        self.full_name = full_name
        self.gaming_password = gaming_password
        self.email = email


class Community(db.Model):
    community_id = db.Column(db.Integer, primary_key=True)
    community_name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    # Needs a user id
    # Many posts belong to a single community
    posts = db.relationship('Post', backref='community', lazy=True)

    def __init__(self, community_name, description):
        self.community_name = community_name
        self.description = description


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.String, nullable=False)
    votes = db.Column(db.Integer, nullable=False)
    # references the foreign key of the account id. In other words, who it belongs to
    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.account_id'), nullable=False)
    # All the comments on this one post.
    comments = db.relationship('Comment', backref='post', lazy=True)
    # Where the post belongs to in the community.
    community_id = db.Column(db.Integer, db.ForeignKey(
        'community.community_id'), nullable=False)

    def __init__(self, title, author, content, date_posted, votes):
        self.title = title
        self.author = author
        self.content = content
        self.date_posted = date_posted
        self.votes = votes


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.String, nullable=False)
    votes = db.Column(db.Integer, nullable=False)
    # The post_id of the comment. Where the comment belongs to.
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.post_id'), nullable=False)
    # The account_id of the comment. Who the comment belongs to.
    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.account_id'), nullable=False)

    def __init__(self, title: str, author: str, content: str, date_posted: str, votes: str):
        self.title = title
        self.author = author
        self.content = content
        self.date_posted = date_posted
        self.votes = votes
