from constants import UserConstants as UC


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password, and username are defined correctly
    """
    assert new_user.email == UC.EMAIL
    assert new_user.password == UC.PASSWORD
    assert new_user.username == UC.USERNAME
