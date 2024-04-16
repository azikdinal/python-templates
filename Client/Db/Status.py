from Db.Base import Base

class Status(Base):
    
    def __init__(self, connection, cursor, schema : str) -> None:
        Base.__init__(self, connection, cursor)

        self.table = 'status'
        self.schema = schema
        
    def get(self):
        res = self.sql_select(self.schema, self.table)
        if res:
            return res
        return []