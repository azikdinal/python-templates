from Db.Base import Base

class Link(Base):
    
    def __init__(self, connection, cursor, schema : str) -> None:
        Base.__init__(self, connection, cursor)

        self.table = 'related'
        self.schema = schema
        
    def get(self):
        res = self.sql_select(self.schema, self.table)
        if res:
            return res
        return []
    
    def add(self, fio, position, link, details):
        return self.sql_insert(self.schema, self.table, {
            'fio': fio, 'position': position, 'link': link,
            'details': details
        })