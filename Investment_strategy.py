"""
Bithumb 외 다른 거래소를 이용하더라도 공동으로 사용될 수 있는 interface를 갖추고,
투자 전략, 변동성 돌파, 수치해석을 위한 메소드들을 제공한다.
추후에 DL 모델을 이곳에서 사용하는 것이 좋을 것 같다.
"""
import Bithumb


class InvestmentStrategy:
    def __init__(self):
        self.bithumb = Bithumb.Bithumb()
        pass

    # Moving Average 5 days
    def get_yesterday_ma5(self, ticker):
        df = self.bithumb.get_ochlv(ticker)
        close = df['close']
        ma = close.rolling(window=5).mean()
        return ma[-2]
        # print(ma, ma[-2])

