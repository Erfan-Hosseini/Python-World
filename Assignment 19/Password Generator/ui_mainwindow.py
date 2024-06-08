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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 178)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_3 = QRadioButton(self.centralwidget)
        self.radio_3.setObjectName(u"radio_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_3.sizePolicy().hasHeightForWidth())
        self.radio_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(14)
        self.radio_3.setFont(font)

        self.gridLayout.addWidget(self.radio_3, 2, 1, 1, 1)

        self.radio_2 = QRadioButton(self.centralwidget)
        self.radio_2.setObjectName(u"radio_2")
        sizePolicy.setHeightForWidth(self.radio_2.sizePolicy().hasHeightForWidth())
        self.radio_2.setSizePolicy(sizePolicy)
        self.radio_2.setFont(font)

        self.gridLayout.addWidget(self.radio_2, 1, 1, 1, 1)

        self.radio_1 = QRadioButton(self.centralwidget)
        self.radio_1.setObjectName(u"radio_1")
        sizePolicy.setHeightForWidth(self.radio_1.sizePolicy().hasHeightForWidth())
        self.radio_1.setSizePolicy(sizePolicy)
        self.radio_1.setFont(font)

        self.gridLayout.addWidget(self.radio_1, 0, 1, 1, 1)

        self.text_box = QLineEdit(self.centralwidget)
        self.text_box.setObjectName(u"text_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_box.sizePolicy().hasHeightForWidth())
        self.text_box.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.text_box, 0, 0, 1, 1)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        sizePolicy1.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(20)
        self.btn_generate.setFont(font1)

        self.gridLayout.addWidget(self.btn_generate, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 613, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radio_3.setText(QCoreApplication.translate("MainWindow", u"Super strong password", None))
        self.radio_2.setText(QCoreApplication.translate("MainWindow", u"Strong password", None))
        self.radio_1.setText(QCoreApplication.translate("MainWindow", u"Normal password", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate new password", None))
    # retranslateUi

