from app.core.utils import hash_password
from security.logger import logger


def get_user_by_username(cur, username: str):
    cur.execute('''
        SELECT user_id from users 
        WHERE username = %s
    ''', (username,))
    registered = cur.fetchone()
    return registered

def get_user_by_id(cur, user_id: str):
    cur.execute('''
        SELECT user_id from users 
        WHERE user_id = %s
    ''', (user_id,))
    registered = cur.fetchone()
    return registered


def create_user(cur, username: str, password: str):
    hashed_password = hash_password(password)
    cur.executemany('''
        INSERT INTO users (username, password)
        values (%s, %s)
    ''', ((username, hashed_password),))
