from PyQt5.QtWidgets import QFileDialog
from openpyxl import Workbook

class ExcelHandler:
    @staticmethod
    def save_template_as_excel(template_data):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(None, "Сохранить шаблон как", "", "Excel Files (*.xlsx)", options=options)
        if file_name:
            workbook = Workbook()
            sheet = workbook.active

            # Здесь можно заполнить лист Excel данными вашего шаблона
            # Например:
            # sheet['A1'] = 'Название'
            # sheet['B1'] = 'Описание'
            # sheet['C1'] = 'Столбцы'
            # Далее заполните остальные ячейки данными из вашего шаблона

            # Сохраняем книгу Excel под указанным именем
            workbook.save(file_name)
