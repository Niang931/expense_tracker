import psycopg2

from ..models import ExpenseItem, Category
from fastapi import  APIRouter
from datetime import date
from typing import Optional
import os
from ..auth.database import connect_db
from security.logger import logger

router = APIRouter(
    prefix='/expenses',
    tags=['expenses'],
    responses={404:{'description':'Not found'}}
)

@router.get('/{username}')
async def get_expenses(username, password,
                       least_amount:Optional[float] = None,
                       expense_date:Optional[date]=None,
                       category: Optional[Category]=None):
    params = locals().copy()
    base_query = 'SELECT * FROM expenses WHERE user_id = (SELECT user_id FROM users WHERE username = %s'
    amount_query = ' amount >= %s '
    other_query = ' %s = %s '
    connector = ' AND '

    try:
        with connect_db() as cur:
            query = base_query
            values = [username]
            if least_amount:
                query += f'{connector} {amount_query}'
                values.append(least_amount)
            if expense_date:
                query += f'{other_query}'
                values.append(expense_date)
            if category:
                query += f'{other_query}'
                values.append(category)
            query += ')'
            print(values)
            print(query)
            cur.execute(query, (tuple(values)))
            items = cur.fetchall()
            return {'expenses': items}
    except psycopg2.DataError as e:
        logger.error(e)


@router.post('/{username}')
async def create_expense(username, expense:ExpenseItem):

    values = expense.model_dump()
    amount, expense_date, category = values['amount'], values['expense_date'], values['category']
    try:
        with connect_db() as cur:
            logger.info(values)
            cur.execute('SELECT user_id FROM users WHERE username = %s', (username,))
            user_id = cur.fetchone()
            logger.info(user_id)
            cur.executemany('INSERT INTO expenses '
                            'values (%s, %s, %s, %s)',
                            ((user_id, amount, expense_date, category),))
            logger.info(f'Expense with {amount} on {expense_date} created successfully')
    except psycopg2.DataError as e:
        logger.error(e)


