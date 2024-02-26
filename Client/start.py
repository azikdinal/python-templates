from PyQt5 import QtWidgets, uic
import sys
import pathlib
from database_connection import DatabaseConnection

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi(f"{pathlib.Path().resolve()}/Client/Forms/login.ui", self)
        self.show()

        # Соединяем событие нажатия кнопки входа с методом handleLogin
        self.pushButton.clicked.connect(self.handleLogin)

        # Связываем событие ввода пароля с методом handleLogin
        self.LineEditPassword.returnPressed.connect(self.handleLogin)

        # Подключение к базе данных
        self.db_connection = DatabaseConnection()

        # Добавляем атрибут для хранения ссылки на главное окно
        self.main_window = None

    def handleLogin(self):
        try:
            # Получаем введенные логин и пароль
            entered_username = self.LineEditLogin.text()
            entered_password = self.LineEditPassword.text()

            # Проверяем логин и пароль в базе данных
            query = f"SELECT * FROM users WHERE username='{entered_username}' AND password='{entered_password}';"
            result = self.db_connection.fetch_data(query)

            if result:
                # Если результат не пустой, значит, пользователь существует
                print("Login successful!")
                self.close()
                
                # Создаем объект MainWindow и сохраняем ссылку на него
                self.main_window = MainWindow()
                self.main_window.show()
                
            else:
                print("Invalid username or password. Please try again.")

        except Exception as e:
            print(f"Error handling login: {e}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(f"{pathlib.Path().resolve()}/Client/Forms/main.ui", self)

        # Подключение к базе данных
        self.db_connection = DatabaseConnection()

        # Пример использования
        result = self.db_connection.fetch_data("SELECT * FROM users;")
        print(result)

        # Закрываем соединение с базой данных при закрытии окна
        self.destroyed.connect(self.close_db_connection)

    def close_db_connection(self):
        # Закрываем соединение с базой данных
        self.db_connection.close_connection()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    sys.exit(app.exec())
