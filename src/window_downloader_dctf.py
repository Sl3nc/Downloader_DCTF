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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 348)
        MainWindow.setMaximumSize(QSize(500, 348))
        MainWindow.setStyleSheet(u"background-color: rgb(242, 242, 242);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_title)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.label_subtitle = QLabel(self.frame_4)
        self.label_subtitle.setObjectName(u"label_subtitle")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_subtitle.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_subtitle)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)


        self.verticalLayout_3.addWidget(self.frame_4)

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
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(10)
        self.label_instruction.setFont(font2)
        self.label_instruction.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_instruction)


        self.verticalLayout_3.addWidget(self.frame)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_execute = QPushButton(self.frame_2)
        self.pushButton_execute.setObjectName(u"pushButton_execute")
        self.pushButton_execute.setMinimumSize(QSize(0, 50))
        self.pushButton_execute.setFont(font)
        self.pushButton_execute.setStyleSheet(u"background-color: rgb(223, 223, 223);")

        self.horizontalLayout_2.addWidget(self.pushButton_execute)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_back = QPushButton(self.frame_3)
        self.pushButton_back.setObjectName(u"pushButton_back")
        font3 = QFont()
        font3.setPointSize(11)
        self.pushButton_back.setFont(font3)
        self.pushButton_back.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.pushButton_back.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton_back)

        self.pushButton_jump = QPushButton(self.frame_3)
        self.pushButton_jump.setObjectName(u"pushButton_jump")
        self.pushButton_jump.setFont(font1)
        self.pushButton_jump.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pushButton_jump.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.pushButton_jump.setIcon(icon1)

        self.verticalLayout.addWidget(self.pushButton_jump)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font3)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.dateEdit_2 = QDateEdit(self.frame_5)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setFont(font1)
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dateEdit_2)

        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(3, 0))
        self.line_4.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.dateEdit_end = QDateEdit(self.frame_5)
        self.dateEdit_end.setObjectName(u"dateEdit_end")
        self.dateEdit_end.setFont(font1)
        self.dateEdit_end.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dateEdit_end)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.pushButton_cancel_date = QPushButton(self.frame_6)
        self.pushButton_cancel_date.setObjectName(u"pushButton_cancel_date")
        self.pushButton_cancel_date.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.pushButton_cancel_date.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.pushButton_cancel_date)

        self.pushButton_send_date = QPushButton(self.frame_6)
        self.pushButton_send_date.setObjectName(u"pushButton_send_date")
        self.pushButton_send_date.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.pushButton_send_date.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.pushButton_send_date)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader DCTF WEB", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Para baixar <span style=\" font-weight:700; font-style:italic;\">automaticamente</span> seus recibos da DCTF WEB</p></body></html>", None))
        self.label_subtitle.setText(QCoreApplication.translate("MainWindow", u"Siga as seguintes instrun\u00e7\u00f5es:", None))
        self.label_instruction.setText(QCoreApplication.translate("MainWindow", u"Intrun\u00e7\u00e3o", None))
        self.pushButton_execute.setText(QCoreApplication.translate("MainWindow", u"Prosseguir", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u" Voltar", None))
        self.pushButton_jump.setText(QCoreApplication.translate("MainWindow", u"Pular ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo de apura\u00e7\u00e3o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Inicio:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"T\u00e9rmino:", None))
        self.pushButton_cancel_date.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_send_date.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

