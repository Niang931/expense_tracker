from pydantic import BaseModel
from enum import Enum
import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserDB(UserBase):
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
    category: Category = 'food'

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

