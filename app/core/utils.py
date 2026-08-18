from ..config import settings
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib import PasswordHash

pwd_context = PasswordHash((Argon2Hasher(),))

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)


