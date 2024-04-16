from PyQt5 import QtWidgets
from Forms.editor import Ui_Editor
from Db.DbContext import DbContext
from utils.Utils import Utils

class EditorDialog(QtWidgets.QDialog):
    statusBoof = {}
    placeBoof = {}
    workerBoof = {}
    linkBoof = {}
    authorBoof = {}
    equipmentBoof = {}
    
    def __init__(self, context: DbContext):
        super(EditorDialog, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_Editor()
        self.ui.setupUi(self)
        
        for link in self.dbContext.link.get():
            if 'name' in link:  
                # Обрабатываем объект link, только если есть ключ 'name'
                self.ui.LinkedLineEdit.addItem(link['name'])
                self.linkBoof[link['name']] = link['id']
            else:
                print("В данных объекта link отсутствует ключ 'name'.")



        
        for status in self.dbContext.status.get():
            self.ui.StatusCombo.addItem(status['name'])
            self.statusBoof[status['name']] = status['id']
        
        for place in self.dbContext.place.get():
            self.ui.PlaceCombo.addItem(place['name'])
            self.placeBoof[place['name']] = place['id']
            
        for worker in self.dbContext.worker.get():
            self.ui.CorrespondentLineEdit.addItem(worker['fio'])
            self.ui.OperatorLineEdit.addItem(worker['fio'])
            self.ui.DriverComboBox.addItem(worker['fio'])
            self.workerBoof[worker['id']] = worker['fio']


            
        # for link in self.dbContext.link.get():
        #     self.ui.LinkedLineEdit.addItem(link['fio'])
        #     self.linkBoof[link['name']] = link['id']
            
        for author in self.dbContext.user.get():
            if 'fio' in author:  
                # Обрабатываем объект author, только если есть ключ 'fio'
                self.ui.AuthorComboBox.addItem(author['fio'])
                self.authorBoof[author['fio']] = author['id']
            else:
                print("В данных объекта author отсутствует ключ 'fio'.")

    
            
        # for author in self.dbContext.user.get():
        #     self.ui.AuthorComboBox.addItem(author['fio'])
        #     self.authorBoof[author['name']] = author['id']
            
        for equipment in self.dbContext.equipment.get():
            self.ui.EquipmentLineEdit.addItem(equipment['name'])
            self.equipmentBoof[equipment['name']] = equipment['id']
            
        self.ui.CancelPushButton_3.clicked.connect(self.close)
        self.ui.SavePushButton.clicked.connect(self.save)
            
    def save(self):
        current_status = self.ui.StatusCombo.currentText()
        if current_status:
            res = self.dbContext.events.add(
                self.statusBoof[current_status],
                self.ui.NameLineEdit.text(),
                self.placeBoof[self.ui.PlaceCombo.currentText()],
                self.ui.DateEdit.dateTime()
            )
            if res:
                msg_box = Utils.createDialog("Готово", "Данные сохранены")
                msg_box.exec_()
        else:
            print("Ошибка: Выберите статус")
        self.close()

        

    def edit(self):
        # Получаем индекс выбранной строки
        selected_row = self.ui.tableView.currentIndex().row()

        # Получаем данные выбранного события из модели
        event_data = self.ui.tableView.model().data(selected_row)

        # Заполняем форму данными выбранного события
        self.ui.StatusCombo.setCurrentText(event_data['status'])
        self.ui.NameLineEdit.setText(event_data['name'])
        self.ui.PlaceCombo.setCurrentText(event_data['place'])
        # Продолжайте заполнение остальных полей формы

        # Показываем диалоговое окно
        self.exec_()

        # После того, как пользователь внес изменения и нажал "Сохранить",
        # обновляем запись в базе данных
        res = self.dbContext.events.update(event_data['id'],
                                        self.statusBoof[self.ui.StatusCombo.currentText()],
                                        self.ui.NameLineEdit.text(),
                                        self.placeBoof[self.ui.PlaceCombo.currentText()],
                                        self.ui.DateEdit.dateTime())
        if res:
            msg_box = Utils.createDialog("Готово", "Данные обновлены")
            msg_box.exec_()
        self.close()    


    def setupComboBoxes(self):
        # Заполнение выпадающего списка для статуса
        statuses = self.dbContext.status.get()
        for status in statuses:
            self.ui.StatusCombo.addItem(status['name'])
            
        # Заполнение выпадающего списка для места
        places = self.dbContext.place.get()
        for place in places:
            self.ui.PlaceCombo.addItem(place['name'])
            
        # Заполнение выпадающего списка для связного
        workers = self.dbContext.worker.get()
        for worker in workers:
            self.ui.CorrespondentLineEdit.addItem(worker['fio'])
            self.ui.OperatorLineEdit.addItem(worker['fio'])
            self.ui.DriverComboBox.addItem(worker['fio'])
            
        # Заполнение выпадающего списка для автора
        authors = self.dbContext.user.get()
        for author in authors:
            self.ui.AuthorComboBox.addItem(author['fio'])
            
        # Заполнение выпадающего списка для оборудования
        equipments = self.dbContext.equipment.get()
        for equipment in equipments:
            self.ui.EquipmentLineEdit.addItem(equipment['name'])    