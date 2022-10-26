from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")

# COMMUNITY POSTS / FEED
@app.get("/community")
def community():
    return None

# USER PROFILE
@app.get("/user")
def user():
    return None