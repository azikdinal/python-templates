from PyQt5 import QtWidgets, uic
from Forms.main import Ui_MainWindow
from calendarWindow import calendarWindow

import sys
 
class mywindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dellButton.setVisible(False)
        self.ui.calendarLayput.setVisible(False)
        self.ui.oneButton.clicked.connect(self.oneButtonClick)
        self.ui.twoButton.clicked.connect(self.twoButtonClick)
        self.ui.dellButton.clicked.connect(self.dellButtonClick)
        self.ui.menu_3.triggered.connect(sys.exit)
        
        self.calendarWindow = calendarWindow()
        self.setUiGroup(2)

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
        

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())