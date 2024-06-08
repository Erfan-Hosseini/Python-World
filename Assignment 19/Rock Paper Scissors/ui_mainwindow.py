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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(637, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_computer = QPushButton(self.centralwidget)
        self.btn_computer.setObjectName(u"btn_computer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_computer.sizePolicy().hasHeightForWidth())
        self.btn_computer.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.btn_computer, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_player = QPushButton(self.centralwidget)
        self.btn_player.setObjectName(u"btn_player")
        sizePolicy.setHeightForWidth(self.btn_player.sizePolicy().hasHeightForWidth())
        self.btn_player.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.btn_player, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_rock = QPushButton(self.centralwidget)
        self.btn_rock.setObjectName(u"btn_rock")
        sizePolicy.setHeightForWidth(self.btn_rock.sizePolicy().hasHeightForWidth())
        self.btn_rock.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_rock)

        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        sizePolicy.setHeightForWidth(self.btn_paper.sizePolicy().hasHeightForWidth())
        self.btn_paper.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_paper)

        self.btn_scissors = QPushButton(self.centralwidget)
        self.btn_scissors.setObjectName(u"btn_scissors")
        sizePolicy.setHeightForWidth(self.btn_scissors.sizePolicy().hasHeightForWidth())
        self.btn_scissors.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_scissors)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 3)

        self.text_box = QLineEdit(self.centralwidget)
        self.text_box.setObjectName(u"text_box")

        self.gridLayout.addWidget(self.text_box, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_player = QLineEdit(self.centralwidget)
        self.text_player.setObjectName(u"text_player")

        self.verticalLayout.addWidget(self.text_player)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_computer = QLineEdit(self.centralwidget)
        self.text_computer.setObjectName(u"text_computer")

        self.verticalLayout_2.addWidget(self.text_computer)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_restart = QPushButton(self.centralwidget)
        self.btn_restart.setObjectName(u"btn_restart")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        self.btn_restart.setFont(font)

        self.verticalLayout_3.addWidget(self.btn_restart)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 637, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_computer.setText("")
        self.btn_player.setText("")
        self.btn_rock.setText("")
        self.btn_paper.setText("")
        self.btn_scissors.setText("")
        self.btn_restart.setText(QCoreApplication.translate("MainWindow", u"Reset the scores", None))
    # retranslateUi

