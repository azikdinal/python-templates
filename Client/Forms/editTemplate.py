from PyQt5.QtWidgets import *
from Db.DbContext import DbContext
from Client.template_dialog import Template

class EditTemplateDialog(QDialog):
    def __init__(self, db_context, template_id=None):
        super().__init__()
        self.db_context = db_context
        self.template_id = template_id

        self.nameLineEdit = QLineEdit()
        self.columnsComboBox = QComboBox()

        self.initUi()

        if template_id is not None:
            template = self.db_context.get_template(template_id)
            self.nameLineEdit.setText(template.name)
            self.columnsComboBox.addItems(template.columns)

    def getData(self):
        return {
            "name": self.nameLineEdit.text(),
            "columns": self.columnsComboBox.selectedItems(),
        }

    def saveButtonClick(self):
        data = self.getData()
        if self.template_id is None:
            new_template = Template(name=data['name'], columns=data['columns'])
            self.dbContext.create_template(new_template, user_id=self.user['id'])
        else:
            updated_template = Template(id=self.template_id, name=data['name'], columns=data['columns'])
            self.dbContext.update_template(updated_template)
        self.close()