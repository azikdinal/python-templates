import psycopg2, os

class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
        self.cursor = self.conn.cursor()
        self.schema = os.getenv('DB_SCHEMA')
        if self.schema:
            self.schema = f'"{self.schema}"'