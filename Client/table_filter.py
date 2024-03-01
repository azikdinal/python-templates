# table_filter.py

from PyQt5.QtWidgets import QHeaderView, QMenu, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore


class TableFilter:
    def __init__(self, table_view, model):
        self.table_view = table_view
        self.model = model
        self.filter_column = 0  # Начнем с фильтрации по первой колонке

        self.filter_line_edit = QLineEdit()
        self.filter_button = QPushButton("Применить фильтр")
        self.filter_button.clicked.connect(self.apply_filter)

        self.setup_ui()

    def setup_ui(self):
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        filter_layout = QVBoxLayout()
        filter_layout.addWidget(self.filter_line_edit)
        filter_layout.addWidget(self.filter_button)

        container_widget = QWidget()
        container_widget.setLayout(filter_layout)

        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        menu = QMenu(self.table_view)

        for i in range(self.model.columnCount()):
            action = menu.addAction(self.model.horizontalHeaderItem(i).text())
            action.setCheckable(True)
            action.setChecked(i == self.filter_column)
            action.triggered.connect(lambda _, col=i: self.set_filter_column(col))

        menu.exec_(self.table_view.mapToGlobal(position))

    def set_filter_column(self, column):
        self.filter_column = column

    def apply_filter(self):
        filter_text = self.filter_line_edit.text().lower()
        for row in range(self.model.rowCount()):
            item = self.model.item(row, self.filter_column)
            if filter_text in item.text().lower():
                self.table_view.setRowHidden(row, False)
            else:
                self.table_view.setRowHidden(row, True)
