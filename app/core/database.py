import psycopg2
from app.config import settings
from security.logger import logger

DATABASE_URL = settings.DATABASE_URL

def connect_db():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        yield cur
        conn.commit()
    except psycopg2.OperationalError as e:
        logger.error(e)
        if conn:
            conn.rollback()
        raise
    finally:
        if conn is not None:
            conn.close()