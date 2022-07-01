from PySide6.QtWidgets import QMainWindow, QApplication
from main_form import Ui_MainWindow
from PySide6.QtGui import QIcon, QScreen


class WeatherMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.favorite_list = ('Москва', 'Санкт-Петербург', 'Сочи', 'Тула')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.combo_favorites.addItems(self.favorite_list)
        self.ui.push_search.clicked.connect(self.prt)

    def prt(self):
        print('Huraa!')


if __name__ == '__main__':
    import sys
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
