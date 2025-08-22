import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    conn = psycopg2.connect(
        dbname="gallery",
        user="postgres",
        password="1910",   # change if different
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
    )
    return conn