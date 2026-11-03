def login(username, password):
    if not username or not username.strip() or not password:
        return False
    return True


def validate_password(password):
    return len(password) >= 8
