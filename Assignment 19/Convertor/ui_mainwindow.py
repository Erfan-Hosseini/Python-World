# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 517)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.combo_list = QComboBox(self.centralwidget)
        self.combo_list.setObjectName(u"combo_list")

        self.verticalLayout.addWidget(self.combo_list)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.text_get = QLineEdit(self.centralwidget)
        self.text_get.setObjectName(u"text_get")
        font = QFont()
        font.setFamilies([u"Rockwell Extra Bold"])
        font.setPointSize(11)
        font.setBold(True)
        self.text_get.setFont(font)
        self.text_get.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 127);")

        self.gridLayout_2.addWidget(self.text_get, 1, 0, 1, 1)

        self.text_show = QLineEdit(self.centralwidget)
        self.text_show.setObjectName(u"text_show")
        self.text_show.setFont(font)
        self.text_show.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 127);")

        self.gridLayout_2.addWidget(self.text_show, 1, 1, 1, 1)

        self.combo_to = QComboBox(self.centralwidget)
        self.combo_to.setObjectName(u"combo_to")

        self.gridLayout_2.addWidget(self.combo_to, 0, 1, 1, 1)

        self.combo_from = QComboBox(self.centralwidget)
        self.combo_from.setObjectName(u"combo_from")

        self.gridLayout_2.addWidget(self.combo_from, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_convert = QPushButton(self.centralwidget)
        self.btn_convert.setObjectName(u"btn_convert")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_convert.sizePolicy().hasHeightForWidth())
        self.btn_convert.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Rockwell Extra Bold"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.btn_convert.setFont(font1)
        self.btn_convert.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")

        self.verticalLayout_2.addWidget(self.btn_convert)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"convert", None))
    # retranslateUi

