from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AddTemplateDialog(QDialog):
    def __init__(self, parent=None):
        super(AddTemplateDialog, self).__init__(parent)
        self.setWindowTitle("Добавить новый шаблон")
        self.setModal(True)  # Чтобы диалоговое окно было модальным
        layout = QVBoxLayout(self)

        # Добавляем поля для ввода данных нового шаблона
        self.name_label = QLabel("Название:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.description_label = QLabel("Описание:")
        self.description_input = QLineEdit()
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)

        self.columns_label = QLabel("Столбцы (введите через запятую):")
        self.columns_input = QLineEdit()
        layout.addWidget(self.columns_label)
        layout.addWidget(self.columns_input)

        # Добавляем кнопки "ОК" и "Отмена"
        self.ok_button = QPushButton("ОК")
        self.cancel_button = QPushButton("Отмена")
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)

        # Подключаем сигналы нажатия кнопок к соответствующим методам
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    # Методы для получения данных из полей ввода
    def getTemplateData(self):
        name = self.name_input.text()
        description = self.description_input.text()
        columns = [col.strip() for col in self.columns_input.text().split(",")]
        return name, description, columns
    


class TemplateDialog(QDialog):
    def __init__(self, template_data):
        super().__init__()
        self.setWindowTitle("Просмотр шаблона")

        # Создаем метки для отображения данных о шаблоне
        name_label = QLabel(f"Название: {template_data['name']}")
        description_label = QLabel(f"Описание: {template_data['description']}")
        columns_label = QLabel(f"Столбцы: {template_data['columns']}")

        # Создаем вертикальный макет и добавляем метки
        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(description_label)
        layout.addWidget(columns_label)

        # Устанавливаем макет для диалогового окна
        self.setLayout(layout)    