from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Forms.main import Ui_MainWindow
from calendarWindow import calendarWindow
from Db.DbContext import DbContext
from Db.User import User
from Utils import Utils
from selectEdit import selectEdit

import sys
 
class main(QMainWindow):
    def __init__(self, dbContext: DbContext, user : User):
        super(main, self).__init__()
        self.dbContext = dbContext
        self.user = user
        
        self.selectEdit = selectEdit(dbContext)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dellButton.setVisible(False)
        self.ui.calendarLayput.setVisible(False)
        self.ui.oneButton.clicked.connect(self.oneButtonClick)
        self.ui.twoButton.clicked.connect(self.twoButtonClick)
        self.ui.dellButton.clicked.connect(self.dellButtonClick)
        self.ui.addButton.clicked.connect(self.addEventButton)
        self.ui.menu_3.triggered.connect(sys.exit)
        
        self.calendarWindow = calendarWindow()
        self.setUiGroup(user['group_id'])
        
        self.ui.tableView.setModel(Utils.toTableModel([]))

    def oneButtonClick(self):
        if self.calendarWindow.isHidden():
            self.calendarWindow.show()
        else:
            self.calendarWindow.hide()
        
    def twoButtonClick(self):
        self.ui.dellButton.setVisible(True)
        self.ui.oneButton.setVisible(False)
        self.ui.twoButton.setVisible(False)
        self.ui.calendarLayput.setVisible(True)
        
    def dellButtonClick(self):
        self.ui.dellButton.setVisible(False)
        self.ui.calendarLayput.setVisible(False)
        self.ui.oneButton.setVisible(True)
        self.ui.twoButton.setVisible(True)
        
    def setUiGroup(self, group : int):
        if group == 1:
            self.ui.menu_2.show()
            self.ui.deleteButton.setVisible(True)
        elif group == 2:
            self.ui.menu_2.hide()
            self.ui.deleteButton.setVisible(False)
            
    def addEventButton(self):
        self.selectEdit.exec()