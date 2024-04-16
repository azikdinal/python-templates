from PyQt5.QtWidgets import QDialog
from Forms.link import Ui_linkDialog
from Db.DbContext import DbContext
from utils.Utils import Utils

class LinkDialog(QDialog):
    def __init__(self, context: DbContext):
        super(LinkDialog, self).__init__()
        
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
        