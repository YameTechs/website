from src.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password, and username are defined correctly
    """
    email = "deez.nuts@test.com"
    password = "password"
    username = "deeznuts"

    user = User(email=email, password=password, username=username)

    assert user.email == email
    assert user.password == password
    assert user.username == username
