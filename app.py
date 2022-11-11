from flask import Flask, render_template, session, redirect, url_for, request
import psycopg2
import psycopg2.extras
from src.models import db

app = Flask(__name__)

#Get The database DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:abc123@localhost:5432/user'

db.init_app(app)


@app.get("/")
def index():
    return render_template("index.html")


@app.get('/about')
def about():
    return render_template("about.html")


@app.get('/login')
def login():

    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form: 
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        print(fullname)
        print(email)
        print(username)
        print(password)
    return render_template("register.html")


@app.get('/create')
def create():
    return render_template("create.html")

# COMMUNITY POSTS / FEED


@app.get("/community")
def community():
    return None

# USER PROFILE


@app.get("/user")
def user():
    return None
