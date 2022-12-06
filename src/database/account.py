from src.models import db, Account as AccountModel


class Account:
    # Get the methods from the repository and then put them into the app.py file
    def create_user_account(self, user_name: str, full_name: str, gaming_password: str, email: str):
        new_account = AccountModel(
            user_name, full_name, gaming_password, email)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def check_username(self, user_name):
        user_object = AccountModel.query.filter_by(user_name=user_name).first()
        return user_object

    def check_by_id(self, id): 
        user_object = Account.query.filter_by(account_id=id).first()
        return user_object
        
    def check_email(self, email):
        email_object = AccountModel.query.filter_by(email=email).first()
        return email_object

    def get_password(self, password):
        # fix this as this is returning an id instead of the password
        passw = AccountModel.query.get(password)
        return passw

    def get_user_id(self, id):
        user_id = AccountModel.query.get(id)
        return user_id


account = Account()
