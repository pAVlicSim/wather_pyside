# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'charts_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_charts(object):
    def setupUi(self, Dialog_charts):
        if not Dialog_charts.objectName():
            Dialog_charts.setObjectName(u"Dialog_charts")
        Dialog_charts.resize(765, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog_charts)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.radioButton = QRadioButton(Dialog_charts)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(Dialog_charts)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(Dialog_charts)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(Dialog_charts)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(Dialog_charts)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(Dialog_charts)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout.addWidget(self.radioButton_6)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_charts)

        QMetaObject.connectSlotsByName(Dialog_charts)
    # setupUi

    def retranslateUi(self, Dialog_charts):
        Dialog_charts.setWindowTitle(QCoreApplication.translate("Dialog_charts", u"Dialog", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog_charts", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog_charts", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog_charts", u"\u0432\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog_charts", u"\u0412\u0435\u0440\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043e\u0441\u0430\u0434\u043a\u043e\u0432", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog_charts", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0435\u0442\u0440\u0430", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog_charts", u"\u0423/\u0424", None))
    # retranslateUi

