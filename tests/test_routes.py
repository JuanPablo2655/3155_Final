from flask.testing import FlaskClient

from src.models import Community
from tests.utils import refresh_db, create_community, create_user, create_post

def test_get_all_communities(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' in page_data
    assert 'Super awesome epic game I love Fortnite!' in page_data


def test_no_communities(test_app: FlaskClient):
    refresh_db()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' not in page_data


def test_get_single_community(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get(f'/community/{test_community.community_name}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' in page_data

def test_get_post(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()
    test_user = create_user()
    test_post = create_post(community_id=test_community.community_id, account_id=test_user.account_id)

    response = test_app.get(f'/community/{test_community.community_name}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert 'Fortnite' in page_data
    assert 'xxflash' in page_data
    assert 'I love this season' in page_data

def get_no_posts(test_app: FlaskClient):
    test_community = create_community()
    test_user = create_user()

    response = test_app.get(f'/community/{test_community.community_name}')
    page_data: str = response.data.decode()

    assert 'Fortnite' not in page_data
    assert 'xxflash' not in page_data
    assert 'I love this season' in page_data

