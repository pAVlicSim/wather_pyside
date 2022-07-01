import sys
from pprint import pprint
from PySide6.QtGui import QIcon, QScreen
from PySide6.QtWidgets import QMainWindow, QApplication
from main_form import Ui_MainWindow
from download_wether_dict import get_my_ip, get_weather_dict, ip_to_city
from message_boxes import info_box
from wd_data import get_weather_str
from collections import deque
from history_favorite_datas import add_city_history


class WeatherMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.favorite_list = ['Москва', 'Санкт-Петербург', 'Сочи', 'Тула']
        self.history_list = deque(maxlen=50)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.combo_favorites.addItems(self.favorite_list)
        self.ui.push_search.clicked.connect(self.weather_from_search)
        self.label_list = []
        self.w_data = {}

        try:
            self.download_data(ip_to_city(get_my_ip()[1])['city'])
            self.show_weather()
        except (TypeError, KeyError):
            info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                             'Проверьте соединение с интернетом.')

    def download_data(self, name_city: str):
        try:
            w_d = get_weather_dict(name_city)
            w_now = w_d['current']
            w_loc = {'name': w_d['location']['name'], 'country': w_d['location']['country']}
            w_forec = []
            w_hour = []
            for i in w_d['forecast']['forecastday']:
                w_forec.append([i['day'], i['astro'], i['date_epoch']])
                w_hour.append(i['hour'])
            # pprint(w_forec)
            self.w_data['now'] = w_now
            self.w_data['loc'] = w_loc
            self.w_data['forec'] = w_forec
            self.w_data['hour'] = w_hour
        except (TypeError, KeyError):
            info_box(self, 'Сбой загрузки.', 'Не удалось загрузить данные.\n'
                                             'Проверьте соединение с интернетом.')

    def show_weather(self):
        weather_srt_list = get_weather_str(self.w_data['now'], self.w_data['loc'], self.w_data['forec'])
        try:
            self.ui.label_now.setText(weather_srt_list[0])
            self.ui.label_today.setText(weather_srt_list[1])
            self.ui.label_tomorrow.setText(weather_srt_list[2])
            self.ui.label_after_tomorrow.setText(weather_srt_list[3])

        except KeyError:
            pass

    def weather_from_search(self):
        self.download_data(self.ui.city_edit.text())
        self.show_weather()
        add_city_history(self.history_list, self.ui.combo_history, self.w_data['loc'])


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
