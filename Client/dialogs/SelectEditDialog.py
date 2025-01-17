from PyQt5.QtWidgets import QDialog
from Forms.select import Ui_SelectDialog
from Db.DbContext import DbContext
from widgets.PlaceWidget import PlaceWidget
from dialogs.LinkDialog import LinkDialog
from widgets.WorkerWidget import WorkerWidget
from dialogs.EditorDialog import EditorDialog
from dialogs.EquipmentDialog import EquipmentDialog

class SelectEditDialog(QDialog):
    def __init__(self, context: DbContext):
        super(SelectEditDialog, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_SelectDialog()
        self.ui.setupUi(self)
        
        self.ui.placeButton.clicked.connect(self.placeDialog)
        self.ui.linkButton.clicked.connect(self.linkDialog)
        self.ui.workerButton.clicked.connect(self.workerDialog)
        self.ui.eventButton.clicked.connect(self.eventDialog)
        self.ui.equipmentButton.clicked.connect(self.equipmentDialog)
        
    def placeDialog(self):
        self.hide()
        p = PlaceWidget(self.dbContext)
        p.exec()
        
    def linkDialog(self):
        self.hide()
        l = LinkDialog(self.dbContext)
        l.exec()
        
    def workerDialog(self):
        self.hide()
        w = WorkerWidget(self.dbContext)
        w.exec()
        
    def eventDialog(self):
        self.hide()
        e = EditorDialog(self.dbContext)
        e.exec()
        
    def equipmentDialog(self):
        self.hide()
        e = EquipmentDialog(self.dbContext)
        e.exec()
        