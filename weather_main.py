import sys
from pprint import pprint

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QScreen
from PySide6.QtWidgets import QMainWindow, QApplication, QInputDialog, QLabel

from _main import Ui_MainWindow
from download_wether_dict import get_my_ip, get_weather_dict, ip_to_city
from message_boxes import info_box
from wd_data import get_now_str, get_daily_str


class WeatherMain(QMainWindow):
    def __init__(self):
        super(WeatherMain, self).__init__()
        self.city_list = ('Москва', 'Санкт-Петербург', 'Сочи', 'Тула')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.w_dada = {}

        self.download_data()

        # self.dialog_city = MyDialogCity()
        self.ui.action_search.triggered.connect(self.dialog_city_show)
        self.ui.action_favorites.triggered.connect(self.dialog_favorites_show)
        self.show_weather()
        self.show_daly()

    def download_data(self):
        try:
            w_d = get_weather_dict(ip_to_city(get_my_ip()[1])['city'])
            # pprint(w_d)
            w_now = w_d['current']
            w_loc = {'name': w_d['location']['name'], 'country': w_d['location']['country']}
            w_forec = []
            w_hour = []
            for i in w_d['forecast']['forecastday']:
                w_forec.append(i['date'])
                w_forec.append(i['day'])
                w_hour.append(i['hour'])
                pprint(w_forec)
            self.w_dada['now'] = w_now
            self.w_dada['loc'] = w_loc
            self.w_dada['forec'] = w_forec
            self.w_dada['hour'] = w_hour
        except TypeError:
            print('download_data: type_error')
            info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                             'Проверьте соединение с интернетом.')

    def dialog_city_show(self):
        text, ok = QInputDialog.getText(self, 'Поиск места',
                                        'ВВедите ваше местоположение: ')

        if ok:
            try:
                w_d = get_weather_dict(text)
                pass
            except TypeError:
                print('download_data: type_error')
                info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                                 'Проверьте соединение с интернетом.')

    def dialog_favorites_show(self):
        text, ok = QInputDialog.getItem(self, 'Выбрать город',
                                        'ВВыбрать город: ', self.city_list)
        if ok:
            try:
                w_d = get_weather_dict(text)
                pass
            except TypeError:
                print('download_data: type_error')
                info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                                 'Проверьте соединение с интернетом.')

    def show_weather(self):
        label_now = QLabel()
        label_now.setAlignment(Qt.AlignCenter)
        self.ui.verticalLayout_weather.addWidget(label_now)
        label_now.setText(get_now_str(self.w_dada['now'], self.w_dada['loc']))

    def show_daly(self):
        print(get_daily_str(self.w_dada['forec']))


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
