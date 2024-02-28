from PyQt5 import QtWidgets, uic
from database_connection import DatabaseConnection

class EventManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(EventManager, self).__init__()
        uic.loadUi("Client/Forms/event_form.ui", self)

        # Подключение к базе данных
        self.db_connection = DatabaseConnection()

        # Заполнение выпадающих списков данными из базы данных
        #self.populate_comboboxes()

        # Связываем кнопку сохранения события с методом save_event
        self.saveButton.clicked.connect(self.save_event)

    # def populate_comboboxes(self):
    #     # Реализуйте заполнение выпадающих списков данными из базы данных
    #     # Пример:
    #     # places = self.db_connection.fetch_data("SELECT name FROM places;")
    #     # self.placeComboBox.addItems(places)

    def save_event(self):
        # Получаем данные из интерфейса
        status = self.statusComboBox.currentText()
        title = self.titleLineEdit.text()
        place = self.placeComboBox.currentText()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        time = self.timeEdit.time().toString("hh:mm")
        related = self.relatedComboBox.currentText()
        correspondent = self.correspondentComboBox.currentText()
        operator = self.operatorComboBox.currentText()
        driver = self.driverComboBox.currentText()
        equipment = self.equipmentComboBox.currentText()
        author = self.authorComboBox.currentText()
        additional_info = self.additionalTextEdit.toPlainText()

        # Выполняем запрос к базе данных для сохранения события
        query = f"INSERT INTO events (status, title, place, date, time, related, correspondent, " \
                f"operator, driver, equipment, author, additional_info) VALUES " \
                f"('{status}', '{title}', '{place}', '{date}', '{time}', '{related}', '{correspondent}', " \
                f"'{operator}', '{driver}', '{equipment}', '{author}', '{additional_info}')"
        self.db_connection.execute_query(query)

        print("Event saved successfully!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    event_manager = EventManager()
    event_manager.show()
    app.exec()
