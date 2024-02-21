from PyQt5 import QtWidgets, uic
import sys
import pathlib
 
app = QtWidgets.QApplication([])
win = uic.loadUi(f"{pathlib.Path().resolve()}/Client/Forms/main.ui")
 
win.show()
sys.exit(app.exec())