from PyQt5 import QtWidgets
from Forms.place import Ui_PlaceDialog
from Db.DbContext import DbContext
from Utils import Utils

class place(QtWidgets.QDialog):
    def __init__(self, context: DbContext):
        super(place, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_PlaceDialog()
        self.ui.setupUi(self)
        
        self.ui.CancelPushButton_3.clicked.connect(self.close)
        self.ui.SavePushButton.clicked.connect(self.save)
        
    def save(self):
        res = self.dbContext.place.add(
            self.ui.NameLineEdit.text(),
            self.ui.AddresLineEdit.text(),
            self.ui.DetailsLineEdit.text()
        )
        if res:
            msg_box = Utils.createDialog("Готово", "Данные сохранены")
            msg_box.exec_() 
        self.close()
        