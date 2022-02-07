import sys
from PyQt5.QtWidgets import *
import WindowManager
import logging

if __name__ == '__main__':
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)


    app = QApplication(sys.argv)
    window = WindowManager.MyWindow()
    window.show()
    app.exec_()
