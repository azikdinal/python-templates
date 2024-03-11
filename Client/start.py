from login import login
from PyQt5 import QtWidgets
from Db.DbContext import DbContext
from dotenv import load_dotenv
import sys
load_dotenv()

app = QtWidgets.QApplication([])
window = login(DbContext())
window.show()
 
sys.exit(app.exec())