from PyQt5.QtCore import *
import pykorbit
import Scraping


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            BTC = Scraping.Currency("BTC")
            price = BTC.get_last()
            # price = pykorbit.get_current_price("BTC")

            self.BTC_price.emit(str(price))

            currentTime = QTime.currentTime()
            self.cur_time.emit(currentTime.toString("hh:mm:ss"))
            self.sleep(1)
