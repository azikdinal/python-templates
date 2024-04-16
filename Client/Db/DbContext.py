from Db.User import User
from Db.Events import Events
from Db.Status import Status
from Db.Place import Place
from Db.Link import Link
from Db.Worker import Worker
from Db.Author import Author
from Db.Equipment import Equipment
from Db.DataBase import DataBase
from Db.Template import Template  # Добавляем импорт класса Template
import json
import psycopg2

class DbContext(DataBase):
    def __init__(self, data=None):
        super().__init__()
        
        self.__user = User(self.conn, self.cursor, self.schema)
        self.__events = Events(self.conn, self.cursor, self.schema)
        self.__status = Status(self.conn, self.cursor, self.schema)
        self.__place = Place(self.conn, self.cursor, self.schema)
        self.__link = Link(self.conn, self.cursor, self.schema)
        self.__worker = Worker(self.conn, self.cursor, self.schema)
        self.__author = Author(self.conn, self.cursor, self.schema)
        self.__equipment = Equipment(self.conn, self.cursor, self.schema)
        self.__template = Template(self.conn, self.cursor, self.schema)  # Добавляем атрибут для работы с шаблонами
        self.data = data if data is not None else []
        
    @property
    def user(self) -> User:
        return self.__user
        
    @property
    def events(self) -> Events:
        return self.__events
        
    @property
    def status(self) -> Status:
        return self.__status
        
    @property
    def place(self) -> Place:
        return self.__place
        
    @property
    def link(self) -> Link:
        return self.__link
        
    @property
    def worker(self) -> Worker:
        return self.__worker
    
    @property
    def author(self) -> Author:
        return self.__author
        
    @property
    def equipment(self) -> Equipment:
        return self.__equipment
    
    @property
    def template(self) -> Template:  # Добавляем свойство для доступа к объекту Template
        return self.__template

    def filter_data(self, author, name, guest, place):
        # Фильтрация данных по заданным критериям
        filtered_data = self.data
        if author:
            filtered_data = [row for row in filtered_data if row['author'] == author]
        if name:
            filtered_data = [row for row in filtered_data if row['name'] == name]
        if guest:
            filtered_data = [row for row in filtered_data if row['guest'] == guest]
        if place:
            filtered_data = [row for row in filtered_data if row['place'] == place]
        return filtered_data
    

    def add_template(self, template: Template):
        # Добавление нового шаблона в базу данных
        query = "INSERT INTO templates1 (name, description, columns) VALUES (%s, %s, %s)"
        values = (template.name, template.description, json.dumps(template.columns))
        self.cursor.execute(query, values)
        self.conn.commit()

    def execute_query(self, query, parameters=None):
        try:
            self.cursor.execute(query, parameters)
            result = self.cursor.fetchall()  # Получаем результаты запроса
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка при выполнении запроса:", error)
            return None    
        
    def get_all_template_names(self):
        # Запрос к базе данных для получения всех имен шаблонов
        query = "SELECT name FROM templates1"
        self.cursor.execute(query)
        template_names = self.cursor.fetchall()
        return [name[0] for name in template_names]
    
    def get_template_by_name(self, template_name):
        # Запрос к базе данных для получения шаблона по его имени
        query = "SELECT name, description, columns FROM templates1 WHERE name = %s"
        self.cursor.execute(query, (template_name,))
        template_data = self.cursor.fetchone()
        if template_data:
            name, description, columns_json = template_data
            print("Содержимое columns_json перед json.loads():", columns_json)  # Добавляем отладочный вывод
            columns = columns_json
            return Template(name, description, columns)
        else:
            return None
