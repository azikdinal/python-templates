from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Forms.main import Ui_MainWindow
from windows.CalendarWindow import CalendarWindow
from Db.DbContext import DbContext
from Db.User import User
from utils.Utils import Utils
from dialogs.SelectEditDialog import SelectEditDialog
from dialogs.AddTemplateDialog import AddTemplateDialog
from widgets.TemplateWidget import TemplateWidget
from utils.excel_handler import ExcelHandler
from data_filter import DataFilter
from dialogs.EditorDialog import EditorDialog

class main(QMainWindow):
    def __init__(self, dbContext: DbContext, user: User):
        super(main, self).__init__()
        self.dbContext = dbContext
        self.user = user
        self.data_filter = DataFilter(dbContext)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dellButton.setVisible(False)
        self.ui.calendarLayput.setVisible(False)
        self.ui.oneButton.clicked.connect(self.oneButtonClick)
        self.ui.twoButton.clicked.connect(self.twoButtonClick)
        self.ui.dellButton.clicked.connect(self.dellButtonClick)
        self.ui.addButton.clicked.connect(self.addEventButton)

        # Создаем экземпляр selectEdit
        self.selectEdit = SelectEditDialog(dbContext)

        self.setUiGroup(user['group_id'])

        # Привязываем метод для создания шаблона к действию "Создать шаблон"
        self.ui.action_2.triggered.connect(self.addTemplate)
        # Привязываем методы для изменения и удаления шаблона к соответствующим действиям
        self.ui.action_3.triggered.connect(self.editTemplate)
        self.ui.action_4.triggered.connect(self.deleteTemplate)

        # Назначаем действие кнопке "Сохранить как"
        self.ui.action.setText("Сохранить как")
        self.ui.action.triggered.connect(self.save_as_excel)

        # Определение таблицы, из которой нужно получить данные
        self.table = 'templates'  # Измените на вашу таблицу

        # Привязываем метод для открытия шаблона к действию "Открыть шаблон"
        self.ui.action_5.triggered.connect(self.open_template)

        # Привязываем метод для фильтрации данных к кнопке "Фильтр"
        self.ui.filterButton.clicked.connect(self.filter_data)
        
        self.ui.editButton.clicked.connect(self.edit)

        self.ui.tableView.setModel(Utils.toTableModel([]))

        self.CalendarWindow = CalendarWindow()

        # self.ui.searchButton.clicked.connect(self.searchButtonClicked)
        # self.ui.filterButton.clicked.connect(self.filterButtonClicked)


    def oneButtonClick(self):
        if self.CalendarWindow.isHidden():
            self.CalendarWindow.show()
        else:
            self.CalendarWindow.hide()

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

    def setUiGroup(self, group: int):
        if group == 1:
            self.ui.menu_2.show()
            self.ui.deleteButton.setVisible(True)
        elif group == 2:
            self.ui.menu_2.hide()
            self.ui.deleteButton.setVisible(False)

    def addEventButton(self):
        self.selectEdit.exec()

    def addTemplate(self):
        # Создаем экземпляр диалогового окна для добавления нового шаблона
        dialog = AddTemplateDialog(self)
        
        # Если пользователь нажал "ОК" в диалоговом окне
        if dialog.exec_() == QDialog.Accepted:
            # Получаем данные о новом шаблоне из диалогового окна
            name, description, columns = dialog.getTemplateData()
            
            # Теперь вы можете использовать эти данные для добавления нового шаблона в базу данных
            # Например:
            new_template = TemplateWidget(name=name, description=description, columns=columns)
            self.dbContext.add_template(new_template)

    def editTemplate(self):
        # Получаем выбранный шаблон из таблицы
        selected_row = self.ui.tableView.currentIndex().row()
        if selected_row != -1:
            selected_template = self.dbContext.get_template_by_index(selected_row)

            # Открываем диалоговое окно для редактирования существующего шаблона
            dialog = AddTemplateDialog(self)
            dialog.setWindowTitle("Изменить шаблон")
            
            # Заполняем поля диалогового окна данными выбранного шаблона
            dialog.name_input.setText(selected_template.name)
            dialog.description_input.setText(selected_template.description)
            dialog.columns_input.setText(", ".join(selected_template.columns))

            # Если пользователь нажал "ОК" в диалоговом окне
            if dialog.exec_() == QDialog.Accepted:
                # Получаем отредактированные данные из диалогового окна
                name, description, columns = dialog.getTemplateData()

                # Обновляем информацию о шаблоне в базе данных
                selected_template.name = name
                selected_template.description = description
                selected_template.columns = columns
                self.dbContext.update_template(selected_template)

    def deleteTemplate(self):
        # Получаем выбранный шаблон из таблицы
        selected_row = self.ui.tableView.currentIndex().row()
        if selected_row != -1:
            selected_template = self.dbContext.get_template_by_index(selected_row)
            
            # Удаляем выбранный шаблон из базы данных
            self.dbContext.delete_template(selected_template)


    def save_as_excel(self):
        template_data = self.get_template_data()  # Получаем данные шаблона
        if template_data:
            ExcelHandler.save_template_as_excel(template_data)  # Сохраняем шаблон в Excel
        else:
            QMessageBox.warning(self, "Предупреждение", "Нет данных для сохранения")


    def get_template_data(self):
        # Здесь добавьте логику для получения данных о шаблоне
        # Например, если у вас есть какой-то элемент интерфейса, отображающий данные о шаблоне,
        # то вы можете использовать его для получения этих данных
        pass        

    def open_template(self):
        # Получаем список названий всех шаблонов из базы данных
        template_names = self.dbContext.get_all_template_names()

        if template_names:
            # Если список названий шаблонов успешно получен из базы данных,
            # создаем выпадающий список и заполняем его этими названиями
            self.templateComboBox = QComboBox()
            self.templateComboBox.addItems(template_names)
            self.templateComboBox.currentIndexChanged.connect(self.on_template_selected)
            self.templateComboBox.show()
        else:
            QMessageBox.warning(self, "Предупреждение", "Не удалось загрузить данные шаблонов из базы данных")

    def on_template_selected(self, index):
        # Получаем выбранное имя шаблона из выпадающего списка
        selected_template = self.templateComboBox.currentText()

        # Получаем данные выбранного шаблона по его имени из базы данных
        template_data = self.dbContext.get_template_by_name(selected_template)

        if template_data:
            # Если данные шаблона успешно получены из базы данных,
            # создаем новую вкладку или окно и отображаем данные шаблона в ней
            template_window = TemplateWidget(template_data)
            template_window.setWindowTitle(selected_template)
            self.ui.templateTabs.addTab(template_window, selected_template)
            self.ui.templateTabs.setCurrentWidget(template_window)
        else:
            QMessageBox.warning(self, "Предупреждение", "Не удалось загрузить данные выбранного шаблона из базы данных")






    def filter_data(self):
        # Получаем критерии фильтрации из полей ввода
        author = self.ui.LineEditAuthor.text()
        name = self.ui.LineEditName.text()
        guest = self.ui.LineEditGuest.text()
        place = self.ui.LineEditPlace.text()

        # Выполняем фильтрацию данных с помощью объекта DataFilter
        filtered_data = self.data_filter.filter_data(author, name, guest, place)

        # Обновляем данные в таблице
        self.update_table(filtered_data)

    def update_table(self, data):
        # Здесь обновляется отображение таблицы с учетом отфильтрованных данных
        pass    

    def edit(self):
        selected_row = self.ui.tableView.currentIndex()
        event_data = self.ui.tableView.model().data(selected_row)

        # Здесь вы можете реализовать логику редактирования события,
        # например, создавая экземпляр окна редактирования и передавая данные события в него
        # или вызывая методы редактирования непосредственно из основного окна.

        # Пример:
        editor_window = EditorDialog(self.dbContext)
        editor_window.edit(event_data)
        editor_window.exec_()
