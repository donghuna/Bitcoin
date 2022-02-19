import Bithumb
import pandas as pd


bithumb = Bithumb.Bithumb()
df = bithumb.get_ochlv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5


writer = pd.ExcelWriter('Backdata.xlsx', engine='xlsxwriter')

print(df.tail())
print(type(df.tail()))

df.to_excel(writer, sheet_name='Sheet1')
writer.close()
