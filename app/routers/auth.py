import psycopg2
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.params import Depends
from app.internal.user import get_user_by_username, create_user
from app.internal.auth import verify_user
from security.logger import logger
from app.core.database import connect_db
from app.models import UserCreate, Token
from app.core.jwt import create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/register', response_model=str)
async def register_user(user: UserCreate, cur= Depends(connect_db)):
    username, password = user.username, user.password
    try:
        if get_user_by_username(cur,username) is not None:
            raise HTTPException(status_code=409, detail='Username already exists')
        create_user(cur, username, password)
        return username

    except psycopg2.DataError as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=e)


@router.post('/login', response_model=Token)
async def login_user(user: UserCreate, cur= Depends(connect_db)):
    username, password = user.username, user.password
    try:
        user_id = get_user_by_username(cur, username)
        if  len(user_id) == 0:
            raise HTTPException(status_code=404, detail='User not found. Please register first')

        if not verify_user(cur, username, password):
            raise HTTPException(status_code=401, detail='Incorrect credentials')

        access_token = create_access_token(user_id=user_id[0])
        token = Token(access_token=access_token, token_type='bearer')
        return token

    except psycopg2.DataError as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=e)
