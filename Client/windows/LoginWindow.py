from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from Forms.login import Ui_LoginWindow
from Db.DbContext import DbContext
from main import main
from utils.Utils import Utils
 
class LoginWindow(QMainWindow):
    def __init__(self, context: DbContext):
        super(LoginWindow, self).__init__()
        
        self.dbContext = context
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        
        self.ui.LineEditLogin.setText('admin')
        self.ui.LineEditPassword.setText('admin')
        
    def login(self):       
        user = self.dbContext.user.getByLogPass(self.ui.LineEditLogin.text(), self.ui.LineEditPassword.text())
        if user:
            self.main = main(self.dbContext, user[0])
            self.main.show()
            self.hide()
        else:
            msg_box = Utils.createDialog("Ошибка", "Неверный логин или пароль", QMessageBox.Warning)
            msg_box.exec_() 