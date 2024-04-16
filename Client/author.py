from PyQt5 import QtWidgets
from Forms.author import Ui_AuthorDialog
from Db.DbContext import DbContext
from Utils import Utils

class author(QtWidgets.QDialog):
    def __init__(self, context: DbContext):
        super(author, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_AuthorDialog()
        self.ui.setupUi(self)
        
        self.ui.CancelPushButton_3.clicked.connect(self.close)
        self.ui.SavePushButton.clicked.connect(self.save)
        
    def save(self):
        res = self.dbContext.worker.add(
            self.ui.fioLineEdit.text(),
            self.ui.jobTitleLineEdit.text(),
        )
        if res:
            msg_box = Utils.createDialog("Готово", "Данные сохранены")
            msg_box.exec_() 
        self.close()
        