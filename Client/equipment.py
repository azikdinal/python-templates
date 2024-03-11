from PyQt5 import QtWidgets
from Forms.equipment import Ui_equipmentDialog
from Db.DbContext import DbContext
from Utils import Utils

class equipment(QtWidgets.QDialog):
    def __init__(self, context: DbContext):
        super(equipment, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_equipmentDialog()
        self.ui.setupUi(self)
        
        self.ui.CancelPushButton_3.clicked.connect(self.close)
        self.ui.SavePushButton.clicked.connect(self.save)
        
    def save(self):
        res = self.dbContext.equipment.add(
            self.ui.NameLineEdit.text(),
            self.ui.detailsLineEdit.text(),
        )
        if res:
            msg_box = Utils.createDialog("Готово", "Данные сохранены")
            msg_box.exec_() 
        self.close()
        
        