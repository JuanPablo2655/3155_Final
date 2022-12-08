from flask import Blueprint, render_template, abort, redirect, url_for, request
from src.database.community import community as community_db

community_blueprint = Blueprint('community', __name__)


@community_blueprint.get('/communities')
def communities():
    all_communities = community_db.get_all_communities()
    return render_template('communities.html', communities = all_communities)

@community_blueprint.route('/community/form', methods=['GET', 'POST'])
def create_community_form():
    return render_template('create_community.html')

@community_blueprint.route('/community/create', methods=['GET', 'POST'])
def create_community():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        if name == '' or description == '':
            abort(400)
        new_community = community_db.create_community(name, description)
        return redirect(url_for('community.communities'), name=name)

    return render_template('communities.html')
    


@community_blueprint.route("/community/<string:name>", methods=['GET', 'POST'])
def community(name):
    community_obj = community_db.get_community(name)
    return render_template('community.html', community=community_obj)

# create a post


@community_blueprint.get('/community/post')
def create_post():
    return render_template('create.html')
