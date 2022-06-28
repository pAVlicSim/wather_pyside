# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(651, 511)
        self.action_today = QAction(MainWindow)
        self.action_today.setObjectName(u"action_today")
        self.action_tomorrow = QAction(MainWindow)
        self.action_tomorrow.setObjectName(u"action_tomorrow")
        self.action_after_tomorrow = QAction(MainWindow)
        self.action_after_tomorrow.setObjectName(u"action_after_tomorrow")
        self.action_three_days = QAction(MainWindow)
        self.action_three_days.setObjectName(u"action_three_days")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.city_edit = QLineEdit(self.centralwidget)
        self.city_edit.setObjectName(u"city_edit")

        self.horizontalLayout.addWidget(self.city_edit)

        self.combo_favorites = QComboBox(self.centralwidget)
        self.combo_favorites.setObjectName(u"combo_favorites")
        self.combo_favorites.setEditable(True)
        self.combo_favorites.setMaxCount(20)

        self.horizontalLayout.addWidget(self.combo_favorites)

        self.combo_history = QComboBox(self.centralwidget)
        self.combo_history.setObjectName(u"combo_history")
        self.combo_history.setEditable(True)
        self.combo_history.setMaxCount(50)

        self.horizontalLayout.addWidget(self.combo_history)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 611, 379))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 651, 27))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_today)
        self.menu.addAction(self.action_tomorrow)
        self.menu.addAction(self.action_after_tomorrow)
        self.menu.addAction(self.action_three_days)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_today.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.action_tomorrow.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0442\u0440\u0430", None))
        self.action_after_tomorrow.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0437\u0430\u0432\u0442\u0440\u0430", None))
        self.action_three_days.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0442\u0440\u0438 \u0434\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.combo_favorites.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0430\u043d\u043d\u043e\u0435", None))
        self.combo_history.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0439\u0447\u0430\u0441", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0442\u0440\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0437\u0430\u0432\u0442\u0440\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

