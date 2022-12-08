from flask import Flask, render_template, session
from src.models import db
from src.config import postgres_uri, secret_key
from src.security import bcrypt
from src.authentication import auth
from src.community import community_blueprint as community

from src.database.account import account

app = Flask(__name__)
app.secret_key = secret_key

# Get The database DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(community)


@app.get("/")
def index():
    return render_template("index.html")


@app.get('/about')
def about():
    return render_template("about.html")


# USER PROFILE


@app.route("/user")
def user():
    id = session['user']['user_id']
    user_account = account.get_user_id(id) 
    return render_template('user.html', user_account=user_account)
