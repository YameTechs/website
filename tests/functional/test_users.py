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
