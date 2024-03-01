from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QTableView

class TableTab(QWidget):
    def __init__(self, parent=None):
        super(TableTab, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tableView = QTableView(self)
        self.layout.addWidget(self.tableView)

class TemplateManager:
    def __init__(self, parent):
        self.parent = parent

    def open_template(self):
        # В этом методе вы можете добавить логику загрузки данных из выбранного шаблона
        # Здесь я добавлю простой пример создания новой вкладки и таблицы
        table_tab = TableTab(self.parent.tabs)
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(5)
        for i in range(5):
            for j in range(3):
                item = QTableWidgetItem(f"Строка {i}, Столбец {j}")
                table.setItem(i, j, item)

        table_tab.tableView.setModel(table.model())
        tab_index = self.parent.tabs.addTab(table_tab, "Новая вкладка")
        self.parent.tabs.setCurrentIndex(tab_index)

class DataItem:
    def __init__(self, author, name, guest, place):
        self.author = author
        self.name = name
        self.guest = guest
        self.place = place