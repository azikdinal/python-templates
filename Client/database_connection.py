import psycopg2
from dotenv import load_dotenv
import os
import sys



# Указываем кодировку при загрузке .env файла
load_dotenv(encoding='utf-8')

# Параметры подключения к базе данных
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                options="-c search_path=public",  # Устанавливаем схему по умолчанию
                client_encoding="utf-8"  # Указываем кодировку UTF-8
            )
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка подключения к базе данных:", error)
            raise  # Добавляем raise, чтобы пробросить исключение выше

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Соединение с базой данных закрыто.")

    def fetch_data(self, query, params=None):
        try:
            self.connect()
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка при извлечении данных из базы данных:", error)
        finally:
            self.close_connection()
            

    def execute_query(self, query, params=None):
        try:
            self.connect()
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Запрос успешно выполнен.")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка при выполнении запроса:", error)
        finally:
            self.close_connection()
        

    def delete_event(self, event_id):
        try:
            self.connect()
            delete_query = "DELETE FROM events WHERE id = %s;"
            self.cursor.execute(delete_query, (event_id,))
            self.connection.commit()
            print(f"Запись с ID {event_id} успешно удалена.")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка при удалении записи из базы данных:", error)
        finally:
            self.close_connection()

        






