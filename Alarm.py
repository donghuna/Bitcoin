import Bithumb
# from pandas import DataFrame


class Alarm:
    def __init__(self):
        self.bithumb = Bithumb.Ticker()

    def tmp(self):
        df = self.bithumb.get_ochlv("BTC")
        close = df['close']

        print(close)
        print(close.dtypes)
        print((close[0] + close[1] + close[2] + close[3] + close[4]) / 5)
        print((close[1] + close[2] + close[3] + close[4] + close[5]) / 5)
        print((close[2] + close[3] + close[4] + close[5] + close[6]) / 5)


    # https://api.bithumb.com/public/candlestick/{order_currency}_{payment_currency}/{chart_intervals}
# https://api.bithumb.com/public/candlestick/BTC_KRW/24h