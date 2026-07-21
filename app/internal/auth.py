from app.core.utils import verify_password, hash_password


def verify_user(cur, username: str, password: str):
    cur.execute('SELECT password FROM users WHERE username = %s', (username,))
    hashed = cur.fetchone()[0]
    verified = verify_password(password, hashed)
    return verified

