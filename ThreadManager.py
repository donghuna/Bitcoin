from PyQt5.QtCore import *
import Bithumb
import Alarm
import time
import datetime


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)
    QTable_controller = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.bithumb = Bithumb.Ticker()
        # TODO : ticker selection method?
        self.tickers = ["BTC", "ETH", "BCH", "ETC"]
        self.alarm = Alarm.Alarm()
        self.delay = 0.5

    def run(self):
        while True:
            data = {}

            for ticker in self.tickers:
                data[ticker] = self.alarm.bull_market(ticker)

            self.QTable_controller.emit(data)
            time.sleep(self.delay)

