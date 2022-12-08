from flask import Blueprint, render_template, abort, redirect, request
from src.database.community import community as community_db

community_blueprint = Blueprint('community', __name__)


@community_blueprint.get('/communities')
def communities():
    all_communities = community_db.get_all_communities()
    return render_template('communities.html', communities = all_communities)


@community_blueprint.route('/community/create', methods=['GET', 'POST'])
def create_community():
    name = request.form.get('name', '')
    description = request.form.get('description', '')
    if name == '' or description == '':
        abort(400)
    new_community = community_db.create_community(name, description)
    return redirect(f'/communities/{new_community.community_id}')


@community_blueprint.route("/community", methods=['GET', 'POST'])
def community():
    return render_template('community.html')

# create a post


@community_blueprint.get('/community/post')
def create_post():
    return render_template('create.html')
