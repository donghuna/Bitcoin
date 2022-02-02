import Bithumb
# from pandas import DataFrame


class Alarm:
    def __init__(self):
        self.bithumb = Bithumb.Ticker()

    def bull_market(self, current_price):
        df = self.bithumb.get_ochlv("BTC")
        close = df['close']

        ma5 = close.rolling(5).mean()
        last_ma5 = ma5[-2]

        if current_price > last_ma5:
            print("up")
        else:
            print("down")





    # https://api.bithumb.com/public/candlestick/{order_currency}_{payment_currency}/{chart_intervals}
# https://api.bithumb.com/public/candlestick/BTC_KRW/24h