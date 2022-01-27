from src import create_app
from src.config import Config


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app(Config)

    with flask_app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200


def test_home_page_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted (POST)
    THEN check that a '405' status code is returned
    """
    flask_app = create_app(Config)

    with flask_app.test_client() as test_client:
        response = test_client.post("/")
        assert response.status_code == 405
