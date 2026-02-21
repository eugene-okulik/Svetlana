import requests
import pytest

from test_meme_api_svetlanagavs.endpoints.authorize import get_token
from test_meme_api_svetlanagavs.endpoints.create_meme import CreateMeme
from test_meme_api_svetlanagavs.endpoints.get_all_memes import GetAllMemes
from test_meme_api_svetlanagavs.endpoints.get_meme import GetMeme
from test_meme_api_svetlanagavs.endpoints.update_meme import UpdateMeme
from test_meme_api_svetlanagavs.endpoints.delete_meme import DeleteMeme

BASE_URL = 'http://memesapi.course.qa-practice.com'


@pytest.fixture(scope='session')
def auth_headers():
    token = get_token()
    return {"Authorization": token}


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def get_all_memes():
    return GetAllMemes()


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def create_and_delete_meme(request, auth_headers, create_meme, delete_meme):
    text, url, tags, info = request.param

    create_meme.create_meme(text, url, tags, info, auth_headers)
    meme_id = create_meme.json['id']

    yield create_meme

    # Try to delete, ignore if already deleted by the test
    response = requests.delete(f'{BASE_URL}/meme/{meme_id}', headers=auth_headers)
