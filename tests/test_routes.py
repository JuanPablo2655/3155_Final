from flask.testing import FlaskClient

from src.models import Community
from tests.utils import refresh_db, create_community


def test_get_all_communities(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert f'Fortnite' in page_data
    assert 'Super awesome epic game I love Fortnite!' in page_data


def test_no_communities(test_app: FlaskClient):
    refresh_db()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert '<a>' not in page_data
    assert '<p>' not in page_data


def test_get_single_community(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get(f'/community/{test_community.community_name}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert f'{test_community.community_name}' in page_data
    assert '<button action="submit">Submit</button>' in page_data
