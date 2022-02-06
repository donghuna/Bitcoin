# NOT USING SO FAR

import requests
# from bs4 import BeautifulSoup


class Currency:
    def __init__(self, coin_name="BTC"):
        if coin_name == "BTC":
            r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
        self.data = r.json()

    def get_last(self):
        return self.data["volume"]


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
