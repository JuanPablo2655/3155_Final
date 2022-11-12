from flask import Flask, render_template, session, redirect, url_for, request, abort, flash
import psycopg2
import psycopg2.extras
from src.models import db, Account
from werkzeug.security import generate_password_hash

from src.repositories.gaming_repository import gaming_repository_singleton

app = Flask(__name__)
app.secret_key = 'super-secret-key'


#Get The database DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:abc123@localhost:5432/user'

db.init_app(app)

connection = psycopg2.connect(host='localhost', user='postgres', password='abc123', database='user')
cursor = connection.cursor()



@app.get("/")
def index():
    return render_template("index.html")


@app.get('/about')
def about():
    return render_template("about.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form: 
        fullname = request.form['fullname']
        email = request.form['email']
        user_name = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        #Check for different conditions, such as if the database has an email/username registered. If not, then make account.
        if gaming_repository_singleton.check_username(user_name): 
            return "Someone has this username"
        elif gaming_repository_singleton.check_email(email): 
            return "Someone already registered with this email"
        else: 
            new_account = gaming_repository_singleton.create_user_account(user_name, fullname, hashed_password, email)
            #Make sure everything is here. DELETE in the final product. 
            print(fullname)
            print(email)
            print(user_name)
            print(password)
            return render_template("register.html")
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
