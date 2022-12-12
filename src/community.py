from flask import Blueprint, render_template, abort, redirect, url_for, request, session, flash
from src.database.community import community as community_db
from src.database.post import post as post_db
from src.database.account import account as account_db
import datetime

community_blueprint = Blueprint('community', __name__)


@community_blueprint.get('/communities')
def communities():
    all_communities = community_db.get_all_communities()
    return render_template('communities.html', communities=all_communities)


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
        community_db.create_community(name, description)
        return redirect(url_for('community.communities'))

    return render_template('communities.html')

#Name is community name
@community_blueprint.route("/community/<string:name>", methods=['GET', 'POST'])
def community(name):
    
    community_obj = community_db.get_community(name)
    get_all_posts = post_db.get_posts(name)


    return render_template('community.html', community=community_obj, posts=get_all_posts)

# create a post


@community_blueprint.route('/community/<string:name>/post', methods=['GET', 'POST'])
def create_post(name):
    community_obj = community_db.get_community(name)

    if request.method == 'POST' and 'user' in session:
        title = request.form.get('title')
        content = request.form.get('description')
        author = session['user']['username']
        account_id = session['user']['user_id']
        community_id = community_obj.community_id

        if title == '' or content == '' or 'user' not in session:
            abort(400)
        post_db.create_post(
            title, author, content, community_id, account_id)
        return redirect(url_for('community.community', name=name))
    else: 
        redirect('/login')

    return render_template('create.html', community=community_obj)



@community_blueprint.route('/community/<string:name>/<int:post_id>', methods=['GET', 'POST'])
def get_specific_post(name, post_id): 

    return render_template('post.html')
