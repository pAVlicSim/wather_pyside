import sys
import time
from pprint import pprint

from PySide6.QtGui import QIcon, QPixmap, QScreen
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from _main import Ui_MainWindow
from download_wether_dict import get_my_ip, get_weather_dict, city_to_ip
from message_boxes import info_box


class WeatherMain(QMainWindow):
    def __init__(self):
        super(WeatherMain, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.weather_dict = {}

        self.download_data()
        pprint(self.weather_dict)

    def download_data(self):
        try:
            self.weather_dict = get_weather_dict(city_to_ip(get_my_ip()[1])['city'])
        except TypeError:
            print('download_data: type_error')
            info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                             'Проверьте соединение с интернетом.')


if __name__ == '__main__':
    app = QApplication()
    window = WeatherMain()
    window.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width() / 1.5,
                  QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
    f = open('my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()

    sys.exit(app.exec())
