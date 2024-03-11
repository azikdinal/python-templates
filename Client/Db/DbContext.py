from Db.User import User
from Db.Events import Events
from Db.Status import Status
from Db.Place import Place
from Db.Link import Link
from Db.Worker import Worker
from Db.Equipment import Equipment
from Db.DataBase import DataBase

class DbContext(DataBase):

    def __init__(self):
        DataBase.__init__(self)
        
        self.__user = User(self.conn, self.cursor, self.schema)
        self.__events = Events(self.conn, self.cursor, self.schema)
        self.__status = Status(self.conn, self.cursor, self.schema)
        self.__place = Place(self.conn, self.cursor, self.schema)
        self.__link = Link(self.conn, self.cursor, self.schema)
        self.__worker = Worker(self.conn, self.cursor, self.schema)
        self.__equipment = Equipment(self.conn, self.cursor, self.schema)
        
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
    def equipment(self) -> Equipment:
        return self.__equipment