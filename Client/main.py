from PyQt5 import QtWidgets, uic
from Forms.main import Ui_MainWindow
from database_connection import DatabaseConnection
from calendarWindow import calendarWindow
from addElementDialog import AddElementDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QToolBar, QAction, QStatusBar, QFormLayout, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCalendarWidget, QTimeEdit, QListView, QFrame
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QCalendarWidget, QTimeEdit
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

        self.addElementDialog = AddElementDialog(self)

        self.ui.addButton.clicked.connect(self.addElementDialog.show)  # Открываем диалог добавления при нажатии кнопки "Добавить"
        self.ui.deleteButton.clicked.connect(self.deleteElement)  # Вызываем функцию удаления при нажатии кнопки "Удалить"
        self.ui.editButton.clicked.connect(self.editElement)  # Вызываем функцию редактирования при нажатии кнопки "Редактировать"
        self.ui.deleteButton.clicked.connect(self.dellButtonClick)


    def addElement(self):
        dialog = AddElementDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.getEnteredData()
            # Обработка данных, например, добавление элемента в список или базу данных   
            
    def addElement(self):
        data = self.addElementDialog.getEnteredData()
        # Добавляем элемент в список или в QListView
        # Пример для QListView: self.ui.listView.model().appendRow(QtGui.QStandardItem(data["title"]))

    def populateComboBoxes(self):
        # Создайте объект для работы с базой данных
        db_connection = DatabaseConnection()

        try:
            # Заполняем выпадающий список статуса
            status_query = "SELECT DISTINCT status FROM events"
            status_values = db_connection.fetch_data(status_query)
            self.statusComboBox.addItems([status[0] for status in status_values])

            # Повторите процесс для других выпадающих списков
        except Exception as e:
            print("Ошибка при заполнении выпадающих списков:", e)
        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()
             

    def deleteElement(self):
        # Реализуйте операцию удаления элемента
        print("Deleting element...")

    def editElement(self):
        # Реализуйте операцию редактирования элемента
        print("Editing element...")    

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