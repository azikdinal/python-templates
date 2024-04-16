import os, datetime
from typing import Any

class Base:

    def __init__(self, connection, cursor) -> None:
        self.cursor = cursor
        self.conn = connection

    def to_property(self, prop : Any) -> str:
        if type(prop) == str:
            return f"'{prop}'"
        elif type(prop) == int:
            return str(prop)
        elif type(prop) == bool:
            return str(prop)
        elif type(prop) == datetime.date:
            return f"TO_TIMESTAMP({self.to_property(prop.strftime('%d-%m-%Y %X'))}, 'DD-MM-YYYY HH24:MI:SS')"
        else:
            return "null"
        
    def to_set_row(self, columns : dict) -> str:
        result = []
 
        for key in columns.keys():
            result.append(f"{key} = {self.to_property(columns[key])}")

        return ', '.join(result)
        
    def sql_select(self, schema : str, table : str, columns : list[str] = ['*'], where : str = None, joins : list[dict] = None, group_by : str = None, having : str = None) -> list[dict] | None:
        path = '.'.join([schema, table]).strip('.')
        sql = f"""
                SELECT {', '.join(columns)} FROM {path} AS {table}
                """
        if joins:
            for join in joins:
                if not 'j_type' in join:
                    join['j_type'] = 'INNER'
                l_table, column = tuple(join['l_table'].split('.'))
                sql += f"{join['j_type']} JOIN {schema}.{l_table} AS {l_table} ON {l_table}.{column} = {join['r_table']}"

        if where:
            sql += f" WHERE {where}"

        if group_by:
            sql += f" GROUP BY {group_by}"

        if having:
            sql += f" HAVING {having}"

        return self.get_result(sql)
    
    def sql_insert(self, schema : str, table : str, columns : dict) -> bool:
        path = '.'.join([schema, table]).strip('.')
        sql = f"""
                INSERT INTO {path}
                ({', '.join(list(columns.keys()))})
                VALUES
                ({', '.join(list(map(self.to_property, list(columns.values()))))})
                """
        
        return self.get_result(sql)
    
    def sql_delete(self, schema : str, table : str, where : str) -> bool:
        path = '.'.join([schema, table]).strip('.')
        sql = f"""
                DELETE FROM {path}
                WHERE {where}
                """
        
        return self.get_result(sql)
    
    def sql_update(self, schema : str, table : str, columns : dict, where : str) -> bool:
        path = '.'.join([schema, table]).strip('.')
        sql = f"""
                UPDATE {path} 
                SET {self.to_set_row(columns)}
                WHERE {where}
                """
        return self.get_result(sql)

    def get_result(self, sql : str) -> list[dict] | bool:
        try:
            self.cursor.execute(sql)

            if 'SELECT' in sql:
                result = []
                rows = self.cursor.fetchall()

                for row in rows:
                    tmp_result = {}

                    index = 0
                    for column in self.cursor.description:
                        tmp_result[column.name] = row[index]
                        index += 1

                    result.append(tmp_result)

                return result
            else:
                self.conn.commit()
                return True

        except Exception as e:
            self.conn.rollback()
            print(f"Произошла ошибка:\n {e}\n")
            return False