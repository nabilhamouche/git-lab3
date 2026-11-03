def login(username, password):
    if not username or not password:
        return False
    return True


def validate_password(password):
    return len(password) >= 8
