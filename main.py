import sys
import Logger.Logger as Logger
from PyQt5.QtWidgets import *
import WindowManager


def main():
    logger = Logger.get_logger(__name__)

    app = QApplication(sys.argv)
    window = WindowManager.MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
