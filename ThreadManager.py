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
        self.now = datetime.datetime.now()
        self.mid = datetime.datetime(self.now.year, self.now.month, self.now.day) + datetime.timedelta(1)

    def run(self):
        while True:
            data = {}
            self.bithumb.renewal_all_ticker_data()

            for ticker in self.tickers:
                data[ticker] = self.alarm.bull_market(ticker)

            self.QTable_controller.emit(data)

            if self.midnight_timer():
                self.bithumb.sell(0)

            time.sleep(self.delay)

    def midnight_timer(self):
        self.now = datetime.datetime.now()
        if self.mid < self.now < self.mid + datetime.timedelta(seconds=20):
            self.mid = datetime.datetime(self.now.year, self.now.month, self.now.day) + datetime.timedelta(1)
            return True
        return False

