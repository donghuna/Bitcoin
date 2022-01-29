import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


# Load window UI made by Qt Designer
form_class = uic.loadUiType("mainWindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Window position, size
        self.setGeometry(200, 200, 300, 400)
        # title
        self.setWindowTitle("BitCoin")
        # icon
        self.setWindowIcon(QIcon("bitcoin_icon.png"))
        # self.setWindowIcon(QIcon("bitcoin_black.png"))

        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")


app = QApplication(sys.argv)
window = MyWindow()
window.show()

# label = QLabel("Hello")
# btn = QPushButton("Hello 1")    # 버튼 객체 생성

app.exec_()
