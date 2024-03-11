from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

class Utils:
    
    def toTableModel(data):
        headers = ['Статус', 'Название', 'Место', 'Дата', 'Время', 'Связной', 'Корресподент', 'Оператор', 'Водитель', 'Оборудование', 'Автор', 'Дополнение']
        model = QStandardItemModel(len(data), len(headers))
        model.setHorizontalHeaderLabels(headers)
        
        for row in data:
            model.appendRow([QStandardItem(item) for item in row])
            
        return model
        
    def createDialog(
        title: str,
        text: str,
        icon: QtWidgets.QMessageBox.Icon = QtWidgets.QMessageBox.Information
    ) -> QtWidgets.QMessageBox:
        """
        Create a dialog with the given title, text, and icon.

        Args:
            title (str): The title of the dialog.
            text (str): The text of the dialog.
            icon (QMessageBox.Icon, optional): The icon of the dialog. Defaults to QMessageBox.Information.

        Returns:
            QMessageBox: The created dialog.
        """
        dialog = QtWidgets.QMessageBox(icon, title, text, QtWidgets.QMessageBox.Ok)
        return dialog
