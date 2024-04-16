from Db.Base import Base

class User(Base):
    
    def __init__(self, connection, cursor, schema : str) -> None:
        Base.__init__(self, connection, cursor)

        self.table = 'users'
        self.schema = schema
    
    def getByLogPass(self, login : str, password : str):
        res = self.sql_select(self.schema, self.table, where=f"username = {self.to_property(login)} and password = {self.to_property(password)}")
        if res:
            return res
        return None
    
    def get(self):
        res = self.sql_select(self.schema, self.table)
        if res:
            return res
        return []