import requests
import datetime
from pandas import DataFrame

# Bithumb.py 에서의 롤은
# API를 사용해서 데이터를 가져오는 것 까지로 제한.
# 데이터 재가공은 어디서? bithumb외에 다른 사이트는? 공통적인 수정부분이 존재?

# 요청 당시 빗썸 거래소 가상자산 현재가 정보를 제공합니다.
# https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}
"""
Public API
1초당 최대 135회 요청 가능합니다.
초과 요청을 보내면 API 사용이 제한됩니다.
Private API
1초당 최대 15회 요청 가능합니다.
초과 요청을 보내면 API 사용이 일시적으로 제한됩니다. (Public - 1분 / Private info - 5분 / Private trade - 10분)
"""

"""
필드	설명	타입
status	결과 상태 코드 (정상: 0000, 그 외 에러 코드 참조)	String
opening_price	시가 00시 기준	Number (String)
closing_price	종가 00시 기준	Number (String)
min_price	저가 00시 기준	Number (String)
max_price	고가 00시 기준	Number (String)
units_traded	거래량 00시 기준	Number (String)
acc_trade_value	거래금액 00시 기준	Number (String)
prev_closing_price	전일종가	Number (String)
units_traded_24H	최근 24시간 거래량	Number (String)
acc_trade_value_24H	최근 24시간 거래금액	Number (String)
fluctate_24H	최근 24시간 변동가	Number (String)
fluctate_rate_24H	최근 24시간 변동률	Number (String)
date	타임 스탬프	Integer(String)
"""


class Bithumb:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.all_ticker_data = {}
        self.candlestick_data = {}
        self.ticker_url = "https://api.bithumb.com/public/ticker/{}_{}"
        self.orderbook_url = "https://api.bithumb.com/public/orderbook/{}_{}"
        self.candlestick_url = "https://api.bithumb.com/public/candlestick/{}_{}/{}"
        self.tickers = self._get_ticker_list()

    def _send_rest_api(self, mode, order_currency, payment_currency):
        if mode == "Ticker":
            url = self.ticker_url.format(order_currency, payment_currency)
        elif mode == "Orderbook":
            url = self.orderbook_url.format(order_currency, payment_currency)
        r = requests.get(url)
        return r.json()

    def _get_ticker_list(self):
        rtn = []
        self.renewal_all_ticker_data()
        if not self.check_status(self.all_ticker_data['status']):
            return None

        for key in self.all_ticker_data['data'].keys():
            rtn.append(key)
        rtn.pop()   # because of last one is 'date'
        return rtn

    def renewal_candlestick(self, ticker):
        # 24h {1m, 3m, 5m, 10m, 30m, 1h, 6h, 12h, 24h 사용 가능}
        chart_intervals = "24h"

        url = self.candlestick_url.format(ticker, "KRW", chart_intervals)
        r = requests.get(url)
        tmp_data = r.json()
        if tmp_data['status'] == "0000":
            self.candlestick_data[ticker] = tmp_data
            return True
        else:
            return False

    def renewal_all_ticker_data(self):
        """
        모든 ticker에 대한 가격정보를 리뉴얼
        :return:
        """
        self.all_ticker_data = self._send_rest_api("Ticker", "ALL", "KRW")
        # print(self.all_ticker_data['data']['BTC']['closing_price'])

    def get_all_tickers(self):
        return self.tickers

    @staticmethod
    def check_status(status):
        # TODO : raise error message
        if status != '0000':
            return False
        return True

    def get_current_price(self, ticker):
        # TODO : need renewal data?
        return int(self.all_ticker_data['data'][ticker]['closing_price'])

    def get_orderbook(self, ticker):
        orderbook_data = self._send_rest_api("Orderbook", "ALL", "KRW")
        # print(orderbook_data['data'][ticker]['bids'][0])
        return orderbook_data

    def get_ochlv(self, ticker):
        if not self.renewal_candlestick(ticker):
            return False

        # TODO : need this seq?
        for i in self.candlestick_data[ticker]['data']:
            i[0] = self._timestamp_to_datetime(i[0])

        # 시가, 종가, 고가, 저가, 거래량
        df = DataFrame(self.candlestick_data[ticker]['data'])
        df.columns = ["date", "open", "close", "high", "low", "volume"]
        df.set_index("date", inplace=True)
        df = df.astype({"open": int, "close": int, "high": int, "low": int, "volume": float})
        return df

    # 잔고 조회
    def get_balance(self, ticker):
        """
        ticker : 조회할 가상화폐 ticker
        :return: 비트코인의 총 잔고, 거래 중인 비트코인의 수량, 보유 중인 총원화, 주문에 사용된 원화를
        """
        # temp return
        return 100

    def sell_market_order(self, ticker, unit):
        pass

    # sell strategy 1. 보유 중인 비트코인을 다음 날 시초가에 전량 매도
    def sell(self, ticker):
        unit = self.get_balance(ticker)
        self.sell_market_order(ticker, unit)

    def buy_market_order(self, ticker, unit):
        pass

    # buy strategy 1. 목표가가 현재가 이상일 경우 잔고를 조회하고 주문 가능한 수량을 계산한 후에 시장가 매수
    def buy_crypto_currency(self, ticker):
        krw = self.get_balance("KRW")  # 잔고 확인
        orderbook = self.get_orderbook(ticker)
        sell_price = orderbook['asks'][0]['price']
        unit = krw / float(sell_price)
        self.buy_market_order(ticker, unit)

    @staticmethod
    def _timestamp_to_datetime(timestamp):
        _date = datetime.datetime.fromtimestamp(int(timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
        return _date


