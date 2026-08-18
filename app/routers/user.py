# from fastapi import FastAPI, APIRouter
#
#
# router = APIRouter(
#     prefix='user', tags=['users']
# )
#
#
# @router.get('/')
# async def get_user():
#     with connect_db() as cur:
#         cur.execute('SELECT * FROM users')
#         users = cur.fetchall()
#         return {'users': users}