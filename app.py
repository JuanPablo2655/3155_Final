from flask import Flask, render_template
from src.models import db
from src.config import postgres_uri, secret_key
from src.security import bcrypt
from src.authentication import auth

from src.database.account import account

app = Flask(__name__)
app.secret_key = secret_key

# Get The database DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth)


@app.get("/")
def index():
    return render_template("index.html")


@app.get('/about')
def about():
    return render_template("about.html")


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         user_name = request.form['username']
#         password = request.form['password']
#         username_object = account.check_username(user_name)

#         if username_object:
#             if bcrypt.check_password_hash(username_object.gaming_password, password):
#                 flash('logged in successfully.', category='success')
#                 session['user'] = {
#                     'user_id': username_object.account_id
#                 }
#                 return redirect(url_for('index'))
#             else:
#                 flash('Incorrect password, please try again.', category='error')
#         else:
#             flash('Username does not exist', category='error')

#         # Make sure the username and password is what it's supposed to. DELETE in the final product.
#         print(user_name)
#         print(password)

#     return render_template("login.html")


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if 'user' in session:
#         flash('already logged in', category='error')
#         return redirect('/')
#     else:
#         if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#             fullname = request.form.get('fullname')
#             email = request.form.get('email')
#             user_name = request.form.get('username')
#             password = request.form.get('password')

#             # salt and hash the password
#             hashed_bytes = bcrypt.generate_password_hash(
#                 password, bcrypt_rounds)
#             hashed_password = hashed_bytes.decode('utf-8')

#             # Check for different conditions, such as if the database has an email/username registered. If not, then make account.
#             if account.check_username(user_name):
#                 flash("Someone has this username", category='error')
#             elif account.check_email(email):
#                 flash("Someone has taken this email", category='error')
#             else:
#                 flash("Registered Successfully!")
#                 new_account = account.create_user_account(
#                     user_name, fullname, hashed_password, email)
#                 # Make sure everything is here. DELETE in the final product.
#                 print(fullname)
#                 print(email)
#                 print(user_name)
#                 print(password)
#                 return render_template("register.html")
#         return render_template("register.html")


# @app.post('/logout')
# def logout():
#     session.pop('user')
#     return redirect('/')


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
