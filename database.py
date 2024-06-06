import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()


class Database:

    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            host=os.getenv('host'),
            port=os.getenv('port'),
        )
        cursor = db.cursor()
        cursor.execute(query)
        data = ['insert', 'create', 'delete', 'update']
        if query_type in data:
            db.commit()
            return f"{query_type} seccessful"
        else:
            return cursor.fetchall()
