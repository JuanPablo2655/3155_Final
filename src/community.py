from flask import Blueprint, render_template, abort, redirect, url_for, request, session, flash
from src.database.community import community as community_db
from src.database.post import post as post_db
from src.database.account import account as account_db
from src.database.comment import comment as comment_db

community_blueprint = Blueprint('community', __name__)


@community_blueprint.get('/communities')
def communities():
    all_communities = community_db.get_all_communities()
    return render_template('communities.html', communities=all_communities)


@community_blueprint.route('/community/form', methods=['GET', 'POST'])
def create_community_form():
    if 'user' not in session: 
        return redirect('/login')
    else: 
        return render_template('create_community.html')


@community_blueprint.route('/community/create', methods=['GET', 'POST'])
def create_community():
    if request.method == 'POST':
        name = str(request.form.get('name')).strip()
        description = request.form.get('description')
        community_object = community_db.check_community(name)
        account_id = session['user']['user_id']

        if community_object:
            flash("This communtity already exists", category='error')
            return redirect('/communities')
        else:
            if name == '' or description == '':
                abort(400)
        community_db.create_community(name, description, account_id)
        return redirect(url_for('community.communities'))
    else:
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

    if 'user' not in session: 
        return redirect('/login')
    
    if request.method == 'POST' and 'user' in session:
        title = request.form.get('title')
        content = request.form.get('description')
        author = session['user']['username']
        account_id = session['user']['user_id']
        community_name = name
        community_id = community_obj.community_id

        if title == '' or content == '' or 'user' not in session:
            abort(400)
        post_db.create_post(
            title, author, content, community_name, account_id, community_id)
        return redirect(url_for('community.community', name=name))

    return render_template('create.html', community=community_obj)

@community_blueprint.post('/community/<string:name>/<int:post_id>/delete')
def delete_post(post_id, name): 
    if 'user' not in session: 
        return redirect('/login')
    else: 
        post = post_db.get_post(post_id)
        if post: 
            if post.account_id != session['user']['user_id']: 
                return redirect(url_for('community.get_specific_post', name=post.community_name, post_id=post.post_id))
            post_db.delete_post(post)
            flash("Successfully deleted post.", "success")
            return redirect('/')
        else: 
            abort(404)

@community_blueprint.route('/community/<string:name>/<int:post_id>', methods=['GET'])
def get_specific_post(name, post_id): 
    community_obj = community_db.get_community(name)
    post = post_db.get_post(post_id)
    if name != post.community_name:
        abort(400, 'Bad request')
    else: 
        get_all_comments = comment_db.get_all_comment_from_post(post_id)
    
    return render_template('post.html', community=community_obj, post=post, comments=get_all_comments)

@community_blueprint.route('/community/<string:name>/<int:post_id>', methods=['POST'])
def create_comment(name, post_id): 
    post_obj = post_db.get_post(post_id)
    community_obj = community_db.get_community(name)

    if request.method == 'POST' and 'user' in session: 
        content = request.form.get('description')
        author = session['user']['username']
        post_id = post_obj.post_id
        account_id = session['user']['user_id']
        new_comment = comment_db.create_new_comment(author, content, post_id, account_id)
        return redirect(f'/community/{community_obj.community_name}/{post_id}')
    else: 
        return redirect('/login')

@community_blueprint.route('/community/<string:name>/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(name, post_id): 
    if 'user' not in session: 
        redirect('/login')
    else: 
        post = post_db.get_post(post_id)
        if request.method == 'POST' and 'user' in session and post.account_id == session['user']['user_id']: 
            title = request.form.get('title')
            content = request.form.get('content')
            post_db.update_post(post, title, content)
            return redirect(url_for('community.get_specific_post', name=name, post_id=post_id))
    return render_template('edit_post.html', post=post)

@community_blueprint.post('/community/<string:name>/<int:post_id>/comment/<int:comment_id>/delete')
def delete_comment(name, post_id, comment_id): 
    post = post_db.get_post(post_id)
    if 'user' not in session: 
        return redirect('/login')
    else: 
        comment = comment_db.get_comment(comment_id)
    if comment: 
        if comment.account_id != session['user']['user_id']:
            return redirect(url_for('community.get_specific_post', name=post.community_name, post_id=post.post_id))
        comment_db.delete_comment(comment)
        flash("Successfully deleted post.", "success")
        return redirect(f'/community/{post.community_name}/{post_id}')
    else: 
        abort(404)

@community_blueprint.route('/community/<string:name>/<int:post_id>/comment/<int:comment_id>/edit', methods=['GET', 'POST'])
def edit_comment(name, post_id, comment_id): 
    post = post_db.get_post(post_id)
    if 'user' not in session: 
        redirect('/login')
    else: 
        comment = comment_db.get_comment(comment_id)
        if request.method == 'POST' and 'user' in session and comment.account_id == session['user']['user_id']: 
            content = request.form.get('content')
            comment_db.update_comment(comment, content)
            return redirect(url_for('community.get_specific_post', name=name, post_id=comment.post_id))
    return render_template('edit_comment.html', comment=comment, post=post)

@community_blueprint.route('/community/<string:name>/edit', methods=['GET', 'POST'])
def edit_community(name): 
    community=community_db.check_community(name)
    if 'user' not in session: 
        redirect('/login')
    else: 
        community=community_db.check_community(name)
        if request.method == 'POST' and 'user' in session and community.account_id == session['user']['user_id']: 
            description = request.form.get('description')
            community_db.update_community(community, description)
            return redirect('/communities')
    return render_template('edit_community.html', community=community)

@community_blueprint.post('/community/<string:name>/delete')
def delete_community(name):
    if 'user' not in session: 
        return redirect('/login')
    else: 
        community = community_db.check_community(name) 
    if community: 
        if community.account_id != session['user']['user_id']: 
            return redirect('/communities')
        community_db.delete_community(community)
        return redirect('/communities')



    