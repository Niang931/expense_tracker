from pydantic import BaseModel
from enum import Enum
import datetime


class UserCreate(BaseModel):
    username: str
    password: str

class UserDB(BaseModel):
    username: str
    hashed_password: str

class Category(str, Enum):
    FOOD = 'food'
    TRANSPORT = 'transport'
    SOCIAL = 'social'
    HOUSEHOLD = 'household'
    EXERCISE = 'exercise'
    OTHERS = 'others'

class ExpenseItem(BaseModel):
    amount: float
    expense_date:datetime.date = datetime.date.today()
    category: Category = Category.FOOD

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


