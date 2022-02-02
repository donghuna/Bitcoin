from PyQt5.QtCore import *
import Bithumb
import time
import datetime
# import pykorbit
# import Scraping


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.delay = 0.5

    def run(self):
        while True:
            # BTC = Scraping.Currency("BTC")
            # price = BTC.get_last()
            # price = pykorbit.get_current_price("BTC")
            bithumb = Bithumb.Ticker()
            bithumb.get_orderbook("BTC")
            timestamp, price = bithumb.get_current_price("BTC")
            bithumb.get_ochlv("BTC")


            self.BTC_price.emit(str(price))

            # currentTime = QTime.currentTime()
            # self.cur_time.emit(currentTime.toString("hh:mm:ss"))

            self.cur_time.emit(str(datetime.datetime.fromtimestamp(timestamp / 1000)))
            time.sleep(self.delay)
