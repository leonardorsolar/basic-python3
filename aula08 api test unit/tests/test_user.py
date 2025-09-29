from domain.user import User

def test_create_user():
    user = User("leo", "leo@gmail.com")
    assert user.username == "leo"
    assert user.email == "leo@gmail.com"