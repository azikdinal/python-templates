from Db.Base import Base

class Events(Base):
    
    def __init__(self, connection, cursor, schema : str) -> None:
        Base.__init__(self, connection, cursor)

        self.table = 'events'
        self.schema = schema
        
    def get(self):
        res = self.sql_select(self.schema, self.table)
        if res:
            return res
        return None
    
    def add(self, status, title, place, date, time, related, correspondent, operator, driver, equipment, author, additional_info):
        return self.sql_insert(self.schema, self.table, {
            'status': status, 'title': title, 'place': place, 'date': date, 
            'time': time, 'related': related, 'correspondent': correspondent,
            'operator': operator, 'driver': driver, 'equipment': equipment,
            'author': author, 'additional_info': additional_info
        })
        
    def update(self, id, status, title, place, date, time, related, correspondent, operator, driver, equipment, author, additional_info):
        return self.sql_update(self.schema, self.table, {
            'status': status, 'title': title, 'place': place, 'date': date, 
            'time': time, 'related': related, 'correspondent': correspondent,
            'operator': operator, 'driver': driver, 'equipment': equipment,
            'author': author, 'additional_info': additional_info
        }, where=f"id = {id}")