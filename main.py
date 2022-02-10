import Logger.Logger as Logger
import sys
from PyQt5.QtWidgets import *
import WindowManager


def main():
    # logging.basicConfig(level=logging.INFO, format='%(relativeCreated)6d %(threadName)s %(message)s')

    # logging.basicConfig(level=logging.INFO)
    # log = logging.getLogger()

    logger = Logger.get_logger(__name__)
    logger.info(f'1번째 방문입니다.')

    app = QApplication(sys.argv)
    window = WindowManager.MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
