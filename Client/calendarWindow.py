from PyQt5 import QtWidgets, uic
from Forms.calendar import Ui_CalendarWindow

import sys
 
class calendarWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(calendarWindow, self).__init__()
        self.ui = Ui_CalendarWindow()
        self.ui.setupUi(self)