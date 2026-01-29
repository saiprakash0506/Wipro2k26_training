# Simple application logic

def register_user(username, password):
    if username and password:
        return "registered"
    return "failed"


def login_user(username, password):
    if username == "sai" and password == "1234":
        return "login success"
    return "login failed"


def test_user_register_and_login():
    # Step 1: Register user
    result = register_user("sai", "1234")
    assert result == "registered"

    # Step 2: Login user
    result = login_user("sai", "1234")
    assert result == "login success"