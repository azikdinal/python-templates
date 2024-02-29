from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from Forms.main import Ui_MainWindow
from database_connection import DatabaseConnection
from template_manager import TemplateManager
from calendarWindow import calendarWindow
from addElementDialog import AddElementDialog
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel
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

        self.template_manager = TemplateManager(self)  # Создаем экземпляр TemplateManager
        

        self.ui.addButton.clicked.connect(self.addElementDialog.show)  # Открываем диалог добавления при нажатии кнопки "Добавить"
        self.ui.deleteButton.clicked.connect(self.deleteElement)  # Вызываем функцию удаления при нажатии кнопки "Удалить"
        self.ui.editButton.clicked.connect(self.editElement)  # Вызываем функцию редактирования при нажатии кнопки "Редактировать"
        self.ui.deleteButton.clicked.connect(self.dellButtonClick)

        self.ui.listView.setModel(QStringListModel())

        self.ui.listView.setModel(QStringListModel())  # Установка пустой модели
        self.populateListView()  # Инициализация данных в QListView

        # Заполняем список данными из базы данных
        data_from_db = self.getDataFromDatabase()
        model = self.ui.listView.model()
        model.setStringList(data_from_db)


    def addElement(self):
        self.addElementDialog.populateComboBoxes()
        if self.addElementDialog.exec_() == QDialog.Accepted:
            self.addElementDialog.saveDataToDatabase()
            self.populateListView()  # Обновление данных в QListView после добавления нового элемента


    def populateListView(self):
        # Очистите текущие данные в списке
        model = QStringListModel()
        self.ui.listView.setModel(model)

        # Получите данные из базы данных
        data_from_db = self.getDataFromDatabase()

        # Если есть данные, добавьте их в модель
        if data_from_db:
            model.setStringList(data_from_db)
            self.ui.listView.setModel(model)

    def updateListView(self):
        # Получите данные из базы данных
        data = self.getDataFromDatabase()

        # Обновите модель QListView
        model = self.ui.listView.model()
        model.setStringList(data)        
 

    def getDataFromDatabase(self):
        db_connection = DatabaseConnection()

        try:
            # Открываем соединение с базой данных
            db_connection.connect()

            # Пример SQL-запроса для получения данных
            select_query = "SELECT title FROM events"  # Замените на ваш запрос

            # Выполняем SQL-запрос
            db_data = db_connection.fetch_data(select_query)

            # Возвращаем список названий записей
            return [data[0] for data in db_data]

        except Exception as e:
            print("Ошибка при получении данных из базы данных:", e)
            return []

        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()

    def getEnteredData(self):
        # Получение данных из элементов формы
        data = {
            "status": self.statusComboBox.currentText(),
            "title": self.titleLineEdit.text(),
            "place": self.placeComboBox.currentText(),
            "date": self.dateCalendar.selectedDate().toString("yyyy-MM-dd"),
            "time": self.startTimeEdit.time().toString("hh:mm:ss"),
            "end_time": self.endTimeEdit.time().toString("hh:mm:ss"),
            "linked": self.linkedComboBox.currentText(),
            "correspondent": self.correspondentComboBox.currentText(),
            "operator": self.operatorComboBox.currentText(),
            "driver": self.driverComboBox.currentText(),
            "equipment": self.equipmentComboBox.currentText(),
            "author": self.authorComboBox.currentText(),
            "additional_info": self.notesTextEdit.toPlainText(),
        }
        return data        


    def addElement(self):
        self.addElementDialog.populateComboBoxes()
        if self.addElementDialog.exec_() == QDialog.Accepted:
            # Получаем введенные данные
            data = self.addElementDialog.getEnteredData()

            # Добавляем элемент в базу данных
            self.addElementToDatabase(data)

            # Добавляем элемент в список
            model = self.ui.listView.model()
            model.setStringList(model.stringList() + [data["title"]])

    def addElementToDatabase(self, data):
        db_connection = DatabaseConnection()

        try:
            # Открываем соединение с базой данных
            db_connection.connect()

            insert_query = """
                INSERT INTO events (status, title, place, date, time, related, correspondent, operator, driver, equipment, author, additional_info)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Передаем данные для вставки, не указывая значение для столбца 'id'
            db_connection.cursor.execute(insert_query, (
                data["status"], data["title"], data["place"],
                data["date"], data["time"], data["linked"],
                data["correspondent"], data["operator"], data["driver"],
                data["equipment"], data["author"], data["additional_info"]
            ))


            # Подтверждаем транзакцию
            db_connection.connection.commit()

            print(f"Element '{data['title']}' added to the database.")

        except Exception as e:
            print("Ошибка при добавлении элемента в базу данных:", e)

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
                INSERT INTO events (status, title, place, date, time, end_time, related, correspondent, operator, driver, equipment, author, additional_info)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Передаем данные для вставки
            db_connection.cursor.execute(insert_query, (
                data["status"], data["title"], data["place"], data["date"],
                data["time"], data["end_time"], data["linked"], data["correspondent"],
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

    def editRecord(self, record_id):
        # Получение данных из элементов формы
        data = self.getEnteredData()

        # Создаем экземпляр класса DatabaseConnection
        db_connection = DatabaseConnection()

        try:
            # Устанавливаем соединение с базой данных
            db_connection.connect()

            # Пример запроса для редактирования данных в таблице events
            edit_query = """
                UPDATE events 
                SET status=%s, title=%s, place=%s, date=%s, time=%s, end_time=%s, related=%s, correspondent=%s,
                    operator=%s, driver=%s, equipment=%s, author=%s, additional_info=%s
                WHERE id=%s
            """
            # Передаем данные для редактирования
            db_connection.cursor.execute(edit_query, (
                data["status"], data["title"], data["place"], data["date"],
                data["time"], data["end_time"], data["linked"], data["correspondent"],
                data["operator"], data["driver"], data["equipment"],
                data["author"], data["additional_info"], record_id
            ))

            # Подтверждаем транзакцию
            db_connection.connection.commit()

            # Закрываем диалог
            self.accept()

        except Exception as e:
            print("Ошибка при редактировании записи в базе данных:", e)

        finally:
            # Закрываем соединение с базой данных в блоке finally,
            # чтобы убедиться, что соединение закрыто даже в случае ошибки
            db_connection.close_connection()             

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
        selected_item = self.ui.listView.selectionModel().selectedIndexes()
        if selected_item:
            selected_item = selected_item[0]
            item_to_delete = selected_item.data()
            # Удаление элемента из базы данных
            self.deleteElementFromDatabase(item_to_delete)
            self.populateListView()  # Обновление данных в QListView после удаления элемента
        else:
            print("Выберите элемент для удаления.")

            print("Deleting element...")

        # Обновление QListView
        self.updateListView()


    def deleteElementFromDatabase(self, item_to_delete):
        db_connection = DatabaseConnection()

        try:
            # Открываем соединение с базой данных
            db_connection.connect()

            # Пример SQL-запроса для удаления данных
            delete_query = "DELETE FROM events WHERE title = %s"  # Замените на ваш запрос

            # Выполняем SQL-запрос с передачей параметра
            db_connection.cursor.execute(delete_query, (item_to_delete,))

            # Подтверждаем транзакцию
            db_connection.connection.commit()

            print(f"Element '{item_to_delete}' deleted from the database.")

        except Exception as e:
            print("Ошибка при удалении элемента из базы данных:", e)

        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()

        # После удаления обновляем список в интерфейсе
        self.populateListView()
        

    def editElement(self):
        selected_item = self.ui.listView.selectionModel().selectedIndexes()
        if selected_item:
            selected_item = selected_item[0]
            record_id = selected_item.data(Qt.UserRole)
            title_to_edit = selected_item.data()
            edit_dialog = AddElementDialog(self, data_to_edit={"title": title_to_edit})
            if edit_dialog.exec_() == QDialog.Accepted:
                edited_data = edit_dialog.getEnteredData()
                print(f"Editing element: {title_to_edit} -> {edited_data['title']}")
                # Редактирование элемента в базе данных
                edit_dialog.editRecord(record_id)
                self.populateListView()  # Обновление данных в QListView после редактирования элемента

                print(f"Editing element: {title_to_edit} -> {edited_data['title']}")

            # Обновление QListView
            self.updateListView()
        else:
            print("Выберите элемент для редактирования.")

            


    def editElementInDatabase(self, old_title, new_data):
        db_connection = DatabaseConnection()

        try:
            # Открываем соединение с базой данных
            db_connection.connect()

            # Пример SQL-запроса для обновления данных
            update_query = """
                UPDATE events
                SET title = %s, status = %s, place = %s, date = %s, time = %s, related = %s,
                    correspondent = %s, operator = %s, driver = %s, equipment = %s,
                    author = %s, additional_info = %s
                WHERE title = %s
            """  # Замените на ваш запрос

            # Выполняем SQL-запрос с передачей параметров
            db_connection.cursor.execute(update_query, (
                new_data["title"], new_data["status"], new_data["place"],
                new_data["date"], new_data["time"], new_data["linked"],
                new_data["correspondent"], new_data["operator"], new_data["driver"],
                new_data["equipment"], new_data["author"], new_data["additional_info"],
                old_title
            ))

            # Подтверждаем транзакцию
            db_connection.connection.commit()

            print(f"Element '{old_title}' updated in the database.")

        except Exception as e:
            print("Ошибка при обновлении элемента в базе данных:", e)

        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()


    def updateElementInDatabase(self, title_to_edit, edited_data):
        db_connection = DatabaseConnection()

        try:
            # Открываем соединение с базой данных
            db_connection.connect()

            # Пример SQL-запроса для обновления данных
            update_query = """
                UPDATE events
                SET title = %s, status = %s, place = %s, date = %s, time = %s,
                    related = %s, correspondent = %s, operator = %s, driver = %s,
                    equipment = %s, author = %s, additional_info = %s
                WHERE title = %s AND date = %s
            """  # Замените на ваш запрос

            # Выполняем SQL-запрос с передачей параметров
            db_connection.cursor.execute(update_query, (
                edited_data["title"], edited_data["status"], edited_data["place"],
                edited_data["date"], edited_data["time"], edited_data["linked"],
                edited_data["correspondent"], edited_data["operator"],
                edited_data["driver"], edited_data["equipment"],
                edited_data["author"], edited_data["additional_info"],
                title_to_edit, edited_data["date"]
            ))

            # Подтверждаем транзакцию
            db_connection.connection.commit()

            print(f"Element '{title_to_edit}' updated in the database.")

        except Exception as e:
            print("Ошибка при обновлении элемента в базе данных:", e)

        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()


    def saveEditedDataToDatabase(self, old_title, edited_data):
        db_connection = DatabaseConnection()

        try:
            # Открываем соединение с базой данных
            db_connection.connect()

            # Пример SQL-запроса для обновления данных
            update_query = """
                UPDATE events
                SET title = %s, status = %s, place = %s  # Добавьте остальные поля для обновления
                WHERE title = %s
            """

            # Выполняем SQL-запрос
            db_connection.cursor.execute(
                update_query,
                (
                    edited_data["title"], edited_data["status"], edited_data["place"],  # Добавьте остальные поля
                    old_title
                )
            )

            # Подтверждаем транзакцию
            db_connection.connection.commit()

            print(f"Saving edited data to the database: {edited_data}")
        except Exception as e:
            print("Ошибка при сохранении измененных данных в базе данных:", e)
        finally:
            # Важно закрывать соединение после использования
            db_connection.close_connection()          

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