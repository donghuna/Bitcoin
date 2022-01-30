import requests
# from bs4 import BeautifulSoup

# 요청 당시 빗썸 거래소 가상자산 현재가 정보를 제공합니다.
# https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}


class Ticker:
    def __init__(self):
        self.base_url = "https://api.bithumb.com/public/ticker/{}_{}"
        self.tickers = self.get_all_tickers_from_bithumb()

    def send_rest_api(self, order_currency, payment_currency):
        url = self.base_url.format(order_currency, payment_currency)
        r = requests.get(url)
        return r.json()

    def get_all_tickers_from_bithumb(self):
        rtn = []
        data = self.send_rest_api("ALL", "KRW")
        for key in data['data'].keys():
            rtn.append(key)
        rtn.pop()   # because of last one is 'date'
        return rtn

    def get_all_tickers(self):
        return self.tickers


"""
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