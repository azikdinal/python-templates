from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QCalendarWidget, QTimeEdit
from database_connection import DatabaseConnection


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
        # Создайте объект для работы с базой данных
        db_connection = DatabaseConnection()

        try:
            # Заполняем выпадающий список статуса
            status_query = "SELECT DISTINCT status FROM events"
            status_values = db_connection.fetch_data(status_query)
            self.statusComboBox.addItems([status[0] for status in status_values])

            # Повторите процесс для других выпадающих списков
            place_query = "SELECT DISTINCT place FROM events"
            place_values = db_connection.fetch_data(place_query)
            self.placeComboBox.addItems([place[0] for place in place_values])

            linked_query = "SELECT DISTINCT linked FROM events"
            linked_values = db_connection.fetch_data(linked_query)
            self.linkedComboBox.addItems([linked[0] for linked in linked_values])

            # Повторите процесс для других выпадающих списков

        except Exception as e:
            print("Ошибка при заполнении выпадающих списков:", e)
        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()

    def addRecord(self):
        # Получение данных из элементов формы
        data = self.getEnteredData()

        # Создаем экземпляр класса DatabaseConnection
        db_connection = DatabaseConnection()

        try:
            # Устанавливаем соединение с базой данных
            db_connection.connect()

            # Пример запроса для вставки данных в таблицу events
            insert_query = """
            INSERT INTO events (status, title, place, date, time, related, correspondent, operator, driver, equipment, author, additional_info)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Передаем данные для вставки
            db_connection.cursor.execute(insert_query, (
                data["status"], data["title"], data["place"], data["date"],
                data["time"], data["linked"], data["correspondent"],
                data["operator"], data["driver"], data["equipment"],
                data["author"], data["additional_info"]
            ))

            # Подтверждаем транзакцию
            db_connection.connection.commit()

            # Закрываем диалог
            self.accept()

        except Exception as e:
            print("Ошибка при добавлении записи в базу данных:", e)

        finally:
            # Закрываем соединение с базой данных в блоке finally,
            # чтобы убедиться, что соединение закрыто даже в случае ошибки
            db_connection.close_connection()

    def getEnteredData(self):
        # Получение данных из элементов формы
        data = {
            "status": self.statusComboBox.currentText(),
            "title": self.titleLineEdit.text(),
            "place": self.placeComboBox.currentText(),
            # Добавьте остальные поля
        }
        return data

