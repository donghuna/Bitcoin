from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import ThreadManager


# Load window UI made by Qt Designer
form_class = uic.loadUiType("Resources/mainWindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Window position, size
        self.setGeometry(200, 200, 300, 400)
        # title
        self.setWindowTitle("BitCoin")
        # icon
        self.setWindowIcon(QIcon("Resources/Icon/bitcoin_icon.png"))

        self.worker = ThreadManager.Worker()
        self.worker.start()
        self.worker.BTC_price.connect(self.signal1_emitted)
        self.worker.cur_time.connect(self.signal2_emitted)

    @pyqtSlot(str)
    def signal1_emitted(self, price):
        self.lineEdit.setText(price)

    @pyqtSlot(str)
    def signal2_emitted(self, str_time):
        self.statusBar().showMessage(str_time)