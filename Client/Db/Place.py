from Db.Base import Base

class Place(Base):
    
    def __init__(self, connection, cursor, schema : str) -> None:
        Base.__init__(self, connection, cursor)

        self.table = 'places'
        self.schema = schema
        
    def get(self):
        res = self.sql_select(self.schema, self.table)
        if res:
            return res
        return []
    
    def add(self, name, address, details):
        return self.sql_insert(self.schema, self.table, {
            'name': name, 'address': address, 'details': details 
        })