import Bithumb
import Investment_strategy


class Controller:
    def __init__(self):
        self.bithumb = Bithumb.Bithumb()
        self.IS = Investment_strategy.InvestmentStrategy()
        self.buy_amount = 1

    def buy(self):
        current_price = self.bithumb.get_last_updated_price("BTC")
        if (current_price > self.IS.get_target_price("BTC")) and \
                (current_price > self.IS.get_yesterday_ma5("BTC")):
            self.bithumb.buy_crypto_currency("BTC")

    def sell(self):
        pass

    def gen_table_data(self, tickers):
        pass
        data = {}
        for ticker in tickers:
            data[ticker] = self.IS.bull_market(ticker)
        return data
