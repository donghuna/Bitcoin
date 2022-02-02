from PyQt5.QtCore import *
import Bithumb
import Alarm
import time
import datetime
# import pykorbit
# import Scraping


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.bithumb = Bithumb.Ticker()
        self.alarm = Alarm.Alarm()
        self.delay = 0.5

    def run(self):
        while True:
            self.bithumb.get_orderbook("BTC")
            timestamp, price = self.bithumb.get_current_price("BTC")

            self.BTC_price.emit(str(price))
            self.alarm.tmp()

            self.cur_time.emit(str(datetime.datetime.fromtimestamp(timestamp / 1000)))
            time.sleep(self.delay)
