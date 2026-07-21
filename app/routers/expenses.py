import psycopg2
from ..models import ExpenseItem, Category
from fastapi import APIRouter, HTTPException
from datetime import date
from typing import Optional
from ..core.database import connect_db
from security.logger import logger
from app.routers.auth import verify_user
from fastapi import Depends
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix='/expenses',
    tags=['expenses'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_expenses(
        least_amount: Optional[float] = None,
        expense_date: Optional[date] = None,
        category: Optional[Category] = None,
        cur=Depends(connect_db),
        user_id=Depends(get_current_user)):
    base_query = 'SELECT * FROM expenses WHERE user_id =  %s '
    amount_query = ' amount >= %s '
    other_query = ' %s = %s '
    connector = ' AND '

    try:
        query = base_query
        values = [user_id]
        if least_amount:
            query += f'{connector} {amount_query}'
            values.append(least_amount)
        if expense_date:
            query += f'{other_query}'
            values.append(expense_date)
        if category:
            query += f'{other_query}'
            values.append(category)
        # query += ')'
        cur.execute(query, (tuple(values)))
        items = cur.fetchall()
        return {'expenses': items}
    except psycopg2.DataError as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=e)


@router.post('/{username}')
async def create_expense(expense: ExpenseItem,
                         cur=Depends(connect_db),
                         user_id=Depends(get_current_user)):
    amount, expense_date, category = expense.amount, expense.expense_date, expense.category
    try:
        cur.executemany('INSERT INTO expenses '
                        'values (%s, %s, %s, %s)',
                        ((user_id, amount, expense_date, category),))
        logger.info(f'Expense with {amount} on {expense_date} created successfully')
        return
    except psycopg2.DataError as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=e)
