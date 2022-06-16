import sys
from pprint import pprint

from PySide6.QtGui import QIcon, QScreen
from PySide6.QtWidgets import QMainWindow, QApplication, QInputDialog

from _main import Ui_MainWindow
from download_wether_dict import get_my_ip, get_weather_dict, city_to_ip
from message_boxes import info_box


class WeatherMain(QMainWindow):
    def __init__(self):
        super(WeatherMain, self).__init__()
        self.city_list = ('Москва', 'Санкт-Петербург', 'Сочи', 'Тула')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.weather_dict = {}

        self.download_data()
        pprint(self.weather_dict)

        # self.dialog_city = MyDialogCity()
        self.ui.action_search.triggered.connect(self.dialog_city_show)
        self.ui.action_favorites.triggered.connect(self.dialog_favorites_show)

    def download_data(self):
        try:
            self.weather_dict = get_weather_dict(city_to_ip(get_my_ip()[1])['city'])
        except TypeError:
            print('download_data: type_error')
            info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                             'Проверьте соединение с интернетом.')

    def dialog_city_show(self):
        text, ok = QInputDialog.getText(self, 'Поиск места',
                                        'ВВедите ваше местоположение: ')

        if ok:
            try:
                self.weather_dict = get_weather_dict(text)
                pprint(self.weather_dict)
            except TypeError:
                print('download_data: type_error')
                info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                                 'Проверьте соединение с интернетом.')

    def dialog_favorites_show(self):
        text, ok = QInputDialog.getItem(self, 'Выбрать город',
                                        'ВВыбрать город: ', self.city_list)
        if ok:
            try:
                self.weather_dict = get_weather_dict(text)
                pprint(self.weather_dict)
            except TypeError:
                print('download_data: type_error')
                info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                                 'Проверьте соединение с интернетом.')


if __name__ == '__main__':
    app = QApplication()
    window = WeatherMain()
    window.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width() / 1.5,
                  QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
    window.setWindowIcon(QIcon('program_icon.png'))
    window.setWindowTitle('Подробный прогноз погоды на три дня.')
    f = open('my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()

    sys.exit(app.exec())
