import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL', '')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')


settings = Settings()  # type: ignore