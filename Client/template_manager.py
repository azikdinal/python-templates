import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, QPushButton

class TemplateManager:
    def __init__(self, parent):
        self.parent = parent
        self.template_data = [
            ["Столбец1", "Столбец2", "Столбец3"],
            ["Значение11", "Значение12", "Значение13"],
            ["Значение21", "Значение22", "Значение23"],
        ]

    def open_template(self):
        new_tab = QWidget()
        self.parent.tabs.addTab(new_tab, "Новая вкладка")

        new_table = QTableWidget(new_tab)
        new_table.setColumnCount(len(self.template_data[0]))
        new_table.setRowCount(len(self.template_data))
        for i, row in enumerate(self.template_data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                new_table.setItem(i, j, item)

        self.parent.tabs.setCurrentWidget(new_tab)