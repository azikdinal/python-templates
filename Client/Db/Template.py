from Db.Base import Base

class Template(Base):
    def __init__(self, connection, cursor, schema):
        super().__init__(connection, cursor)
        self.schema = schema

    def get_template_by_index(self, template_id: int):
        """
        Получение информации о шаблоне по его ID.

        :param template_id: ID шаблона.
        :return: Информация о шаблоне или None, если шаблон не найден.
        """
        sql = f"SELECT * FROM {self.schema}.templates WHERE id = {template_id}"
        result = self.get_result(sql)
        if result:
            return result[0]  # Возвращаем первый найденный шаблон
        else:
            return None

    def update_template(self, template):
        """
        Обновление информации о шаблоне в базе данных.

        :param template: Объект шаблона для обновления.
        :return: True, если обновление прошло успешно, иначе False.
        """
        sql = f"""
                UPDATE {self.schema}.templates
                SET name = '{template.name}', description = '{template.description}', columns = '{', '.join(template.columns)}'
                WHERE id = {template.id}
                """
        return self.get_result(sql)

    def delete_template(self, template_id: int):
        """
        Удаление шаблона из базы данных по его ID.

        :param template_id: ID шаблона для удаления.
        :return: True, если удаление прошло успешно, иначе False.
        """
        sql = f"DELETE FROM {self.schema}.templates WHERE id = {template_id}"
        return self.get_result(sql)
