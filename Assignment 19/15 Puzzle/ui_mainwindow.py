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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(719, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_10 = QPushButton(self.centralwidget)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_10, 4, 1, 1, 1)

        self.btn_13 = QPushButton(self.centralwidget)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_13, 5, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_6, 3, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_9, 4, 0, 1, 1)

        self.btn_12 = QPushButton(self.centralwidget)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_12, 4, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_5, 3, 0, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_7, 3, 2, 1, 1)

        self.btn_unpause = QPushButton(self.centralwidget)
        self.btn_unpause.setObjectName(u"btn_unpause")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(12)
        self.btn_unpause.setFont(font)

        self.gridLayout.addWidget(self.btn_unpause, 0, 2, 1, 1)

        self.btn_11 = QPushButton(self.centralwidget)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_11, 4, 2, 1, 1)

        self.btn_14 = QPushButton(self.centralwidget)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_14, 5, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_4, 2, 3, 1, 1)

        self.btn_16 = QPushButton(self.centralwidget)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_16, 5, 3, 1, 1)

        self.btn_restart = QPushButton(self.centralwidget)
        self.btn_restart.setObjectName(u"btn_restart")
        self.btn_restart.setFont(font)

        self.gridLayout.addWidget(self.btn_restart, 0, 0, 1, 1)

        self.btn_pause = QPushButton(self.centralwidget)
        self.btn_pause.setObjectName(u"btn_pause")
        self.btn_pause.setFont(font)

        self.gridLayout.addWidget(self.btn_pause, 0, 1, 1, 1)

        self.btn_15 = QPushButton(self.centralwidget)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_15, 5, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_8, 3, 3, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.text_box = QLineEdit(self.centralwidget)
        self.text_box.setObjectName(u"text_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_box.sizePolicy().hasHeightForWidth())
        self.text_box.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.text_box, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_10.setText("")
        self.btn_13.setText("")
        self.btn_6.setText("")
        self.btn_9.setText("")
        self.btn_12.setText("")
        self.btn_5.setText("")
        self.btn_7.setText("")
        self.btn_unpause.setText(QCoreApplication.translate("MainWindow", u"unpause", None))
        self.btn_11.setText("")
        self.btn_14.setText("")
        self.btn_4.setText("")
        self.btn_16.setText("")
        self.btn_restart.setText(QCoreApplication.translate("MainWindow", u"restart", None))
        self.btn_pause.setText(QCoreApplication.translate("MainWindow", u"pause", None))
        self.btn_15.setText("")
        self.btn_3.setText("")
        self.btn_8.setText("")
        self.btn_2.setText("")
        self.btn_1.setText("")
    # retranslateUi

