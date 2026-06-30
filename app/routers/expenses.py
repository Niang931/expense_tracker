from fastapi import  APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional

class Category(str, Enum):
    FOOD = 'food'
    TRANSPORT = 'transport'
    SOCIAL = 'social'
    HOUSEHOLD = 'household'
    EXERCISE = 'exercise'
    OTHERS = 'others'

class ExpenseItem(BaseModel):
    expense_date:date
    category: Category
    amount: float

router = APIRouter(
    prefix='/expenses',
    tags=['expenses'],
    responses={404:{'description':'Not found'}}
)

@router.get('/{username}')
async def get_expenses(username, password,
                       expense_date:Optional[date]=None,
                       category: Optional[Category]=None,
                       least_amount:Optional[float] = None):
    return 'get expense'

@router.post('/{username}')
async def create_expense(username, password,
                         expense_item:ExpenseItem):
    pass


