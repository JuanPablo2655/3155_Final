from src.models import Game, Account
from flask import request
from src.models import db
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

class Gaming_Repository:
    #Get the methods from the repository and then put them into the app.py file
    def create_user_account(self, user_name, full_name, gaming_password, email): 
        new_account = Account(user_name = user_name, full_name = full_name, gaming_password = gaming_password, email = email)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def check_username(self, user_name): 
        user_object = Account.query.filter_by(user_name=user_name).first()
        return user_object
    
    def check_email(self, email): 
        email_object = Account.query.filter_by(email=email).first() 
        return email_object
    
    def get_password(self, password): 
        #fix this as this is returning an id instead of the password
        passw = Account.query.get(password)
        return passw

    def get_user_id(self, id): 
        user_id = Account.query.get(id)
        return user_id

#use in other modules
gaming_repository_singleton = Gaming_Repository()
