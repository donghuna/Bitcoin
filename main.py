import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

# Load window UI made by Qt Designer
form_class = uic.loadUiType("mainWindow.ui")[0]


class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)


class MySignal(QObject):
    # for make signal
    signal1 = pyqtSignal(float)
    signal2 = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)
        self.price = pykorbit.get_current_price("BTC")
        self.str_time = "A"

    def inquiry(self):
        self.price = pykorbit.get_current_price("BTC")
        cur_time = QTime.currentTime()
        self.str_time = cur_time.toString("hh:mm:ss")

    def run(self):
        self.signal1.emit(self.price)
        self.signal2.emit(self.str_time)


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
        # self.setWindowIcon(QIcon("bitcoin_black.png"))

        signal = MySignal()
        signal.signal1.connect(self.signal1_emitted)
        signal.signal2.connect(self.signal2_emitted)
        signal.run()

    @pyqtSlot(float)
    def signal1_emitted(self, price):
        self.lineEdit.setText(str(price))

    @pyqtSlot(str)
    def signal2_emitted(self, str_time):
        self.statusBar().showMessage(str_time)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
