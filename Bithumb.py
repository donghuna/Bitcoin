import requests

# 요청 당시 빗썸 거래소 가상자산 현재가 정보를 제공합니다.
# https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}
# 빗썸의 공개 API는 초당 20회 호출할 수 있습니다

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


class Ticker:
    def __init__(self):
        self.ticker_url = "https://api.bithumb.com/public/ticker/{}_{}"
        self.orderbook_url = "https://api.bithumb.com/public/orderbook/{}_{}"
        self.candlestick_url = "https://api.bithumb.com/public/candlestick/{}_{}/{}"
        self.tickers = self._get_ticker_list()
        self.all_ticker_data = {}
        self.candlestick_data = {}

    def _send_rest_api(self, mode, order_currency, payment_currency):
        if mode == "Ticker":
            url = self.ticker_url.format(order_currency, payment_currency)
        elif mode == "Orderbook":
            url = self.orderbook_url.format(order_currency, payment_currency)
        r = requests.get(url)
        return r.json()

    def _get_ticker_list(self):
        rtn = []
        self.get_all_ticker_data()
        self.check_status()
        for key in self.all_ticker_data['data'].keys():
            rtn.append(key)
        rtn.pop()   # because of last one is 'date'
        return rtn

    def get_all_ticker_data(self):
        self.all_ticker_data = self._send_rest_api("Ticker", "ALL", "KRW")

    def get_all_tickers(self):
        return self.tickers

    def check_status(self):
        # TODO : raise error message
        if self.all_ticker_data['status'] != '0000':
            return False
        return True

    def get_current_price(self, ticker):
        self.get_all_ticker_data()
        self.check_status()
        return int(self.all_ticker_data['data']['date']), self.all_ticker_data['data'][ticker]['closing_price']

    def get_market_detail(self, ticker):
        # TODO : return value which I need
        self.get_all_ticker_data()
        self.check_status()
        rtn = ()
        self.all_ticker_data['data'][ticker]['min_price']
        self.all_ticker_data['data'][ticker]['max_price']
        self.all_ticker_data['data'][ticker]['min_price']
        self.all_ticker_data['data'][ticker]['min_price']
        return None

    def get_orderbook(self, ticker):
        orderbook_data = self._send_rest_api("Orderbook", "ALL", "KRW")
        print(orderbook_data['data'][ticker]['bids'][0])
        return orderbook_data

    def _renewal_candlestick(self, ticker):
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

    def get_ochlv(self, ticker):
        if not self._renewal_candlestick(ticker):
            return False
        # str(datetime.datetime.fromtimestamp(timestamp / 1000))
        print(self.candlestick_data)








"""
# from bs4 import BeautifulSoup
url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_per")
print(tags)
tag = tags[0]
print(tag.text)

# tags = soup.select("table tbody tr td em")
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")

print(len(tags))
for tag in tags:
    print(tag.text)
"""