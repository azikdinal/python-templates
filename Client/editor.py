from PyQt5 import QtWidgets
from Forms.editor import Ui_Editor
from Db.DbContext import DbContext
from Utils import Utils

class editor(QtWidgets.QDialog):
    
    statusBoof = {}
    placeBoof = {}
    workerBoof = {}
    linkBoof = {}
    authorBoof = {}
    equipmentBoof = {}
    
    def __init__(self, context: DbContext):
        super(editor, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_Editor()
        self.ui.setupUi(self)
        
        for status in self.dbContext.status.get():
            self.ui.StatusCombo.addItem(status['name'])
            self.statusBoof[status['name']] = status['id']
        
        for place in self.dbContext.place.get():
            self.ui.PlaceCombo.addItem(place['name'])
            self.placeBoof[place['name']] = place['id']
            
        for worker in self.dbContext.worker.get():
            self.ui.CorrespondentLineEdit.addItem(worker['fio'])
            self.ui.OperatorLineEdit.addItem(worker['fio'])
            self.ui.DriverComboBox.addItem(worker['fio'])
            self.workerBoof[worker['name']] = worker['id']
            
        for link in self.dbContext.link.get():
            self.ui.LinkedLineEdit.addItem(link['fio'])
            self.linkBoof[link['name']] = link['id']
            
        for author in self.dbContext.user.get():
            self.ui.AuthorComboBox.addItem(author['fio'])
            self.authorBoof[author['name']] = author['id']
            
        for equipment in self.dbContext.equipment.get():
            self.ui.EquipmentLineEdit.addItem(equipment['name'])
            self.equipmentBoof[equipment['name']] = equipment['id']
            
        self.ui.CancelPushButton_3.clicked.connect(self.close)
        self.ui.SavePushButton.clicked.connect(self.save)
            
    def save(self):
        res = self.dbContext.events.add(
            self.statusBoof[self.ui.StatusCombo.currentText()],
            self.ui.NameLineEdit.text(),
            self.placeBoof[self.ui.PlaceCombo.currentText()],
            self.ui.DateEdit.dateTime(),
            
        )
        if res:
            msg_box = Utils.createDialog("Готово", "Данные сохранены")
            msg_box.exec_() 
        self.close()
        