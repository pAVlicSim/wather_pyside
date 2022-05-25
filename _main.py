# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 586)
        self.action_search = QAction(MainWindow)
        self.action_search.setObjectName(u"action_search")
        self.action_charts = QAction(MainWindow)
        self.action_charts.setObjectName(u"action_charts")
        self.action_favorites = QAction(MainWindow)
        self.action_favorites.setObjectName(u"action_favorites")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_day1 = QLabel(self.centralwidget)
        self.label_day1.setObjectName(u"label_day1")
        self.label_day1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_day1)

        self.label_day2 = QLabel(self.centralwidget)
        self.label_day2.setObjectName(u"label_day2")
        self.label_day2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_day2)

        self.label_day3 = QLabel(self.centralwidget)
        self.label_day3.setObjectName(u"label_day3")
        self.label_day3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_day3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_search)
        self.menu.addAction(self.action_charts)
        self.menu.addAction(self.action_favorites)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0413\u043e\u0440\u043e\u0434", None))
        self.action_charts.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.action_favorites.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.label_day1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_day2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_day3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

