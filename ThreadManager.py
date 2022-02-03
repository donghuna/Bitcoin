from PyQt5.QtCore import *
import Bithumb
import Alarm
import time
import datetime


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)
    QTable_controller = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.bithumb = Bithumb.Ticker()
        # TODO : ticker selection method?
        self.tickers = ["BTC", "ETH", "BCH", "ETC"]
        self.alarm = Alarm.Alarm()
        self.delay = 0.5

    def run(self):
        while True:
            # self.bithumb.get_orderbook("BTC")
            self.QTable_controller.emit(self.tickers)

            timestamp, price = self.bithumb.get_current_price("BTC")

            self.BTC_price.emit(str(price))
            self.alarm.bull_market(price)

            self.cur_time.emit(str(datetime.datetime.fromtimestamp(timestamp / 1000)))
            time.sleep(self.delay)
