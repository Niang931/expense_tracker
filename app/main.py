from fastapi import FastAPI
from app.auth import users
from app.routers import expenses
import os
from dotenv import load_dotenv
from app.models import UserDB

# ALGORITHM = settings.ALGORITHM
# ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
#
# password_hash = PasswordHash.recommended()
#
# DUMMY_HASH = password_hash.hash('dummypassword')
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


app = FastAPI()

# def get_password_hash(password):
#     return password_hash.hash(password)


app.include_router(expenses.router)

app.include_router(users.router)



@app.get('/')
async def home():
    return 'Welcome'