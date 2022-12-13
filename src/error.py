from flask import Blueprint, render_template

error = Blueprint('errors', __name__)

@error.app_errorhandler(404)
def not_found(e): 
    return render_template('404.html'), 404

@error.app_errorhandler(500)
def page_not_found(e): 
    return render_template('500.html'), 500

@error.app_errorhandler(400)
def page_not_found(e): 
    return render_template('400.html'), 400

    
