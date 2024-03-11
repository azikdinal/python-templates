from PyQt5 import QtWidgets
from Forms.link import Ui_linkDialog
from Db.DbContext import DbContext
from Utils import Utils

class link(QtWidgets.QDialog):
    def __init__(self, context: DbContext):
        super(link, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_linkDialog()
        self.ui.setupUi(self)
        
        self.ui.CancelPushButton_3.clicked.connect(self.close)
        self.ui.SavePushButton.clicked.connect(self.save)
        
    def save(self):
        res = self.dbContext.link.add(
            self.ui.fioLineEdit.text(),
            self.ui.jobTitleLineEdit.text(),
            self.ui.connectionLineEdit.text(),
            self.ui.additionLineEdit.text(),
        )
        if res:
            msg_box = Utils.createDialog("Готово", "Данные сохранены")
            msg_box.exec_() 
        self.close()
        