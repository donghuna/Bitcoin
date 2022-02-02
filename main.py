import sys
from PyQt5.QtWidgets import *
import WindowManager


app = QApplication(sys.argv)
window = WindowManager.MyWindow()
window.show()
app.exec_()
