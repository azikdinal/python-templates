from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QCalendarWidget, QTimeEdit



class AddElementDialog(QDialog):
    def __init__(self, parent=None):
        super(AddElementDialog, self).__init__(parent)

        self.setWindowTitle("Форма заполнения")

        # Создание элементов формы
        self.statusComboBox = QComboBox(self)
        self.titleLineEdit = QLineEdit(self)
        self.placeComboBox = QComboBox(self)
        self.dateCalendar = QCalendarWidget(self)
        self.startTimeEdit = QTimeEdit(self)
        self.endTimeEdit = QTimeEdit(self)
        self.linkedComboBox = QComboBox(self)
        self.correspondentComboBox = QComboBox(self)
        self.operatorComboBox = QComboBox(self)
        self.driverComboBox = QComboBox(self)
        self.equipmentComboBox = QComboBox(self)
        self.authorComboBox = QComboBox(self)
        self.notesTextEdit = QTextEdit(self)

        # Наполнение выпадающих списков данными из БД
        self.populateComboBoxes()

        # Кнопки
        self.addButton = QPushButton("Добавить", self)
        self.cancelButton = QPushButton("Отмена", self)

        # Размещение элементов в форме
        layout = QVBoxLayout(self)

        form_layout = QFormLayout()
        form_layout.addRow("Статус:", self.statusComboBox)
        form_layout.addRow("Название:", self.titleLineEdit)
        form_layout.addRow("Место:", self.placeComboBox)
        form_layout.addRow("Дата:", self.dateCalendar)
        form_layout.addRow("Время начала:", self.startTimeEdit)
        form_layout.addRow("Время окончания:", self.endTimeEdit)
        form_layout.addRow("Связной:", self.linkedComboBox)
        form_layout.addRow("Корреспондент:", self.correspondentComboBox)
        form_layout.addRow("Оператор:", self.operatorComboBox)
        form_layout.addRow("Водитель:", self.driverComboBox)
        form_layout.addRow("Оборудование:", self.equipmentComboBox)
        form_layout.addRow("Автор:", self.authorComboBox)

        layout.addLayout(form_layout)
        layout.addWidget(QLabel("Дополнение:"))
        layout.addWidget(self.notesTextEdit)
        layout.addWidget(self.addButton)
        layout.addWidget(self.cancelButton)

        # Подключение сигналов к слотам
        self.addButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

    def populateComboBoxes(self):
        # Реализуйте логику наполнения выпадающих списков данными из БД
        # Например, self.statusComboBox.addItems(["в процессе", "завершен", "отменен"])
        pass

    def getEnteredData(self):
        # Получение данных из элементов формы
        data = {
            "status": self.statusComboBox.currentText(),
            "title": self.titleLineEdit.text(),
            "place": self.placeComboBox.currentText(),
            # Добавьте остальные поля
        }
        return data

