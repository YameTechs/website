def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"login" in response.data
    assert b"register" in response.data


def test_home_page_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/")
    assert response.status_code == 405


def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/register/")
    assert response.status_code == 200
    assert b"register" in response.data

    assert b"username" in response.data
    assert b"email" in response.data
    assert b"password" in response.data
    assert b"confirm" in response.data


def test_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/login/")
    assert response.status_code == 200
    assert b"login" in response.data

    assert b"email" in response.data
    assert b"password" in response.data
