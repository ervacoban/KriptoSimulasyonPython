# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GirisKayitEkran.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import simgeler_rc

class Ui_GirisKayitEkran(object):
    def setupUi(self, GirisKayitEkran):
        if not GirisKayitEkran.objectName():
            GirisKayitEkran.setObjectName(u"GirisKayitEkran")
        GirisKayitEkran.resize(400, 570)
        GirisKayitEkran.setMinimumSize(QSize(300, 570))
        GirisKayitEkran.setMaximumSize(QSize(400, 570))
        GirisKayitEkran.setWindowIcon(QIcon(u":/simge/simge/logo.png"))
        font = QFont()
        font.setFamily(u"Segoe UI Historic")
        GirisKayitEkran.setFont(font)
        self.centralwidget = QWidget(GirisKayitEkran)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.AnaFrame = QFrame(self.centralwidget)
        self.AnaFrame.setObjectName(u"AnaFrame")
        self.AnaFrame.setEnabled(True)
        self.AnaFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(60, 99, 161);\n"
"}")
        self.AnaFrame.setFrameShape(QFrame.StyledPanel)
        self.AnaFrame.setFrameShadow(QFrame.Raised)
        self.UstIcerikFrame = QFrame(self.AnaFrame)
        self.UstIcerikFrame.setObjectName(u"UstIcerikFrame")
        self.UstIcerikFrame.setGeometry(QRect(0, 0, 381, 31))
        self.UstIcerikFrame.setStyleSheet(u"QFrame{\n"
"	color: white;\n"
"	background-color: rgb(74, 125, 200);\n"
"}")
        self.UstIcerikFrame.setFrameShape(QFrame.StyledPanel)
        self.UstIcerikFrame.setFrameShadow(QFrame.Raised)
        self.ProgAdiFrame = QFrame(self.UstIcerikFrame)
        self.ProgAdiFrame.setObjectName(u"ProgAdiFrame")
        self.ProgAdiFrame.setGeometry(QRect(-1, -1, 301, 31))
        self.ProgAdiFrame.setFrameShape(QFrame.StyledPanel)
        self.ProgAdiFrame.setFrameShadow(QFrame.Raised)
        self.ProgAdiText = QLabel(self.ProgAdiFrame)
        self.ProgAdiText.setObjectName(u"ProgAdiText")
        self.ProgAdiText.setGeometry(QRect(0, 0, 200, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Historic")
        font1.setPointSize(12)
        self.ProgAdiText.setFont(font1)
        self.ProgAdiText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"	margin-left: 5px;\n"
"	color: white;\n"
"}")
        self.ProgButonlar = QFrame(self.UstIcerikFrame)
        self.ProgButonlar.setObjectName(u"ProgButonlar")
        self.ProgButonlar.setGeometry(QRect(300, 0, 81, 31))
        self.ProgButonlar.setStyleSheet(u"")
        self.ProgButonlar.setFrameShape(QFrame.StyledPanel)
        self.ProgButonlar.setFrameShadow(QFrame.Raised)
        self.asagiButton = QPushButton(self.ProgButonlar)
        self.asagiButton.setObjectName(u"asagiButton")
        self.asagiButton.setGeometry(QRect(0, 0, 41, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asagiButton.sizePolicy().hasHeightForWidth())
        self.asagiButton.setSizePolicy(sizePolicy)
        self.asagiButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.asagiButton.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/simge/simge/s-asagi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.asagiButton.setIcon(icon)
        self.kapatButon = QPushButton(self.ProgButonlar)
        self.kapatButon.setObjectName(u"kapatButon")
        self.kapatButon.setGeometry(QRect(40, 0, 41, 31))
        sizePolicy.setHeightForWidth(self.kapatButon.sizePolicy().hasHeightForWidth())
        self.kapatButon.setSizePolicy(sizePolicy)
        self.kapatButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.kapatButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/simge/simge/s-kapat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kapatButon.setIcon(icon1)
        self.AltIcerikFrame = QFrame(self.AnaFrame)
        self.AltIcerikFrame.setObjectName(u"AltIcerikFrame")
        self.AltIcerikFrame.setGeometry(QRect(0, 30, 381, 521))
        self.AltIcerikFrame.setFrameShape(QFrame.StyledPanel)
        self.AltIcerikFrame.setFrameShadow(QFrame.Raised)
        self.SayfaWidget = QStackedWidget(self.AltIcerikFrame)
        self.SayfaWidget.setObjectName(u"SayfaWidget")
        self.SayfaWidget.setGeometry(QRect(0, 0, 381, 521))
        self.GirisEkrani = QWidget()
        self.GirisEkrani.setObjectName(u"GirisEkrani")
        self.groupBox_2 = QGroupBox(self.GirisEkrani)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(80, 30, 221, 221))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"}\n"
"")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 201))
        self.label.setPixmap(QPixmap(u":/simge/simge/logo.png"))
        self.label.setScaledContents(True)
        self.groupBox = QGroupBox(self.GirisEkrani)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 280, 341, 221))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"}\n"
"")
        self.KayitEkranButon = QPushButton(self.groupBox)
        self.KayitEkranButon.setObjectName(u"KayitEkranButon")
        self.KayitEkranButon.setGeometry(QRect(130, 190, 81, 21))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        self.KayitEkranButon.setFont(font2)
        self.KayitEkranButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.KayitEkranButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.SifreText = QLineEdit(self.groupBox)
        self.SifreText.setObjectName(u"SifreText")
        self.SifreText.setGeometry(QRect(20, 80, 301, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.SifreText.setFont(font3)
        self.SifreText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.SifreText.setEchoMode(QLineEdit.Password)
        self.MailText = QLineEdit(self.groupBox)
        self.MailText.setObjectName(u"MailText")
        self.MailText.setGeometry(QRect(20, 20, 301, 41))
        self.MailText.setFont(font3)
        self.MailText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.MailText.setEchoMode(QLineEdit.Normal)
        self.GirisButon = QPushButton(self.groupBox)
        self.GirisButon.setObjectName(u"GirisButon")
        self.GirisButon.setGeometry(QRect(20, 140, 301, 41))
        self.GirisButon.setFont(font3)
        self.GirisButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.GirisButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.GirisButon.setIconSize(QSize(20, 20))
        self.GirisErrorLabel = QLabel(self.groupBox)
        self.GirisErrorLabel.setObjectName(u"GirisErrorLabel")
        self.GirisErrorLabel.setGeometry(QRect(20, 190, 121, 21))
        self.GirisErrorLabel.setFont(font2)
        self.GirisErrorLabel.setStyleSheet(u"")
        self.SifreText.raise_()
        self.MailText.raise_()
        self.GirisButon.raise_()
        self.GirisErrorLabel.raise_()
        self.KayitEkranButon.raise_()
        self.SayfaWidget.addWidget(self.GirisEkrani)
        self.KayitEkrani = QWidget()
        self.KayitEkrani.setObjectName(u"KayitEkrani")
        self.KayitEkrani.setEnabled(True)
        self.groupBox_3 = QGroupBox(self.KayitEkrani)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 341, 481))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"}\n"
"")
        self.GirisEkranButon = QPushButton(self.groupBox_3)
        self.GirisEkranButon.setObjectName(u"GirisEkranButon")
        self.GirisEkranButon.setGeometry(QRect(130, 450, 81, 21))
        font4 = QFont()
        font4.setPointSize(10)
        self.GirisEkranButon.setFont(font4)
        self.GirisEkranButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.GirisEkranButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.MailSifreKayitTekrar = QLineEdit(self.groupBox_3)
        self.MailSifreKayitTekrar.setObjectName(u"MailSifreKayitTekrar")
        self.MailSifreKayitTekrar.setGeometry(QRect(20, 340, 301, 41))
        self.MailSifreKayitTekrar.setFont(font3)
        self.MailSifreKayitTekrar.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.MailSifreKayitTekrar.setEchoMode(QLineEdit.Password)
        self.MailTextKayit = QLineEdit(self.groupBox_3)
        self.MailTextKayit.setObjectName(u"MailTextKayit")
        self.MailTextKayit.setGeometry(QRect(20, 220, 301, 41))
        self.MailTextKayit.setFont(font3)
        self.MailTextKayit.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.MailTextKayit.setEchoMode(QLineEdit.Normal)
        self.KayitOlButon = QPushButton(self.groupBox_3)
        self.KayitOlButon.setObjectName(u"KayitOlButon")
        self.KayitOlButon.setGeometry(QRect(20, 400, 301, 41))
        self.KayitOlButon.setFont(font3)
        self.KayitOlButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.KayitOlButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KayitOlButon.setIconSize(QSize(20, 20))
        self.MailSifreKayit = QLineEdit(self.groupBox_3)
        self.MailSifreKayit.setObjectName(u"MailSifreKayit")
        self.MailSifreKayit.setGeometry(QRect(20, 280, 301, 41))
        self.MailSifreKayit.setFont(font3)
        self.MailSifreKayit.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.MailSifreKayit.setEchoMode(QLineEdit.Password)
        self.SoyisimText = QLineEdit(self.groupBox_3)
        self.SoyisimText.setObjectName(u"SoyisimText")
        self.SoyisimText.setGeometry(QRect(20, 160, 301, 41))
        self.SoyisimText.setFont(font3)
        self.SoyisimText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.SoyisimText.setEchoMode(QLineEdit.Normal)
        self.IsimText = QLineEdit(self.groupBox_3)
        self.IsimText.setObjectName(u"IsimText")
        self.IsimText.setGeometry(QRect(20, 100, 301, 41))
        self.IsimText.setFont(font3)
        self.IsimText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QLineEdit::hover{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(45, 75, 121) ;\n"
"	background-color: rgb(52, 87, 140);\n"
"}")
        self.IsimText.setEchoMode(QLineEdit.Normal)
        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(130, 10, 81, 81))
        self.groupBox_7.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"}\n"
"")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 81, 81))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}\n"
"")
        self.label_4.setPixmap(QPixmap(u":/simge/simge/logo.png"))
        self.label_4.setScaledContents(True)
        self.KayitErrorLabel = QLabel(self.groupBox_3)
        self.KayitErrorLabel.setObjectName(u"KayitErrorLabel")
        self.KayitErrorLabel.setGeometry(QRect(20, 450, 121, 21))
        self.KayitErrorLabel.setFont(font2)
        self.KayitErrorLabel.setStyleSheet(u"")
        self.MailSifreKayitTekrar.raise_()
        self.MailTextKayit.raise_()
        self.KayitOlButon.raise_()
        self.MailSifreKayit.raise_()
        self.SoyisimText.raise_()
        self.IsimText.raise_()
        self.groupBox_7.raise_()
        self.KayitErrorLabel.raise_()
        self.GirisEkranButon.raise_()
        self.SayfaWidget.addWidget(self.KayitEkrani)
        self.LoadEkrani = QWidget()
        self.LoadEkrani.setObjectName(u"LoadEkrani")
        self.LoadEkrani.setEnabled(False)
        self.groupBox_5 = QGroupBox(self.LoadEkrani)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 20, 341, 481))
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"}\n"
"")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(110, 20, 121, 121))
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(74, 125, 200);\n"
"}\n"
"")
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 101, 101))
        self.label_3.setPixmap(QPixmap(u":/simge/simge/logo.png"))
        self.label_3.setScaledContents(True)
        self.progressBarFrame = QFrame(self.groupBox_5)
        self.progressBarFrame.setObjectName(u"progressBarFrame")
        self.progressBarFrame.setGeometry(QRect(30, 170, 280, 280))
        self.progressBarFrame.setStyleSheet(u"")
        self.progressBarFrame.setFrameShape(QFrame.NoFrame)
        self.progressBarFrame.setFrameShadow(QFrame.Raised)
        self.progressBG = QFrame(self.progressBarFrame)
        self.progressBG.setObjectName(u"progressBG")
        self.progressBG.setGeometry(QRect(0, 0, 280, 280))
        self.progressBG.setStyleSheet(u"QFrame{\n"
"	border-radius: 140px;\n"
"	background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.progressBG.setFrameShape(QFrame.NoFrame)
        self.progressBG.setFrameShadow(QFrame.Raised)
        self.progressBarFrameIc = QFrame(self.progressBarFrame)
        self.progressBarFrameIc.setObjectName(u"progressBarFrameIc")
        self.progressBarFrameIc.setGeometry(QRect(0, 0, 280, 280))
        self.progressBarFrameIc.setStyleSheet(u"QFrame{\n"
"	border-radius: 140px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(167, 10, 10, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.progressBarFrameIc.setFrameShape(QFrame.NoFrame)
        self.progressBarFrameIc.setFrameShadow(QFrame.Raised)
        self.progressContainer = QFrame(self.progressBarFrame)
        self.progressContainer.setObjectName(u"progressContainer")
        self.progressContainer.setGeometry(QRect(30, 30, 220, 220))
        self.progressContainer.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;\n"
"	background-color: rgb(57, 94, 153);\n"
"}")
        self.progressContainer.setFrameShape(QFrame.StyledPanel)
        self.progressContainer.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.progressContainer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 181, 101))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.YukleniyorText = QLabel(self.layoutWidget)
        self.YukleniyorText.setObjectName(u"YukleniyorText")
        self.YukleniyorText.setFont(font4)
        self.YukleniyorText.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.YukleniyorText.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.YukleniyorText, 0, 0, 1, 1)

        self.YukleniyorYuzdeText = QLabel(self.layoutWidget)
        self.YukleniyorYuzdeText.setObjectName(u"YukleniyorYuzdeText")
        font5 = QFont()
        font5.setPointSize(40)
        self.YukleniyorYuzdeText.setFont(font5)
        self.YukleniyorYuzdeText.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.YukleniyorYuzdeText.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.YukleniyorYuzdeText, 1, 0, 1, 1)

        self.SayfaWidget.addWidget(self.LoadEkrani)

        self.verticalLayout.addWidget(self.AnaFrame)

        GirisKayitEkran.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.MailText, self.SifreText)
        QWidget.setTabOrder(self.SifreText, self.GirisButon)
        QWidget.setTabOrder(self.GirisButon, self.KayitEkranButon)
        QWidget.setTabOrder(self.KayitEkranButon, self.asagiButton)
        QWidget.setTabOrder(self.asagiButton, self.kapatButon)
        QWidget.setTabOrder(self.kapatButon, self.IsimText)
        QWidget.setTabOrder(self.IsimText, self.SoyisimText)
        QWidget.setTabOrder(self.SoyisimText, self.MailTextKayit)
        QWidget.setTabOrder(self.MailTextKayit, self.MailSifreKayit)
        QWidget.setTabOrder(self.MailSifreKayit, self.MailSifreKayitTekrar)
        QWidget.setTabOrder(self.MailSifreKayitTekrar, self.KayitOlButon)
        QWidget.setTabOrder(self.KayitOlButon, self.GirisEkranButon)

        self.retranslateUi(GirisKayitEkran)

        self.SayfaWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GirisKayitEkran)
    # setupUi

    def retranslateUi(self, GirisKayitEkran):
        GirisKayitEkran.setWindowTitle(QCoreApplication.translate("GirisKayitEkran", u"MainWindow", None))
        self.ProgAdiText.setText(QCoreApplication.translate("GirisKayitEkran", u"Kriptogram", None))
#if QT_CONFIG(tooltip)
        self.asagiButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.asagiButton.setText("")
#if QT_CONFIG(tooltip)
        self.kapatButon.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.kapatButon.setText("")
        self.groupBox_2.setTitle("")
        self.label.setText("")
        self.groupBox.setTitle("")
        self.KayitEkranButon.setText(QCoreApplication.translate("GirisKayitEkran", u"Kay\u0131t Ol", None))
        self.SifreText.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"\u015eifre", None))
        self.MailText.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"E-Posta", None))
        self.GirisButon.setText(QCoreApplication.translate("GirisKayitEkran", u"Giri\u015f Yap", None))
        self.GirisErrorLabel.setText("")
        self.groupBox_3.setTitle("")
        self.GirisEkranButon.setText(QCoreApplication.translate("GirisKayitEkran", u"Giri\u015f Yap", None))
        self.MailSifreKayitTekrar.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"\u015eifre Tekrar\u0131", None))
        self.MailTextKayit.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"E-Posta", None))
        self.KayitOlButon.setText(QCoreApplication.translate("GirisKayitEkran", u"Kay\u0131t Ol", None))
        self.MailSifreKayit.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"\u015eifre", None))
        self.SoyisimText.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"Soyisim", None))
        self.IsimText.setPlaceholderText(QCoreApplication.translate("GirisKayitEkran", u"\u0130sim", None))
        self.groupBox_7.setTitle("")
        self.label_4.setText("")
        self.KayitErrorLabel.setText("")
        self.groupBox_5.setTitle("")
        self.groupBox_6.setTitle("")
        self.label_3.setText("")
        self.YukleniyorText.setText(QCoreApplication.translate("GirisKayitEkran", u"Y\u00fckleniyor...", None))
        self.YukleniyorYuzdeText.setText(QCoreApplication.translate("GirisKayitEkran", u"0%", None))
    # retranslateUi

