import Bithumb
# from pandas import DataFrame


class Alarm:
    def __init__(self):
        self.bithumb = Bithumb.Ticker()

    def bull_market(self, ticker):
        price = self.bithumb.get_current_price(ticker)
        df = self.bithumb.get_ochlv(ticker)
        close = df['close']

        ma5 = close.rolling(5).mean()
        last_ma5 = ma5[-2]

        state = None
        if price > last_ma5:
            state = "상승"
        else:
            state = "하락"

        return price, last_ma5, state


# alarm의 롤은
# 데이터 분석
# 화면에 보여주기 위한 재가공?

    # https://api.bithumb.com/public/candlestick/{order_currency}_{payment_currency}/{chart_intervals}
# https://api.bithumb.com/public/candlestick/BTC_KRW/24h