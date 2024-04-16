from PyQt5 import QtWidgets, uic
from Forms.calendar import Ui_CalendarWindow
from datetime import date
import sys

class CalendarWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.ui = Ui_CalendarWindow()
        self.ui.setupUi(self)

        # Подключаем событие изменения даты в календаре
        self.ui.calendarWidget_2.clicked.connect(self.date_selected)


    def date_selected(self):
        # Получаем выбранную дату из календаря
        selected_date = self.ui.calendarWidget_2.selectedDate().toPyDate()

        print(f"Selected date: {selected_date}")

# Пример использования
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    calendar_window = calendarWindow()
    calendar_window.show()
    sys.exit(app.exec())
