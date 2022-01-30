import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

# Load window UI made by Qt Designer
form_class = uic.loadUiType("mainWindow.ui")[0]


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            price = pykorbit.get_current_price("BTC")
            self.BTC_price.emit(str(price))

            currentTime = QTime.currentTime()
            self.cur_time.emit(currentTime.toString("hh:mm:ss"))
            self.sleep(1)


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

        self.worker = Worker()
        self.worker.start()
        self.worker.BTC_price.connect(self.signal1_emitted)
        self.worker.cur_time.connect(self.signal2_emitted)

    @pyqtSlot(str)
    def signal1_emitted(self, price):
        self.lineEdit.setText(price)

    @pyqtSlot(str)
    def signal2_emitted(self, str_time):
        self.statusBar().showMessage(str_time)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
