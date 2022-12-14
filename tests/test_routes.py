from flask.testing import FlaskClient

from src.models import Community
from tests.utils import refresh_db, create_community

<<<<<<< HEAD
=======

>>>>>>> e77c14f99d255543eceea12b58a032b5839b3c6d
def test_get_all_communities(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
<<<<<<< HEAD
    assert f'<a class="text-2xl text-blue-700" href="/community/{test_community.community_name}">Fortnite</a>' in page_data
    assert '<p class="text-white">Super awesome epic game I love Fortnite!</p>' in page_data
=======
    assert f'Fortnite' in page_data
    assert 'Super awesome epic game I love Fortnite!' in page_data

>>>>>>> e77c14f99d255543eceea12b58a032b5839b3c6d

def test_no_communities(test_app: FlaskClient):
    refresh_db()

    response = test_app.get('/communities')
    page_data: str = response.data.decode()

    assert response.status_code == 200
    assert '<a>' not in page_data
<<<<<<< HEAD
    assert '<p>It looks empty, lets make a community!</p>' in page_data

=======
    assert '<p>' not in page_data
>>>>>>> e77c14f99d255543eceea12b58a032b5839b3c6d


def test_get_single_community(test_app: FlaskClient):
    refresh_db()
    test_community = create_community()

    response = test_app.get(f'/community/{test_community.community_name}')
    page_data: str = response.data.decode()

    assert response.status_code == 200
<<<<<<< HEAD
    assert f'<h1 class="text-center text-lg font-bold">{test_community.community_name}</h1>' in page_data
    assert '<button action="submit">Submit</button>' in page_data
    

    
=======
    assert f'{test_community.community_name}' in page_data
    # assert '<button action="submit">Submit</button>' in page_data
>>>>>>> e77c14f99d255543eceea12b58a032b5839b3c6d
