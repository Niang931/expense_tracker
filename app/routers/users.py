from fastapi import FastAPI, APIRouter

users = ['Naing', 'Kato']
router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404:{'description':'User Not found'}}
)

@router.get('/')
async def get_user():
    return {"user":users}

@router.post('/{username}')
async def create_user(username, password):
    pass

@router.put('/{username}')
async def modify_user(username, password):
    pass
