from flask.testing import FlaskClient

from src.models import Community
from tests.utils import refresh_db, create_community, create_user, create_post, create_comment

#Tests communities page
def test_get_all_communities(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' in page_data
    assert 'Super awesome epic game I love Fortnite!' in page_data

#Tests communities page with no entries
def test_no_communities(test_app: FlaskClient):
    refresh_db()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' not in page_data

#Tests getting a community page
def test_get_single_community(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get(f'/community/{test_community.slug}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' in page_data

#Tests a community page with a post
def test_get_post(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()
    test_user = create_user()
    test_post = create_post(community_id=test_community.community_id, account_id=test_user.account_id)

    response = test_app.get(f'/community/{test_community.slug}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' in page_data
    assert 'xxflash' in page_data
    assert 'I love this season' in page_data

#Tests a community page with no posts
def get_no_posts(test_app: FlaskClient):
    test_community = create_community()
    test_user = create_user()

    response = test_app.get(f'/community/{test_community.slug}')
    page_data: str = response.data.decode()

    #Makes sure there it's in the right community
    assert 'Fortnite' not in page_data
    #Check rights user made the comment
    assert 'xxflash' not in page_data
    #Checks to make sure the post has the right content
    assert 'I love this season' in page_data

#Tests getting a single post with comments
def test_get_comment(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()
    test_user_1 = create_user()
    #Two users are created so there is a distinction between the post author and the comment author
    test_user2 = create_user(user_name='fortnite_haterxx', full_name= 'Mr Hater', gaming_password='IH8FORTNITE', email='ihfn@gmail.com')
    test_post = create_post(community_id=test_community.community_id, account_id=test_user_1.account_id)
    test_comment = create_comment(author = test_user2.user_name, post_id=test_post.post_id, account_id= test_user2.account_id)

    response = test_app.get(f'/community/{test_community.slug}/{test_post.post_id}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    #Makes sure it's the right communitity
    assert 'Fortnite' in page_data
    #Makes sure the user who had the post is there
    assert 'xxflash' in page_data
    #Makes sure post content is there
    assert 'I love this season' in page_data
    #Makes sure comment from a different user is there
    assert 'fortnite_haterxx' in page_data
    #Makes sure the comment content is there
    assert 'I do not agree sir...' in page_data
