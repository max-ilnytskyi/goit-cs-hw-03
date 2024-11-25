import psycopg2
from contextlib import contextmanager

DATABASE_URL = "postgresql://postgres:567234@localhost:5432/postgres"

@contextmanager
def create_connection():
    connection = psycopg2.connect(DATABASE_URL)
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()