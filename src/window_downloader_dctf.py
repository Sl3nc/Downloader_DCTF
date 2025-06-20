# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_downloader-dctf.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(545, 311)
        MainWindow.setStyleSheet(u"background-color: rgb(242, 242, 242);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_execute = QPushButton(self.frame_2)
        self.pushButton_execute.setObjectName(u"pushButton_execute")
        self.pushButton_execute.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_execute.setFont(font)
        self.pushButton_execute.setStyleSheet(u"background-color: rgb(223, 223, 223);")

        self.horizontalLayout_2.addWidget(self.pushButton_execute)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_back = QPushButton(self.frame_3)
        self.pushButton_back.setObjectName(u"pushButton_back")
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_back.setFont(font1)
        self.pushButton_back.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.pushButton_back.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton_back)

        self.pushButton_jump = QPushButton(self.frame_3)
        self.pushButton_jump.setObjectName(u"pushButton_jump")
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_jump.setFont(font2)
        self.pushButton_jump.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pushButton_jump.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.pushButton_jump.setIcon(icon1)

        self.verticalLayout.addWidget(self.pushButton_jump)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 3, 1, 2)

        self.label_subtitle = QLabel(self.centralwidget)
        self.label_subtitle.setObjectName(u"label_subtitle")
        self.label_subtitle.setFont(font2)

        self.gridLayout.addWidget(self.label_subtitle, 1, 2, 1, 1)

        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy2)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 5)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_instruction = QLabel(self.frame)
        self.label_instruction.setObjectName(u"label_instruction")
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(10)
        self.label_instruction.setFont(font3)
        self.label_instruction.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_instruction)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 545, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader DCTF WEB", None))
        self.pushButton_execute.setText(QCoreApplication.translate("MainWindow", u"Prosseguir", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u" Voltar", None))
        self.pushButton_jump.setText(QCoreApplication.translate("MainWindow", u"Pular ", None))
        self.label_subtitle.setText(QCoreApplication.translate("MainWindow", u"Siga as seguintes instrun\u00e7\u00f5es:", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Para baixar <span style=\" font-weight:700; font-style:italic;\">automaticamente</span> seus recibos da DCTF WEB</p></body></html>", None))
        self.label_instruction.setText(QCoreApplication.translate("MainWindow", u"Intrun\u00e7\u00e3o", None))
    # retranslateUi

