from PyQt5.QtCore import *
import Bithumb
import Controller
import time
import datetime
import logging


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)
    QTable_controller = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.bithumb = Bithumb.Bithumb()
        self.controller = Controller.Controller()
        # TODO : ticker selection method?
        self.tickers = ["BTC", "ETH"]
        self.delay = 0.5
        self.now = datetime.datetime.now()
        self.mid = datetime.datetime(self.now.year, self.now.month, self.now.day) + datetime.timedelta(1)

    def run(self):
        while True:
            # display
            self.bithumb.renewal_all_ticker_data()
            self.QTable_controller.emit(self.controller.gen_table_data(self.tickers))

            # sell condition
            if self.midnight_watchdog():
                self.controller.sell()

            # buy condition
            self.controller.buy()

            time.sleep(self.delay)

    # temp func for sell
    def midnight_watchdog(self):
        self.now = datetime.datetime.now()
        if self.mid < self.now < self.mid + datetime.timedelta(seconds=20):
            self.mid = datetime.datetime(self.now.year, self.now.month, self.now.day) + datetime.timedelta(1)
            return True
        return False

    def buy_watchdog(self):
        # 매수 알고리즘 성능에 따라 시간간격이 달라질 것임.
        pass
