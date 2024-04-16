from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class Template(QWidget):
    def __init__(self, template):
        super().__init__()

        self.template = template

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Создаем виджеты для отображения информации о шаблоне
        if isinstance(self.template, list):  # Проверяем, является ли self.template списком
            columns_label = QLabel(f"Столбцы: {', '.join(self.template)}")
        else:
            columns_label = QLabel(f"Столбец: {self.template}")  # Если self.template не список, то считаем его строкой

        # Добавляем виджет на вертикальный макет
        layout.addWidget(columns_label)

        # Устанавливаем макет для окна
        self.setLayout(layout)
