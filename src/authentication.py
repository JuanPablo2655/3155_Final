from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from src.security import bcrypt
from src.config import bcrypt_rounds

from src.database.account import account

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session: 
        return redirect('/')
    else: 
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            user_name = request.form.get('username')
            password = request.form.get('password')
            username_object = account.check_username(user_name)

            if username_object:
                if bcrypt.check_password_hash(username_object.gaming_password, password):
                    flash('logged in successfully.', category='success')
                    session['user'] = {
                        'user_id': username_object.account_id,
                        'user_email': username_object.email,
                        'user_name': username_object.full_name,
                        'username': username_object.user_name

                    }
                    return redirect(url_for('index'))
                else:
                    #flash('Incorrect password, please try again.', category='error')
                    redirect('/login')
            else:
                #flash('Username does not exist', category='error')
                redirect('/login')

            # Make sure the username and password is what it's supposed to. DELETE in the final product.
            print(user_name)
            print(password)

        return render_template("login.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    if 'user' in session:
        flash('already logged in', category='error')
        return redirect('/')
    else: 
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'confirm_password' in request.form:
            fullname = request.form.get('fullname')
            email = request.form.get('email')
            user_name = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            # salt and hash the password

            # Check for different conditions, such as if the database has an email/username registered. If not, then make account.
            if account.check_username(user_name):
                return redirect('/register')
            elif account.check_email(email):
                return redirect('/register')
            elif password != confirm_password:
                return redirect('/register')
            else:
                hashed_bytes = bcrypt.generate_password_hash(
                    password, bcrypt_rounds)
                hashed_password = hashed_bytes.decode('utf-8')
                new_account = account.create_user_account(
                    user_name, fullname, hashed_password, email)
                return render_template("login.html")
    return render_template("register.html")


@auth.get('/logout')
def logout():
    if 'user' not in session: 
        return redirect('/login')
    else: 
        session.pop('user')
        return redirect('/')
