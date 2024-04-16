from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class AddUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Добавить пользователя')

        self.login_label = QLabel('Логин:')
        self.login_input = QLineEdit()

        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.group_label = QLabel('Группа:')
        self.group_input = QLineEdit()

        self.submit_button = QPushButton('Добавить')

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        
