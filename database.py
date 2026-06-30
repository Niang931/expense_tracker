import psycopg2
from security.logger import logger

DATABASE = 'test.db'

conn = psycopg2.connect(
    dbname=DATABASE,
)
