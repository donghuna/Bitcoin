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

    def bull_market(self, ticker):
        """
        Qtable에 표시하기 위한 데이터.
        상승장, 하락장 여부를 판단,
        :param ticker:
        :return: 현재가격, 5일평균, "상승" or "하락"
        """
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

    def get_target_price(self, ticker):
        """
        가격 변동폭 계산: 투자하려는 가상화폐의 전일 고가(high)에서 전일 저가(low)를 빼서 가상화폐의 가격 변동폭 계산
        매수 기준: 당일 시간에서 (변동폭 * 0.5) 이상 상승하면 해당 가격에 바로 매수
        :param ticker:
        :return:    매수 기준에 적합하면 True를 리턴
        """

        # price = self.bithumb.get_current_price(ticker)
        df = self.bithumb.get_ochlv(ticker)
        yesterday = df.iloc[-2]

        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * 0.5

        return target
