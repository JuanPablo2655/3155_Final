from flask import Blueprint, render_template

community_blueprint = Blueprint('community', __name__)


@community_blueprint.get('/communities')
def communities():
    return render_template('communities.html')


@community_blueprint.route('/community/create', methods=['GET', 'POST'])
def create_community():

    return render_template('create_community.html')


@community_blueprint.route("/community", methods=['GET', 'POST'])
def community():
    return render_template('community.html')

# create a post


@community_blueprint.get('/community/post')
def create_post():
    return render_template('create.html')
