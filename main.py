import sys
from PyQt5.QtWidgets import *
import WindowManager

import Bithumb

a = Bithumb.Ticker()
tickers = a.get_all_tickers()
print(len(tickers))
print(tickers)


app = QApplication(sys.argv)
window = WindowManager.MyWindow()
window.show()
app.exec_()
