from PyQt5 import QtWidgets
from windows.LoginWindow import LoginWindow
from Db.DbContext import DbContext
from dotenv import load_dotenv
import sys

load_dotenv()

app = QtWidgets.QApplication([])
window = LoginWindow(DbContext())
window.show()
 
sys.exit(app.exec())