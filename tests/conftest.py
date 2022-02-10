import pytest
from constants import UserConstants as UC

from src import create_app
from src.models import User


@pytest.fixture(scope="module")
def new_user():
    return User(username=UC.USERNAME, email=UC.EMAIL, password=UC.PASSWORD)


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    with flask_app.test_client() as testing_client:
        yield testing_client
