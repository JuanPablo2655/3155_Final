from src.models import db, Account as AccountModel


class Account:
    def create_user_account(self, user_name: str, full_name: str, gaming_password: str, email: str):
        """
        Create an account and put it in the database.
        """
        new_account = AccountModel(
            user_name, full_name, gaming_password, email)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def check_username(self, user_name):
        """
        Check the account by it's user_name.
        """
        user_object = AccountModel.query.filter_by(user_name=user_name).first()
        return user_object

    def check_by_id(self, id): 
        """
        Check the account by its account_id
        """
        user_object = Account.query.filter_by(account_id=id).first()
        return user_object
        
    def check_email(self, email):
        """
        Check the username by email. 
        """
        email_object = AccountModel.query.filter_by(email=email).first()
        return email_object

    def get_user_id(self, id):
        """
        Get the user
        """
        user_id = AccountModel.query.get(id)
        return user_id


account = Account()
