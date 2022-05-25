import sys
from pprint import pprint

from PySide6.QtGui import QIcon, QPixmap, QScreen
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from _main import Ui_MainWindow


class WeatherMain(QMainWindow):
    def __init__(self):
        super(WeatherMain, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = WeatherMain()
    window.resize(900, 600)
    f = open('my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()

    sys.exit(app.exec())
