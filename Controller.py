import Bithumb
import Investment_strategy


class Controller:
    def __init__(self):
        self.bithumb = Bithumb.Bithumb()
        self.IS = Investment_strategy.InvestmentStrategy()

    def buy(self):
        current_price = self.bithumb.get_current_price("BTC")
        if (current_price > self.IS.get_target_price("BTC")) and \
                (current_price > self.IS.get_yesterday_ma5("BTC")):
            self.bithumb.buy_crypto_currency("BTC")

    def sell(self):
        pass
