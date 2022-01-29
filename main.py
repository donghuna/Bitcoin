import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

# Load window UI made by Qt Designer
form_class = uic.loadUiType("mainWindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Window position, size
        self.setGeometry(200, 200, 300, 400)
        # title
        self.setWindowTitle("BitCoin")
        # icon
        self.setWindowIcon(QIcon("bitcoin_icon.png"))
        # self.setWindowIcon(QIcon("bitcoin_black.png"))

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
