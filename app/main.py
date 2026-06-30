from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers import users
from app.routers import expenses
import os

DATABASE_URL = os.getenv("DATABASE_URL")
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Global reference for connection pool
db_pool = None

@asynccontextmanager
async def lifespan(app:FastAPI):
    global db_pool



app.include_router(expenses.router)

app.include_router(users.router)



@app.get('/')
async def home():
    return 'Welcome'