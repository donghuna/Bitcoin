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

    def strategy_1(self, ticker):
        """
        가격 변동폭 계산: 투자하려는 가상화폐의 전일 고가(high)에서 전일 저가(low)를 빼서 가상화폐의 가격 변동폭 계산
        매수 기준: 당일 시간에서 (변동폭 * 0.5) 이상 상승하면 해당 가격에 바로 매수
        매도 기준: 당일 종가에 매도
        :param ticker:
        :return:
        """

        price = self.bithumb.get_current_price(ticker)
        df = self.bithumb.get_ochlv(ticker)
        yesterday = df.iloc[-2]

        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * 0.5

        if target < price:
            return True
        else:
            return False




# alarm의 롤은
# 데이터 분석
# 화면에 보여주기 위한 재가공까지?
