from PyQt5.QtCore import *
import Bithumb
import Alarm
import time
import Investment_strategy
import datetime


class Worker(QThread):
    BTC_price = pyqtSignal(str)
    cur_time = pyqtSignal(str)
    QTable_controller = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.bithumb = Bithumb.Bithumb()
        self.IS = Investment_strategy.InvestmentStrategy()
        # TODO : ticker selection method?
        self.tickers = ["BTC", "ETH", "BCH", "ETC"]
        self.alarm = Alarm.Alarm()
        self.delay = 0.5
        self.now = datetime.datetime.now()
        self.mid = datetime.datetime(self.now.year, self.now.month, self.now.day) + datetime.timedelta(1)

    def run(self):
        while True:
            # display
            data = {}
            self.bithumb.renewal_all_ticker_data()

            for ticker in self.tickers:
                data[ticker] = self.alarm.bull_market(ticker)

            self.QTable_controller.emit(data)

            # sell condition
            if self.midnight_watchdog():
                self.bithumb.sell(0)

            # buy condition
            current_price = self.bithumb.get_current_price("BTC")
            if current_price > self.alarm.get_target_price("BTC"):
                self.bithumb.buy_crypto_currency("BTC")


            # test
            self.BTC_price.emit(str(self.IS.get_yesterday_ma5("BTC")))

            time.sleep(self.delay)

    # temp func for sell
    def midnight_watchdog(self):
        self.now = datetime.datetime.now()
        if self.mid < self.now < self.mid + datetime.timedelta(seconds=20):
            self.mid = datetime.datetime(self.now.year, self.now.month, self.now.day) + datetime.timedelta(1)
            return True
        return False

    def buy_watchdog(self):
        pass
