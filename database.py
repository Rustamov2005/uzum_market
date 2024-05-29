import psycopg2 as psql


class Database:

    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database='lesson_10',
            user='postgres',
            password='20052005',
            host='localhost',
            port='5432',
        )
        cursor = db.cursor()
        cursor.execute(query)
        data = ['insert', 'create', 'delete', 'update']
        if query_type in data:
            db.commit()
            return f"{query_type} seccessful"
        else:
            return cursor.fetchall()
