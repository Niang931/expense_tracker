from fastapi import FastAPI
from app.routers import expenses, auth

app = FastAPI()

app.include_router(expenses.router)

app.include_router(auth.router)

# app.include_router(user.router)


@app.get('/')
async def home():
    return 'Welcome'