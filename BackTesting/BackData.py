import Bithumb

bithumb = Bithumb.Bithumb()
df = bithumb.get_ochlv("BTC")
print(df.tail())