from PyQt5 import QtWidgets
from Forms.select import Ui_SelectDialog
from Db.DbContext import DbContext
from place import place
from link import link
from worker import worker
from editor import editor
from equipment import equipment

class selectEdit(QtWidgets.QDialog):
    def __init__(self, context: DbContext):
        super(selectEdit, self).__init__()
        
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
        p = place(self.dbContext)
        p.exec()
        
    def linkDialog(self):
        self.hide()
        l = link(self.dbContext)
        l.exec()
        
    def workerDialog(self):
        self.hide()
        w = worker(self.dbContext)
        w.exec()
        
    def eventDialog(self):
        self.hide()
        e = editor(self.dbContext)
        e.exec()
        
    def equipmentDialog(self):
        self.hide()
        e = equipment(self.dbContext)
        e.exec()
        