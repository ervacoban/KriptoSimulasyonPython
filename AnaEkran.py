# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnaEkran.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import simgeler_rc

class Ui_AnaEkran(object):
    def setupUi(self, AnaEkran):
        if not AnaEkran.objectName():
            AnaEkran.setObjectName(u"AnaEkran")
        AnaEkran.resize(950, 650)
        AnaEkran.setMinimumSize(QSize(950, 650))
        AnaEkran.setMaximumSize(QSize(950, 650))
        AnaEkran.setWindowIcon(QIcon(u":/simge/simge/logo.png"))
        font = QFont()
        font.setFamily(u"Segoe UI Historic")
        AnaEkran.setFont(font)
        self.centralwidget = QWidget(AnaEkran)
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
        self.AnaFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.AnaFrame.setFrameShape(QFrame.StyledPanel)
        self.AnaFrame.setFrameShadow(QFrame.Raised)
        self.AltFrame = QFrame(self.AnaFrame)
        self.AltFrame.setObjectName(u"AltFrame")
        self.AltFrame.setGeometry(QRect(0, 59, 931, 571))
        self.AltFrame.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(60, 99, 161);\n"
"}")
        self.AltFrame.setFrameShape(QFrame.StyledPanel)
        self.AltFrame.setFrameShadow(QFrame.Raised)
        self.SolMenuFrame = QFrame(self.AltFrame)
        self.SolMenuFrame.setObjectName(u"SolMenuFrame")
        self.SolMenuFrame.setGeometry(QRect(0, 0, 71, 571))
        self.SolMenuFrame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(45, 75, 121);\n"
"}")
        self.SolMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.SolMenuFrame.setFrameShadow(QFrame.Raised)
        self.solMenuUstButonlar = QFrame(self.SolMenuFrame)
        self.solMenuUstButonlar.setObjectName(u"solMenuUstButonlar")
        self.solMenuUstButonlar.setGeometry(QRect(0, -1, 71, 281))
        self.solMenuUstButonlar.setStyleSheet(u"")
        self.solMenuUstButonlar.setFrameShape(QFrame.StyledPanel)
        self.solMenuUstButonlar.setFrameShadow(QFrame.Raised)
        self.cuzdanButon = QPushButton(self.solMenuUstButonlar)
        self.cuzdanButon.setObjectName(u"cuzdanButon")
        self.cuzdanButon.setGeometry(QRect(0, 0, 71, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cuzdanButon.sizePolicy().hasHeightForWidth())
        self.cuzdanButon.setSizePolicy(sizePolicy)
        self.cuzdanButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.cuzdanButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/simge/simge/s-cuzdan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cuzdanButon.setIcon(icon)
        self.cuzdanButon.setIconSize(QSize(24, 24))
        self.piyasaButon = QPushButton(self.solMenuUstButonlar)
        self.piyasaButon.setObjectName(u"piyasaButon")
        self.piyasaButon.setGeometry(QRect(0, 71, 71, 71))
        sizePolicy.setHeightForWidth(self.piyasaButon.sizePolicy().hasHeightForWidth())
        self.piyasaButon.setSizePolicy(sizePolicy)
        self.piyasaButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.piyasaButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/simge/simge/s-piyasa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.piyasaButon.setIcon(icon1)
        self.piyasaButon.setIconSize(QSize(24, 24))
        self.solMenuAltButonlar = QFrame(self.SolMenuFrame)
        self.solMenuAltButonlar.setObjectName(u"solMenuAltButonlar")
        self.solMenuAltButonlar.setGeometry(QRect(0, 290, 71, 281))
        self.solMenuAltButonlar.setStyleSheet(u"")
        self.solMenuAltButonlar.setFrameShape(QFrame.StyledPanel)
        self.solMenuAltButonlar.setFrameShadow(QFrame.Raised)
        self.cikisButon = QPushButton(self.solMenuAltButonlar)
        self.cikisButon.setObjectName(u"cikisButon")
        self.cikisButon.setGeometry(QRect(0, 210, 71, 71))
        sizePolicy.setHeightForWidth(self.cikisButon.sizePolicy().hasHeightForWidth())
        self.cikisButon.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(8)
        self.cikisButon.setFont(font1)
        self.cikisButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.cikisButon.setToolTipDuration(-1)
        self.cikisButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/simge/simge/s-cikis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cikisButon.setIcon(icon2)
        self.cikisButon.setIconSize(QSize(24, 24))
        self.ayarlarButon = QPushButton(self.solMenuAltButonlar)
        self.ayarlarButon.setObjectName(u"ayarlarButon")
        self.ayarlarButon.setGeometry(QRect(0, 139, 71, 71))
        sizePolicy.setHeightForWidth(self.ayarlarButon.sizePolicy().hasHeightForWidth())
        self.ayarlarButon.setSizePolicy(sizePolicy)
        self.ayarlarButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.ayarlarButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 99, 161);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/simge/simge/s-ayarlar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ayarlarButon.setIcon(icon3)
        self.ayarlarButon.setIconSize(QSize(24, 24))
        self.SagIcerikFrame = QFrame(self.AltFrame)
        self.SagIcerikFrame.setObjectName(u"SagIcerikFrame")
        self.SagIcerikFrame.setGeometry(QRect(70, 0, 861, 571))
        self.SagIcerikFrame.setStyleSheet(u"")
        self.SagIcerikFrame.setFrameShape(QFrame.StyledPanel)
        self.SagIcerikFrame.setFrameShadow(QFrame.Raised)
        self.SayfaWidget = QStackedWidget(self.SagIcerikFrame)
        self.SayfaWidget.setObjectName(u"SayfaWidget")
        self.SayfaWidget.setGeometry(QRect(0, 0, 861, 571))
        self.SayfaWidget.setStyleSheet(u"")
        self.cuzdanWidget = QWidget()
        self.cuzdanWidget.setObjectName(u"cuzdanWidget")
        self.cuzdanIcerik = QGroupBox(self.cuzdanWidget)
        self.cuzdanIcerik.setObjectName(u"cuzdanIcerik")
        self.cuzdanIcerik.setGeometry(QRect(10, 10, 841, 551))
        self.cuzdanIcerik.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.FrameXLM = QFrame(self.cuzdanIcerik)
        self.FrameXLM.setObjectName(u"FrameXLM")
        self.FrameXLM.setGeometry(QRect(600, 460, 231, 81))
        self.FrameXLM.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameXLM.setFrameShape(QFrame.StyledPanel)
        self.FrameXLM.setFrameShadow(QFrame.Raised)
        self.LogoXLM = QLabel(self.FrameXLM)
        self.LogoXLM.setObjectName(u"LogoXLM")
        self.LogoXLM.setGeometry(QRect(10, 10, 61, 61))
        self.LogoXLM.setPixmap(QPixmap(u":/simge/simge/XLM.png"))
        self.LogoXLM.setScaledContents(True)
        self.TextXLM = QLabel(self.FrameXLM)
        self.TextXLM.setObjectName(u"TextXLM")
        self.TextXLM.setGeometry(QRect(80, 10, 141, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Historic")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.TextXLM.setFont(font2)
        self.TextXLM.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetXLM = QLabel(self.FrameXLM)
        self.AdetXLM.setObjectName(u"AdetXLM")
        self.AdetXLM.setGeometry(QRect(80, 30, 141, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Historic")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.AdetXLM.setFont(font3)
        self.AdetXLM.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLXLM = QLabel(self.FrameXLM)
        self.TLXLM.setObjectName(u"TLXLM")
        self.TLXLM.setGeometry(QRect(80, 50, 141, 21))
        self.TLXLM.setFont(font3)
        self.TLXLM.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLXLM.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.FrameDOGE = QFrame(self.cuzdanIcerik)
        self.FrameDOGE.setObjectName(u"FrameDOGE")
        self.FrameDOGE.setGeometry(QRect(600, 370, 231, 81))
        self.FrameDOGE.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameDOGE.setFrameShape(QFrame.StyledPanel)
        self.FrameDOGE.setFrameShadow(QFrame.Raised)
        self.LogoDOGE = QLabel(self.FrameDOGE)
        self.LogoDOGE.setObjectName(u"LogoDOGE")
        self.LogoDOGE.setGeometry(QRect(10, 10, 61, 61))
        self.LogoDOGE.setPixmap(QPixmap(u":/simge/simge/DOGE.png"))
        self.LogoDOGE.setScaledContents(True)
        self.TextDOGE = QLabel(self.FrameDOGE)
        self.TextDOGE.setObjectName(u"TextDOGE")
        self.TextDOGE.setGeometry(QRect(80, 10, 141, 21))
        self.TextDOGE.setFont(font2)
        self.TextDOGE.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetDOGE = QLabel(self.FrameDOGE)
        self.AdetDOGE.setObjectName(u"AdetDOGE")
        self.AdetDOGE.setGeometry(QRect(80, 30, 141, 21))
        self.AdetDOGE.setFont(font3)
        self.AdetDOGE.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetDOGE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TLDOGE = QLabel(self.FrameDOGE)
        self.TLDOGE.setObjectName(u"TLDOGE")
        self.TLDOGE.setGeometry(QRect(80, 50, 141, 21))
        self.TLDOGE.setFont(font3)
        self.TLDOGE.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLDOGE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.LogoDOGE.raise_()
        self.AdetDOGE.raise_()
        self.TextDOGE.raise_()
        self.TLDOGE.raise_()
        self.FrameHOT = QFrame(self.cuzdanIcerik)
        self.FrameHOT.setObjectName(u"FrameHOT")
        self.FrameHOT.setGeometry(QRect(600, 280, 231, 81))
        self.FrameHOT.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameHOT.setFrameShape(QFrame.StyledPanel)
        self.FrameHOT.setFrameShadow(QFrame.Raised)
        self.LogoHOT = QLabel(self.FrameHOT)
        self.LogoHOT.setObjectName(u"LogoHOT")
        self.LogoHOT.setGeometry(QRect(10, 10, 61, 61))
        self.LogoHOT.setPixmap(QPixmap(u":/simge/simge/HOT.png"))
        self.LogoHOT.setScaledContents(True)
        self.TextHOT = QLabel(self.FrameHOT)
        self.TextHOT.setObjectName(u"TextHOT")
        self.TextHOT.setGeometry(QRect(80, 10, 141, 21))
        self.TextHOT.setFont(font2)
        self.TextHOT.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetHOT = QLabel(self.FrameHOT)
        self.AdetHOT.setObjectName(u"AdetHOT")
        self.AdetHOT.setGeometry(QRect(80, 30, 141, 21))
        self.AdetHOT.setFont(font3)
        self.AdetHOT.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLHOT = QLabel(self.FrameHOT)
        self.TLHOT.setObjectName(u"TLHOT")
        self.TLHOT.setGeometry(QRect(80, 50, 141, 21))
        self.TLHOT.setFont(font3)
        self.TLHOT.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLHOT.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.FrameAVAX = QFrame(self.cuzdanIcerik)
        self.FrameAVAX.setObjectName(u"FrameAVAX")
        self.FrameAVAX.setGeometry(QRect(10, 460, 231, 80))
        self.FrameAVAX.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameAVAX.setFrameShape(QFrame.StyledPanel)
        self.FrameAVAX.setFrameShadow(QFrame.Raised)
        self.LogoAVAX = QLabel(self.FrameAVAX)
        self.LogoAVAX.setObjectName(u"LogoAVAX")
        self.LogoAVAX.setGeometry(QRect(10, 10, 61, 61))
        self.LogoAVAX.setPixmap(QPixmap(u":/simge/simge/AVAX.png"))
        self.LogoAVAX.setScaledContents(True)
        self.TextAVAX = QLabel(self.FrameAVAX)
        self.TextAVAX.setObjectName(u"TextAVAX")
        self.TextAVAX.setGeometry(QRect(80, 10, 141, 21))
        self.TextAVAX.setFont(font2)
        self.TextAVAX.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetAVAX = QLabel(self.FrameAVAX)
        self.AdetAVAX.setObjectName(u"AdetAVAX")
        self.AdetAVAX.setGeometry(QRect(80, 30, 141, 21))
        self.AdetAVAX.setFont(font3)
        self.AdetAVAX.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLAVAX = QLabel(self.FrameAVAX)
        self.TLAVAX.setObjectName(u"TLAVAX")
        self.TLAVAX.setGeometry(QRect(80, 50, 141, 21))
        self.TLAVAX.setFont(font3)
        self.TLAVAX.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLAVAX.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.FrameXRP = QFrame(self.cuzdanIcerik)
        self.FrameXRP.setObjectName(u"FrameXRP")
        self.FrameXRP.setGeometry(QRect(600, 190, 231, 81))
        self.FrameXRP.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameXRP.setFrameShape(QFrame.StyledPanel)
        self.FrameXRP.setFrameShadow(QFrame.Raised)
        self.LogoXRP = QLabel(self.FrameXRP)
        self.LogoXRP.setObjectName(u"LogoXRP")
        self.LogoXRP.setGeometry(QRect(10, 10, 61, 61))
        self.LogoXRP.setPixmap(QPixmap(u":/simge/simge/XRP.png"))
        self.LogoXRP.setScaledContents(True)
        self.TextXRP = QLabel(self.FrameXRP)
        self.TextXRP.setObjectName(u"TextXRP")
        self.TextXRP.setGeometry(QRect(80, 10, 141, 21))
        self.TextXRP.setFont(font2)
        self.TextXRP.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetXRP = QLabel(self.FrameXRP)
        self.AdetXRP.setObjectName(u"AdetXRP")
        self.AdetXRP.setGeometry(QRect(80, 30, 141, 21))
        self.AdetXRP.setFont(font3)
        self.AdetXRP.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLXRP = QLabel(self.FrameXRP)
        self.TLXRP.setObjectName(u"TLXRP")
        self.TLXRP.setGeometry(QRect(80, 50, 141, 21))
        self.TLXRP.setFont(font3)
        self.TLXRP.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.FrameCHZ = QFrame(self.cuzdanIcerik)
        self.FrameCHZ.setObjectName(u"FrameCHZ")
        self.FrameCHZ.setGeometry(QRect(10, 370, 231, 81))
        self.FrameCHZ.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameCHZ.setFrameShape(QFrame.StyledPanel)
        self.FrameCHZ.setFrameShadow(QFrame.Raised)
        self.LogoCHZ = QLabel(self.FrameCHZ)
        self.LogoCHZ.setObjectName(u"LogoCHZ")
        self.LogoCHZ.setGeometry(QRect(10, 10, 61, 61))
        self.LogoCHZ.setPixmap(QPixmap(u":/simge/simge/CHZ.png"))
        self.LogoCHZ.setScaledContents(True)
        self.TextCHZ = QLabel(self.FrameCHZ)
        self.TextCHZ.setObjectName(u"TextCHZ")
        self.TextCHZ.setGeometry(QRect(80, 10, 141, 21))
        self.TextCHZ.setFont(font2)
        self.TextCHZ.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetCHZ = QLabel(self.FrameCHZ)
        self.AdetCHZ.setObjectName(u"AdetCHZ")
        self.AdetCHZ.setGeometry(QRect(80, 30, 141, 21))
        self.AdetCHZ.setFont(font3)
        self.AdetCHZ.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLCHZ = QLabel(self.FrameCHZ)
        self.TLCHZ.setObjectName(u"TLCHZ")
        self.TLCHZ.setGeometry(QRect(80, 50, 141, 21))
        self.TLCHZ.setFont(font3)
        self.TLCHZ.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLCHZ.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.FrameBTC = QFrame(self.cuzdanIcerik)
        self.FrameBTC.setObjectName(u"FrameBTC")
        self.FrameBTC.setGeometry(QRect(10, 190, 231, 81))
        self.FrameBTC.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameBTC.setFrameShape(QFrame.StyledPanel)
        self.FrameBTC.setFrameShadow(QFrame.Raised)
        self.LogoBTC = QLabel(self.FrameBTC)
        self.LogoBTC.setObjectName(u"LogoBTC")
        self.LogoBTC.setGeometry(QRect(10, 10, 61, 61))
        self.LogoBTC.setPixmap(QPixmap(u":/simge/simge/BTC.png"))
        self.LogoBTC.setScaledContents(True)
        self.TextBTC = QLabel(self.FrameBTC)
        self.TextBTC.setObjectName(u"TextBTC")
        self.TextBTC.setGeometry(QRect(80, 10, 141, 21))
        self.TextBTC.setFont(font2)
        self.TextBTC.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetBTC = QLabel(self.FrameBTC)
        self.AdetBTC.setObjectName(u"AdetBTC")
        self.AdetBTC.setGeometry(QRect(80, 30, 141, 21))
        self.AdetBTC.setFont(font3)
        self.AdetBTC.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetBTC.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TLBTC = QLabel(self.FrameBTC)
        self.TLBTC.setObjectName(u"TLBTC")
        self.TLBTC.setGeometry(QRect(80, 50, 141, 21))
        self.TLBTC.setFont(font3)
        self.TLBTC.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLBTC.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.FrameETH = QFrame(self.cuzdanIcerik)
        self.FrameETH.setObjectName(u"FrameETH")
        self.FrameETH.setGeometry(QRect(10, 280, 231, 81))
        self.FrameETH.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameETH.setFrameShape(QFrame.StyledPanel)
        self.FrameETH.setFrameShadow(QFrame.Raised)
        self.LogoETH = QLabel(self.FrameETH)
        self.LogoETH.setObjectName(u"LogoETH")
        self.LogoETH.setGeometry(QRect(10, 10, 61, 61))
        self.LogoETH.setPixmap(QPixmap(u":/simge/simge/ETH.png"))
        self.LogoETH.setScaledContents(True)
        self.TextETH = QLabel(self.FrameETH)
        self.TextETH.setObjectName(u"TextETH")
        self.TextETH.setGeometry(QRect(80, 10, 141, 21))
        self.TextETH.setFont(font2)
        self.TextETH.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.AdetETH = QLabel(self.FrameETH)
        self.AdetETH.setObjectName(u"AdetETH")
        self.AdetETH.setGeometry(QRect(80, 30, 141, 21))
        self.AdetETH.setFont(font3)
        self.AdetETH.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLETH = QLabel(self.FrameETH)
        self.TLETH.setObjectName(u"TLETH")
        self.TLETH.setGeometry(QRect(80, 50, 141, 21))
        self.TLETH.setFont(font3)
        self.TLETH.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.TLETH.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ParaGoruntu = QGroupBox(self.cuzdanIcerik)
        self.ParaGoruntu.setObjectName(u"ParaGoruntu")
        self.ParaGoruntu.setGeometry(QRect(10, 10, 821, 171))
        self.toplamParaDegisim = QLabel(self.ParaGoruntu)
        self.toplamParaDegisim.setObjectName(u"toplamParaDegisim")
        self.toplamParaDegisim.setGeometry(QRect(170, 100, 281, 51))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Historic")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.toplamParaDegisim.setFont(font4)
        self.toplamParaDegisim.setStyleSheet(u"QLabel{\n"
"	background: transparent;	\n"
"}")
        self.toplamParaDegisim.setAlignment(Qt.AlignCenter)
        self.toplamPara = QLabel(self.ParaGoruntu)
        self.toplamPara.setObjectName(u"toplamPara")
        self.toplamPara.setGeometry(QRect(10, 10, 601, 81))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Historic")
        font5.setPointSize(50)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(75)
        font5.setStrikeOut(False)
        self.toplamPara.setFont(font5)
        self.toplamPara.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.toplamPara.setAlignment(Qt.AlignCenter)
        self.cuzdanPastaGrafik = QWidget(self.ParaGoruntu)
        self.cuzdanPastaGrafik.setObjectName(u"cuzdanPastaGrafik")
        self.cuzdanPastaGrafik.setGeometry(QRect(620, 0, 191, 171))
        self.cuzdanDegerGrafik = QWidget(self.cuzdanIcerik)
        self.cuzdanDegerGrafik.setObjectName(u"cuzdanDegerGrafik")
        self.cuzdanDegerGrafik.setGeometry(QRect(240, 220, 361, 301))
        self.SayfaWidget.addWidget(self.cuzdanWidget)
        self.bakiyeWidget = QWidget()
        self.bakiyeWidget.setObjectName(u"bakiyeWidget")
        self.bakiyeWidgetBox = QGroupBox(self.bakiyeWidget)
        self.bakiyeWidgetBox.setObjectName(u"bakiyeWidgetBox")
        self.bakiyeWidgetBox.setGeometry(QRect(10, 10, 841, 551))
        self.bakiyeWidgetBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.ParaAtBox = QGroupBox(self.bakiyeWidgetBox)
        self.ParaAtBox.setObjectName(u"ParaAtBox")
        self.ParaAtBox.setGeometry(QRect(20, 110, 391, 311))
        self.ParaAtBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.MiktarParaAt = QLineEdit(self.ParaAtBox)
        self.MiktarParaAt.setObjectName(u"MiktarParaAt")
        self.MiktarParaAt.setGeometry(QRect(20, 70, 351, 41))
        font6 = QFont()
        font6.setPointSize(12)
        self.MiktarParaAt.setFont(font6)
        self.MiktarParaAt.setStyleSheet(u"QLineEdit{\n"
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
        self.MiktarParaAt.setMaxLength(12)
        self.MiktarParaAt.setEchoMode(QLineEdit.Normal)
        self.CVCAtma = QLineEdit(self.ParaAtBox)
        self.CVCAtma.setObjectName(u"CVCAtma")
        self.CVCAtma.setGeometry(QRect(20, 190, 351, 41))
        self.CVCAtma.setFont(font6)
        self.CVCAtma.setStyleSheet(u"QLineEdit{\n"
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
        self.CVCAtma.setMaxLength(3)
        self.CVCAtma.setEchoMode(QLineEdit.Normal)
        self.ParaAtmaText = QLabel(self.ParaAtBox)
        self.ParaAtmaText.setObjectName(u"ParaAtmaText")
        self.ParaAtmaText.setGeometry(QRect(20, 10, 351, 41))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Historic")
        font7.setPointSize(15)
        self.ParaAtmaText.setFont(font7)
        self.ParaAtmaText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ParaAtmaText.setAlignment(Qt.AlignCenter)
        self.ParaYatirButon = QPushButton(self.ParaAtBox)
        self.ParaYatirButon.setObjectName(u"ParaYatirButon")
        self.ParaYatirButon.setGeometry(QRect(20, 250, 351, 41))
        self.ParaYatirButon.setFont(font6)
        self.ParaYatirButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.ParaYatirButon.setStyleSheet(u"QPushButton {	\n"
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
        self.ParaYatirButon.setIconSize(QSize(20, 20))
        self.KKNoAtma1 = QLineEdit(self.ParaAtBox)
        self.KKNoAtma1.setObjectName(u"KKNoAtma1")
        self.KKNoAtma1.setGeometry(QRect(20, 130, 80, 41))
        self.KKNoAtma1.setFont(font6)
        self.KKNoAtma1.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoAtma1.setMaxLength(4)
        self.KKNoAtma1.setEchoMode(QLineEdit.Normal)
        self.KKNoAtma2 = QLineEdit(self.ParaAtBox)
        self.KKNoAtma2.setObjectName(u"KKNoAtma2")
        self.KKNoAtma2.setGeometry(QRect(110, 130, 80, 41))
        self.KKNoAtma2.setFont(font6)
        self.KKNoAtma2.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoAtma2.setMaxLength(4)
        self.KKNoAtma2.setEchoMode(QLineEdit.Normal)
        self.KKNoAtma3 = QLineEdit(self.ParaAtBox)
        self.KKNoAtma3.setObjectName(u"KKNoAtma3")
        self.KKNoAtma3.setGeometry(QRect(200, 130, 80, 41))
        self.KKNoAtma3.setFont(font6)
        self.KKNoAtma3.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoAtma3.setMaxLength(4)
        self.KKNoAtma3.setEchoMode(QLineEdit.Normal)
        self.KKNoAtma4 = QLineEdit(self.ParaAtBox)
        self.KKNoAtma4.setObjectName(u"KKNoAtma4")
        self.KKNoAtma4.setGeometry(QRect(290, 130, 80, 41))
        self.KKNoAtma4.setFont(font6)
        self.KKNoAtma4.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoAtma4.setMaxLength(4)
        self.KKNoAtma4.setEchoMode(QLineEdit.Normal)
        self.ParaCekBox = QGroupBox(self.bakiyeWidgetBox)
        self.ParaCekBox.setObjectName(u"ParaCekBox")
        self.ParaCekBox.setEnabled(True)
        self.ParaCekBox.setGeometry(QRect(430, 110, 391, 311))
        self.ParaCekBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.ParaCekmeText = QLabel(self.ParaCekBox)
        self.ParaCekmeText.setObjectName(u"ParaCekmeText")
        self.ParaCekmeText.setGeometry(QRect(20, 10, 351, 41))
        self.ParaCekmeText.setFont(font7)
        self.ParaCekmeText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ParaCekmeText.setAlignment(Qt.AlignCenter)
        self.MiktarParaCek = QLineEdit(self.ParaCekBox)
        self.MiktarParaCek.setObjectName(u"MiktarParaCek")
        self.MiktarParaCek.setGeometry(QRect(20, 70, 281, 41))
        self.MiktarParaCek.setFont(font6)
        self.MiktarParaCek.setStyleSheet(u"QLineEdit{\n"
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
        self.MiktarParaCek.setMaxLength(12)
        self.MiktarParaCek.setEchoMode(QLineEdit.Normal)
        self.KKNoCekme1 = QLineEdit(self.ParaCekBox)
        self.KKNoCekme1.setObjectName(u"KKNoCekme1")
        self.KKNoCekme1.setGeometry(QRect(20, 130, 80, 41))
        self.KKNoCekme1.setFont(font6)
        self.KKNoCekme1.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoCekme1.setMaxLength(4)
        self.KKNoCekme1.setEchoMode(QLineEdit.Normal)
        self.CVCCekme = QLineEdit(self.ParaCekBox)
        self.CVCCekme.setObjectName(u"CVCCekme")
        self.CVCCekme.setGeometry(QRect(20, 190, 351, 41))
        self.CVCCekme.setFont(font6)
        self.CVCCekme.setStyleSheet(u"QLineEdit{\n"
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
        self.CVCCekme.setMaxLength(3)
        self.CVCCekme.setEchoMode(QLineEdit.Normal)
        self.ParaCekButon = QPushButton(self.ParaCekBox)
        self.ParaCekButon.setObjectName(u"ParaCekButon")
        self.ParaCekButon.setGeometry(QRect(20, 250, 351, 41))
        self.ParaCekButon.setFont(font6)
        self.ParaCekButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.ParaCekButon.setStyleSheet(u"QPushButton {	\n"
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
        self.ParaCekButon.setIconSize(QSize(20, 20))
        self.KKNoCekme2 = QLineEdit(self.ParaCekBox)
        self.KKNoCekme2.setObjectName(u"KKNoCekme2")
        self.KKNoCekme2.setGeometry(QRect(110, 130, 80, 41))
        self.KKNoCekme2.setFont(font6)
        self.KKNoCekme2.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoCekme2.setMaxLength(4)
        self.KKNoCekme2.setEchoMode(QLineEdit.Normal)
        self.KKNoCekme3 = QLineEdit(self.ParaCekBox)
        self.KKNoCekme3.setObjectName(u"KKNoCekme3")
        self.KKNoCekme3.setGeometry(QRect(200, 130, 80, 41))
        self.KKNoCekme3.setFont(font6)
        self.KKNoCekme3.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoCekme3.setMaxLength(4)
        self.KKNoCekme3.setEchoMode(QLineEdit.Normal)
        self.KKNoCekme4 = QLineEdit(self.ParaCekBox)
        self.KKNoCekme4.setObjectName(u"KKNoCekme4")
        self.KKNoCekme4.setGeometry(QRect(290, 130, 80, 41))
        self.KKNoCekme4.setFont(font6)
        self.KKNoCekme4.setStyleSheet(u"QLineEdit{\n"
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
        self.KKNoCekme4.setMaxLength(4)
        self.KKNoCekme4.setEchoMode(QLineEdit.Normal)
        self.ParaCekMaxButon = QPushButton(self.ParaCekBox)
        self.ParaCekMaxButon.setObjectName(u"ParaCekMaxButon")
        self.ParaCekMaxButon.setGeometry(QRect(310, 70, 61, 41))
        self.ParaCekMaxButon.setFont(font6)
        self.ParaCekMaxButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.ParaCekMaxButon.setStyleSheet(u"QPushButton {	\n"
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
        self.ParaCekMaxButon.setIconSize(QSize(20, 20))
        self.BakiyeIslemText = QLabel(self.bakiyeWidgetBox)
        self.BakiyeIslemText.setObjectName(u"BakiyeIslemText")
        self.BakiyeIslemText.setGeometry(QRect(300, 430, 241, 31))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(10)
        self.BakiyeIslemText.setFont(font8)
        self.BakiyeIslemText.setStyleSheet(u"")
        self.BakiyeIslemText.setAlignment(Qt.AlignCenter)
        self.SayfaWidget.addWidget(self.bakiyeWidget)
        self.piyasaWidget = QWidget()
        self.piyasaWidget.setObjectName(u"piyasaWidget")
        self.piyasaIcerik = QGroupBox(self.piyasaWidget)
        self.piyasaIcerik.setObjectName(u"piyasaIcerik")
        self.piyasaIcerik.setGeometry(QRect(10, 10, 841, 551))
        self.piyasaIcerik.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.FrameBTCPiyasa = QFrame(self.piyasaIcerik)
        self.FrameBTCPiyasa.setObjectName(u"FrameBTCPiyasa")
        self.FrameBTCPiyasa.setGeometry(QRect(20, 20, 391, 111))
        self.FrameBTCPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameBTCPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameBTCPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoBTC_2 = QLabel(self.FrameBTCPiyasa)
        self.LogoBTC_2.setObjectName(u"LogoBTC_2")
        self.LogoBTC_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoBTC_2.setPixmap(QPixmap(u":/simge/simge/BTC.png"))
        self.LogoBTC_2.setScaledContents(True)
        self.TextBTC_2 = QLabel(self.FrameBTCPiyasa)
        self.TextBTC_2.setObjectName(u"TextBTC_2")
        self.TextBTC_2.setGeometry(QRect(90, 16, 141, 20))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Historic")
        font9.setPointSize(13)
        font9.setBold(True)
        font9.setWeight(75)
        self.TextBTC_2.setFont(font9)
        self.TextBTC_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerBTC = QLabel(self.FrameBTCPiyasa)
        self.DegerBTC.setObjectName(u"DegerBTC")
        self.DegerBTC.setGeometry(QRect(90, 40, 131, 21))
        self.DegerBTC.setFont(font3)
        self.DegerBTC.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisBTC = QLabel(self.FrameBTCPiyasa)
        self.ArtisBTC.setObjectName(u"ArtisBTC")
        self.ArtisBTC.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisBTC.setFont(font3)
        self.ArtisBTC.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisBTC.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisBTCYuzde = QLabel(self.FrameBTCPiyasa)
        self.ArtisBTCYuzde.setObjectName(u"ArtisBTCYuzde")
        self.ArtisBTCYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisBTCYuzde.setFont(font3)
        self.ArtisBTCYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisBTCYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoBTCAl = QPushButton(self.FrameBTCPiyasa)
        self.KriptoBTCAl.setObjectName(u"KriptoBTCAl")
        self.KriptoBTCAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoBTCAl.setFont(font6)
        self.KriptoBTCAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoBTCAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoBTCAl.setIconSize(QSize(20, 20))
        self.KriptoBTCDetay = QPushButton(self.FrameBTCPiyasa)
        self.KriptoBTCDetay.setObjectName(u"KriptoBTCDetay")
        self.KriptoBTCDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoBTCDetay.setFont(font6)
        self.KriptoBTCDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoBTCDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoBTCDetay.setIconSize(QSize(20, 20))
        self.FrameETHPiyasa = QFrame(self.piyasaIcerik)
        self.FrameETHPiyasa.setObjectName(u"FrameETHPiyasa")
        self.FrameETHPiyasa.setGeometry(QRect(430, 20, 391, 111))
        self.FrameETHPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameETHPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameETHPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoETH_2 = QLabel(self.FrameETHPiyasa)
        self.LogoETH_2.setObjectName(u"LogoETH_2")
        self.LogoETH_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoETH_2.setPixmap(QPixmap(u":/simge/simge/ETH.png"))
        self.LogoETH_2.setScaledContents(True)
        self.TextETH_2 = QLabel(self.FrameETHPiyasa)
        self.TextETH_2.setObjectName(u"TextETH_2")
        self.TextETH_2.setGeometry(QRect(90, 16, 151, 20))
        self.TextETH_2.setFont(font9)
        self.TextETH_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerETH = QLabel(self.FrameETHPiyasa)
        self.DegerETH.setObjectName(u"DegerETH")
        self.DegerETH.setGeometry(QRect(90, 40, 131, 21))
        self.DegerETH.setFont(font3)
        self.DegerETH.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisETH = QLabel(self.FrameETHPiyasa)
        self.ArtisETH.setObjectName(u"ArtisETH")
        self.ArtisETH.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisETH.setFont(font3)
        self.ArtisETH.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisETH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisETHYuzde = QLabel(self.FrameETHPiyasa)
        self.ArtisETHYuzde.setObjectName(u"ArtisETHYuzde")
        self.ArtisETHYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisETHYuzde.setFont(font3)
        self.ArtisETHYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisETHYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoETHDetay = QPushButton(self.FrameETHPiyasa)
        self.KriptoETHDetay.setObjectName(u"KriptoETHDetay")
        self.KriptoETHDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoETHDetay.setFont(font6)
        self.KriptoETHDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoETHDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoETHDetay.setIconSize(QSize(20, 20))
        self.KriptoETHAl = QPushButton(self.FrameETHPiyasa)
        self.KriptoETHAl.setObjectName(u"KriptoETHAl")
        self.KriptoETHAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoETHAl.setFont(font6)
        self.KriptoETHAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoETHAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoETHAl.setIconSize(QSize(20, 20))
        self.FrameAVAXPiyasa = QFrame(self.piyasaIcerik)
        self.FrameAVAXPiyasa.setObjectName(u"FrameAVAXPiyasa")
        self.FrameAVAXPiyasa.setGeometry(QRect(20, 150, 391, 111))
        self.FrameAVAXPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameAVAXPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameAVAXPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoAVAX_2 = QLabel(self.FrameAVAXPiyasa)
        self.LogoAVAX_2.setObjectName(u"LogoAVAX_2")
        self.LogoAVAX_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoAVAX_2.setPixmap(QPixmap(u":/simge/simge/AVAX.png"))
        self.LogoAVAX_2.setScaledContents(True)
        self.TextAVAX_2 = QLabel(self.FrameAVAXPiyasa)
        self.TextAVAX_2.setObjectName(u"TextAVAX_2")
        self.TextAVAX_2.setGeometry(QRect(90, 16, 171, 20))
        self.TextAVAX_2.setFont(font9)
        self.TextAVAX_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerAVAX = QLabel(self.FrameAVAXPiyasa)
        self.DegerAVAX.setObjectName(u"DegerAVAX")
        self.DegerAVAX.setGeometry(QRect(90, 40, 131, 21))
        self.DegerAVAX.setFont(font3)
        self.DegerAVAX.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisAVAX = QLabel(self.FrameAVAXPiyasa)
        self.ArtisAVAX.setObjectName(u"ArtisAVAX")
        self.ArtisAVAX.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisAVAX.setFont(font3)
        self.ArtisAVAX.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisAVAX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisAVAXYuzde = QLabel(self.FrameAVAXPiyasa)
        self.ArtisAVAXYuzde.setObjectName(u"ArtisAVAXYuzde")
        self.ArtisAVAXYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisAVAXYuzde.setFont(font3)
        self.ArtisAVAXYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisAVAXYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoAVAXAl = QPushButton(self.FrameAVAXPiyasa)
        self.KriptoAVAXAl.setObjectName(u"KriptoAVAXAl")
        self.KriptoAVAXAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoAVAXAl.setFont(font6)
        self.KriptoAVAXAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoAVAXAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoAVAXAl.setIconSize(QSize(20, 20))
        self.KriptoAVAXDetay = QPushButton(self.FrameAVAXPiyasa)
        self.KriptoAVAXDetay.setObjectName(u"KriptoAVAXDetay")
        self.KriptoAVAXDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoAVAXDetay.setFont(font6)
        self.KriptoAVAXDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoAVAXDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoAVAXDetay.setIconSize(QSize(20, 20))
        self.FrameCHZPiyasa = QFrame(self.piyasaIcerik)
        self.FrameCHZPiyasa.setObjectName(u"FrameCHZPiyasa")
        self.FrameCHZPiyasa.setGeometry(QRect(430, 150, 391, 111))
        self.FrameCHZPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameCHZPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameCHZPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoCHZ_2 = QLabel(self.FrameCHZPiyasa)
        self.LogoCHZ_2.setObjectName(u"LogoCHZ_2")
        self.LogoCHZ_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoCHZ_2.setPixmap(QPixmap(u":/simge/simge/CHZ.png"))
        self.LogoCHZ_2.setScaledContents(True)
        self.TextCHZ_2 = QLabel(self.FrameCHZPiyasa)
        self.TextCHZ_2.setObjectName(u"TextCHZ_2")
        self.TextCHZ_2.setGeometry(QRect(90, 16, 141, 20))
        self.TextCHZ_2.setFont(font9)
        self.TextCHZ_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerCHZ = QLabel(self.FrameCHZPiyasa)
        self.DegerCHZ.setObjectName(u"DegerCHZ")
        self.DegerCHZ.setGeometry(QRect(90, 40, 131, 21))
        self.DegerCHZ.setFont(font3)
        self.DegerCHZ.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisCHZ = QLabel(self.FrameCHZPiyasa)
        self.ArtisCHZ.setObjectName(u"ArtisCHZ")
        self.ArtisCHZ.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisCHZ.setFont(font3)
        self.ArtisCHZ.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisCHZ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisCHZYuzde = QLabel(self.FrameCHZPiyasa)
        self.ArtisCHZYuzde.setObjectName(u"ArtisCHZYuzde")
        self.ArtisCHZYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisCHZYuzde.setFont(font3)
        self.ArtisCHZYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisCHZYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoCHZAl = QPushButton(self.FrameCHZPiyasa)
        self.KriptoCHZAl.setObjectName(u"KriptoCHZAl")
        self.KriptoCHZAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoCHZAl.setFont(font6)
        self.KriptoCHZAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoCHZAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoCHZAl.setIconSize(QSize(20, 20))
        self.KriptoCHZDetay = QPushButton(self.FrameCHZPiyasa)
        self.KriptoCHZDetay.setObjectName(u"KriptoCHZDetay")
        self.KriptoCHZDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoCHZDetay.setFont(font6)
        self.KriptoCHZDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoCHZDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoCHZDetay.setIconSize(QSize(20, 20))
        self.FrameDOGEPiyasa = QFrame(self.piyasaIcerik)
        self.FrameDOGEPiyasa.setObjectName(u"FrameDOGEPiyasa")
        self.FrameDOGEPiyasa.setGeometry(QRect(20, 280, 391, 111))
        self.FrameDOGEPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameDOGEPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameDOGEPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoDOGE_2 = QLabel(self.FrameDOGEPiyasa)
        self.LogoDOGE_2.setObjectName(u"LogoDOGE_2")
        self.LogoDOGE_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoDOGE_2.setPixmap(QPixmap(u":/simge/simge/DOGE.png"))
        self.LogoDOGE_2.setScaledContents(True)
        self.TextDOGE_2 = QLabel(self.FrameDOGEPiyasa)
        self.TextDOGE_2.setObjectName(u"TextDOGE_2")
        self.TextDOGE_2.setGeometry(QRect(90, 16, 161, 21))
        self.TextDOGE_2.setFont(font9)
        self.TextDOGE_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerDOGE = QLabel(self.FrameDOGEPiyasa)
        self.DegerDOGE.setObjectName(u"DegerDOGE")
        self.DegerDOGE.setGeometry(QRect(90, 40, 131, 21))
        self.DegerDOGE.setFont(font3)
        self.DegerDOGE.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisDOGE = QLabel(self.FrameDOGEPiyasa)
        self.ArtisDOGE.setObjectName(u"ArtisDOGE")
        self.ArtisDOGE.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisDOGE.setFont(font3)
        self.ArtisDOGE.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisDOGE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisDOGEYuzde = QLabel(self.FrameDOGEPiyasa)
        self.ArtisDOGEYuzde.setObjectName(u"ArtisDOGEYuzde")
        self.ArtisDOGEYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisDOGEYuzde.setFont(font3)
        self.ArtisDOGEYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisDOGEYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoDOGEAl = QPushButton(self.FrameDOGEPiyasa)
        self.KriptoDOGEAl.setObjectName(u"KriptoDOGEAl")
        self.KriptoDOGEAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoDOGEAl.setFont(font6)
        self.KriptoDOGEAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoDOGEAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoDOGEAl.setIconSize(QSize(20, 20))
        self.KriptoDOGEDetay = QPushButton(self.FrameDOGEPiyasa)
        self.KriptoDOGEDetay.setObjectName(u"KriptoDOGEDetay")
        self.KriptoDOGEDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoDOGEDetay.setFont(font6)
        self.KriptoDOGEDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoDOGEDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoDOGEDetay.setIconSize(QSize(20, 20))
        self.FrameHOTPiyasa = QFrame(self.piyasaIcerik)
        self.FrameHOTPiyasa.setObjectName(u"FrameHOTPiyasa")
        self.FrameHOTPiyasa.setGeometry(QRect(430, 280, 391, 111))
        self.FrameHOTPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameHOTPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameHOTPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoHOT_2 = QLabel(self.FrameHOTPiyasa)
        self.LogoHOT_2.setObjectName(u"LogoHOT_2")
        self.LogoHOT_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoHOT_2.setPixmap(QPixmap(u":/simge/simge/HOT.png"))
        self.LogoHOT_2.setScaledContents(True)
        self.TextHOT_2 = QLabel(self.FrameHOTPiyasa)
        self.TextHOT_2.setObjectName(u"TextHOT_2")
        self.TextHOT_2.setGeometry(QRect(90, 16, 141, 20))
        self.TextHOT_2.setFont(font9)
        self.TextHOT_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerHOT = QLabel(self.FrameHOTPiyasa)
        self.DegerHOT.setObjectName(u"DegerHOT")
        self.DegerHOT.setGeometry(QRect(90, 40, 131, 21))
        self.DegerHOT.setFont(font3)
        self.DegerHOT.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisHOT = QLabel(self.FrameHOTPiyasa)
        self.ArtisHOT.setObjectName(u"ArtisHOT")
        self.ArtisHOT.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisHOT.setFont(font3)
        self.ArtisHOT.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisHOT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisHOTYuzde = QLabel(self.FrameHOTPiyasa)
        self.ArtisHOTYuzde.setObjectName(u"ArtisHOTYuzde")
        self.ArtisHOTYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisHOTYuzde.setFont(font3)
        self.ArtisHOTYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisHOTYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoHOTAl = QPushButton(self.FrameHOTPiyasa)
        self.KriptoHOTAl.setObjectName(u"KriptoHOTAl")
        self.KriptoHOTAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoHOTAl.setFont(font6)
        self.KriptoHOTAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoHOTAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoHOTAl.setIconSize(QSize(20, 20))
        self.KriptoHOTDetay = QPushButton(self.FrameHOTPiyasa)
        self.KriptoHOTDetay.setObjectName(u"KriptoHOTDetay")
        self.KriptoHOTDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoHOTDetay.setFont(font6)
        self.KriptoHOTDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoHOTDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoHOTDetay.setIconSize(QSize(20, 20))
        self.FrameXRPPiyasa = QFrame(self.piyasaIcerik)
        self.FrameXRPPiyasa.setObjectName(u"FrameXRPPiyasa")
        self.FrameXRPPiyasa.setGeometry(QRect(20, 410, 391, 111))
        self.FrameXRPPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameXRPPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameXRPPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoXRP_2 = QLabel(self.FrameXRPPiyasa)
        self.LogoXRP_2.setObjectName(u"LogoXRP_2")
        self.LogoXRP_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoXRP_2.setPixmap(QPixmap(u":/simge/simge/XRP.png"))
        self.LogoXRP_2.setScaledContents(True)
        self.TextXRP_2 = QLabel(self.FrameXRPPiyasa)
        self.TextXRP_2.setObjectName(u"TextXRP_2")
        self.TextXRP_2.setGeometry(QRect(90, 16, 141, 21))
        self.TextXRP_2.setFont(font9)
        self.TextXRP_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerXRP = QLabel(self.FrameXRPPiyasa)
        self.DegerXRP.setObjectName(u"DegerXRP")
        self.DegerXRP.setGeometry(QRect(90, 40, 131, 21))
        self.DegerXRP.setFont(font3)
        self.DegerXRP.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisXRP = QLabel(self.FrameXRPPiyasa)
        self.ArtisXRP.setObjectName(u"ArtisXRP")
        self.ArtisXRP.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisXRP.setFont(font3)
        self.ArtisXRP.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisXRP.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisXRPYuzde = QLabel(self.FrameXRPPiyasa)
        self.ArtisXRPYuzde.setObjectName(u"ArtisXRPYuzde")
        self.ArtisXRPYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisXRPYuzde.setFont(font3)
        self.ArtisXRPYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisXRPYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoXRPAl = QPushButton(self.FrameXRPPiyasa)
        self.KriptoXRPAl.setObjectName(u"KriptoXRPAl")
        self.KriptoXRPAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoXRPAl.setFont(font6)
        self.KriptoXRPAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoXRPAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoXRPAl.setIconSize(QSize(20, 20))
        self.KriptoXRPDetay = QPushButton(self.FrameXRPPiyasa)
        self.KriptoXRPDetay.setObjectName(u"KriptoXRPDetay")
        self.KriptoXRPDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoXRPDetay.setFont(font6)
        self.KriptoXRPDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoXRPDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoXRPDetay.setIconSize(QSize(20, 20))
        self.FrameXLMPiyasa = QFrame(self.piyasaIcerik)
        self.FrameXLMPiyasa.setObjectName(u"FrameXLMPiyasa")
        self.FrameXLMPiyasa.setGeometry(QRect(430, 410, 391, 111))
        self.FrameXLMPiyasa.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.FrameXLMPiyasa.setFrameShape(QFrame.StyledPanel)
        self.FrameXLMPiyasa.setFrameShadow(QFrame.Raised)
        self.LogoXLM_2 = QLabel(self.FrameXLMPiyasa)
        self.LogoXLM_2.setObjectName(u"LogoXLM_2")
        self.LogoXLM_2.setGeometry(QRect(10, 10, 61, 61))
        self.LogoXLM_2.setPixmap(QPixmap(u":/simge/simge/XLM.png"))
        self.LogoXLM_2.setScaledContents(True)
        self.TextXLM_2 = QLabel(self.FrameXLMPiyasa)
        self.TextXLM_2.setObjectName(u"TextXLM_2")
        self.TextXLM_2.setGeometry(QRect(90, 16, 141, 20))
        self.TextXLM_2.setFont(font9)
        self.TextXLM_2.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.DegerXLM = QLabel(self.FrameXLMPiyasa)
        self.DegerXLM.setObjectName(u"DegerXLM")
        self.DegerXLM.setGeometry(QRect(90, 40, 131, 21))
        self.DegerXLM.setFont(font3)
        self.DegerXLM.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisXLM = QLabel(self.FrameXLMPiyasa)
        self.ArtisXLM.setObjectName(u"ArtisXLM")
        self.ArtisXLM.setGeometry(QRect(270, 40, 111, 21))
        self.ArtisXLM.setFont(font3)
        self.ArtisXLM.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisXLM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ArtisXLMYuzde = QLabel(self.FrameXLMPiyasa)
        self.ArtisXLMYuzde.setObjectName(u"ArtisXLMYuzde")
        self.ArtisXLMYuzde.setGeometry(QRect(290, 10, 91, 31))
        self.ArtisXLMYuzde.setFont(font3)
        self.ArtisXLMYuzde.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.ArtisXLMYuzde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.KriptoXLMAl = QPushButton(self.FrameXLMPiyasa)
        self.KriptoXLMAl.setObjectName(u"KriptoXLMAl")
        self.KriptoXLMAl.setGeometry(QRect(10, 80, 181, 21))
        self.KriptoXLMAl.setFont(font6)
        self.KriptoXLMAl.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoXLMAl.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoXLMAl.setIconSize(QSize(20, 20))
        self.KriptoXLMDetay = QPushButton(self.FrameXLMPiyasa)
        self.KriptoXLMDetay.setObjectName(u"KriptoXLMDetay")
        self.KriptoXLMDetay.setGeometry(QRect(200, 80, 181, 21))
        self.KriptoXLMDetay.setFont(font6)
        self.KriptoXLMDetay.setCursor(QCursor(Qt.PointingHandCursor))
        self.KriptoXLMDetay.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(73, 147, 221);\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.KriptoXLMDetay.setIconSize(QSize(20, 20))
        self.SayfaWidget.addWidget(self.piyasaWidget)
        self.ayarlarWidget = QWidget()
        self.ayarlarWidget.setObjectName(u"ayarlarWidget")
        self.ayarlarIcerik = QGroupBox(self.ayarlarWidget)
        self.ayarlarIcerik.setObjectName(u"ayarlarIcerik")
        self.ayarlarIcerik.setGeometry(QRect(10, 10, 841, 551))
        self.ayarlarIcerik.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.HesapAyarBox = QGroupBox(self.ayarlarIcerik)
        self.HesapAyarBox.setObjectName(u"HesapAyarBox")
        self.HesapAyarBox.setGeometry(QRect(20, 110, 391, 311))
        self.HesapAyarBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.IsimText = QLineEdit(self.HesapAyarBox)
        self.IsimText.setObjectName(u"IsimText")
        self.IsimText.setGeometry(QRect(20, 70, 351, 41))
        self.IsimText.setFont(font6)
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
        self.SoyisimText = QLineEdit(self.HesapAyarBox)
        self.SoyisimText.setObjectName(u"SoyisimText")
        self.SoyisimText.setGeometry(QRect(20, 130, 351, 41))
        self.SoyisimText.setFont(font6)
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
        self.MailText = QLineEdit(self.HesapAyarBox)
        self.MailText.setObjectName(u"MailText")
        self.MailText.setGeometry(QRect(20, 190, 351, 41))
        self.MailText.setFont(font6)
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
        self.HesapAyarText = QLabel(self.HesapAyarBox)
        self.HesapAyarText.setObjectName(u"HesapAyarText")
        self.HesapAyarText.setGeometry(QRect(20, 10, 351, 41))
        self.HesapAyarText.setFont(font7)
        self.HesapAyarText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.HesapAyarText.setAlignment(Qt.AlignCenter)
        self.KaydetButon = QPushButton(self.HesapAyarBox)
        self.KaydetButon.setObjectName(u"KaydetButon")
        self.KaydetButon.setGeometry(QRect(20, 250, 351, 41))
        self.KaydetButon.setFont(font6)
        self.KaydetButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.KaydetButon.setStyleSheet(u"QPushButton {	\n"
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
        self.KaydetButon.setIconSize(QSize(20, 20))
        self.SifreAyarBox = QGroupBox(self.ayarlarIcerik)
        self.SifreAyarBox.setObjectName(u"SifreAyarBox")
        self.SifreAyarBox.setGeometry(QRect(430, 110, 391, 311))
        self.SifreAyarText = QLabel(self.SifreAyarBox)
        self.SifreAyarText.setObjectName(u"SifreAyarText")
        self.SifreAyarText.setGeometry(QRect(20, 10, 351, 41))
        self.SifreAyarText.setFont(font7)
        self.SifreAyarText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.SifreAyarText.setAlignment(Qt.AlignCenter)
        self.SifreEski = QLineEdit(self.SifreAyarBox)
        self.SifreEski.setObjectName(u"SifreEski")
        self.SifreEski.setGeometry(QRect(20, 70, 351, 41))
        self.SifreEski.setFont(font6)
        self.SifreEski.setStyleSheet(u"QLineEdit{\n"
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
        self.SifreEski.setEchoMode(QLineEdit.Password)
        self.SifreText = QLineEdit(self.SifreAyarBox)
        self.SifreText.setObjectName(u"SifreText")
        self.SifreText.setGeometry(QRect(20, 130, 351, 41))
        self.SifreText.setFont(font6)
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
        self.SifreTekrar = QLineEdit(self.SifreAyarBox)
        self.SifreTekrar.setObjectName(u"SifreTekrar")
        self.SifreTekrar.setGeometry(QRect(20, 190, 351, 41))
        self.SifreTekrar.setFont(font6)
        self.SifreTekrar.setStyleSheet(u"QLineEdit{\n"
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
        self.SifreTekrar.setEchoMode(QLineEdit.Password)
        self.SifreGuncelle = QPushButton(self.SifreAyarBox)
        self.SifreGuncelle.setObjectName(u"SifreGuncelle")
        self.SifreGuncelle.setGeometry(QRect(20, 250, 351, 41))
        self.SifreGuncelle.setFont(font6)
        self.SifreGuncelle.setCursor(QCursor(Qt.PointingHandCursor))
        self.SifreGuncelle.setStyleSheet(u"QPushButton {	\n"
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
        self.SifreGuncelle.setIconSize(QSize(20, 20))
        self.HesapSil = QPushButton(self.ayarlarIcerik)
        self.HesapSil.setObjectName(u"HesapSil")
        self.HesapSil.setGeometry(QRect(680, 490, 141, 41))
        self.HesapSil.setFont(font6)
        self.HesapSil.setCursor(QCursor(Qt.PointingHandCursor))
        self.HesapSil.setStyleSheet(u"QPushButton {	\n"
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
        self.HesapSil.setIconSize(QSize(20, 20))
        self.AyarlarIslemText = QLabel(self.ayarlarIcerik)
        self.AyarlarIslemText.setObjectName(u"AyarlarIslemText")
        self.AyarlarIslemText.setGeometry(QRect(300, 430, 241, 31))
        self.AyarlarIslemText.setFont(font8)
        self.AyarlarIslemText.setStyleSheet(u"")
        self.AyarlarIslemText.setAlignment(Qt.AlignCenter)
        self.SayfaWidget.addWidget(self.ayarlarWidget)
        self.kriptoSatAlWidget = QWidget()
        self.kriptoSatAlWidget.setObjectName(u"kriptoSatAlWidget")
        self.kriptoSatAlBox = QGroupBox(self.kriptoSatAlWidget)
        self.kriptoSatAlBox.setObjectName(u"kriptoSatAlBox")
        self.kriptoSatAlBox.setGeometry(QRect(10, 10, 841, 551))
        self.kriptoSatAlBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}")
        self.kriptoSatAlFrame = QFrame(self.kriptoSatAlBox)
        self.kriptoSatAlFrame.setObjectName(u"kriptoSatAlFrame")
        self.kriptoSatAlFrame.setGeometry(QRect(210, 30, 421, 121))
        self.kriptoSatAlFrame.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.kriptoSatAlFrame.setFrameShape(QFrame.StyledPanel)
        self.kriptoSatAlFrame.setFrameShadow(QFrame.Raised)
        self.kriptoSatAlLogo = QLabel(self.kriptoSatAlFrame)
        self.kriptoSatAlLogo.setObjectName(u"kriptoSatAlLogo")
        self.kriptoSatAlLogo.setGeometry(QRect(10, 10, 101, 101))
        self.kriptoSatAlLogo.setScaledContents(True)
        self.kriptoSatAlAdi = QLabel(self.kriptoSatAlFrame)
        self.kriptoSatAlAdi.setObjectName(u"kriptoSatAlAdi")
        self.kriptoSatAlAdi.setGeometry(QRect(130, 0, 281, 41))
        font10 = QFont()
        font10.setFamily(u"Segoe UI Historic")
        font10.setPointSize(15)
        font10.setBold(True)
        font10.setWeight(75)
        self.kriptoSatAlAdi.setFont(font10)
        self.kriptoSatAlAdi.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoSatAlAdi.setAlignment(Qt.AlignCenter)
        self.kriptoSatAlCuzdan = QLabel(self.kriptoSatAlFrame)
        self.kriptoSatAlCuzdan.setObjectName(u"kriptoSatAlCuzdan")
        self.kriptoSatAlCuzdan.setGeometry(QRect(130, 70, 281, 41))
        font11 = QFont()
        font11.setFamily(u"Segoe UI Historic")
        font11.setPointSize(15)
        font11.setBold(False)
        font11.setWeight(50)
        self.kriptoSatAlCuzdan.setFont(font11)
        self.kriptoSatAlCuzdan.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoSatAlCuzdan.setAlignment(Qt.AlignCenter)
        self.kriptoSatAlDeger = QLabel(self.kriptoSatAlFrame)
        self.kriptoSatAlDeger.setObjectName(u"kriptoSatAlDeger")
        self.kriptoSatAlDeger.setGeometry(QRect(130, 40, 281, 31))
        self.kriptoSatAlDeger.setFont(font11)
        self.kriptoSatAlDeger.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoSatAlDeger.setAlignment(Qt.AlignCenter)
        self.kriptoSatBox = QGroupBox(self.kriptoSatAlBox)
        self.kriptoSatBox.setObjectName(u"kriptoSatBox")
        self.kriptoSatBox.setGeometry(QRect(430, 180, 391, 261))
        self.kriptoSatBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.kriptoSatMiktar = QLineEdit(self.kriptoSatBox)
        self.kriptoSatMiktar.setObjectName(u"kriptoSatMiktar")
        self.kriptoSatMiktar.setGeometry(QRect(20, 70, 281, 41))
        self.kriptoSatMiktar.setFont(font6)
        self.kriptoSatMiktar.setStyleSheet(u"QLineEdit{\n"
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
        self.kriptoSatMiktar.setMaxLength(12)
        self.kriptoSatMiktar.setEchoMode(QLineEdit.Normal)
        self.kriptoAdiSat = QLabel(self.kriptoSatBox)
        self.kriptoAdiSat.setObjectName(u"kriptoAdiSat")
        self.kriptoAdiSat.setGeometry(QRect(20, 10, 351, 41))
        self.kriptoAdiSat.setFont(font7)
        self.kriptoAdiSat.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoAdiSat.setAlignment(Qt.AlignCenter)
        self.kriptoSatButon = QPushButton(self.kriptoSatBox)
        self.kriptoSatButon.setObjectName(u"kriptoSatButon")
        self.kriptoSatButon.setGeometry(QRect(20, 190, 351, 41))
        self.kriptoSatButon.setFont(font6)
        self.kriptoSatButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.kriptoSatButon.setStyleSheet(u"QPushButton {	\n"
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
        self.kriptoSatButon.setIconSize(QSize(20, 20))
        self.kriptoSatMax = QPushButton(self.kriptoSatBox)
        self.kriptoSatMax.setObjectName(u"kriptoSatMax")
        self.kriptoSatMax.setGeometry(QRect(310, 70, 61, 41))
        self.kriptoSatMax.setFont(font6)
        self.kriptoSatMax.setCursor(QCursor(Qt.PointingHandCursor))
        self.kriptoSatMax.setStyleSheet(u"QPushButton {	\n"
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
        self.kriptoSatMax.setIconSize(QSize(20, 20))
        self.kriptoSatSifre = QLineEdit(self.kriptoSatBox)
        self.kriptoSatSifre.setObjectName(u"kriptoSatSifre")
        self.kriptoSatSifre.setGeometry(QRect(20, 130, 351, 41))
        self.kriptoSatSifre.setFont(font6)
        self.kriptoSatSifre.setStyleSheet(u"QLineEdit{\n"
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
        self.kriptoSatSifre.setEchoMode(QLineEdit.Password)
        self.kriptoAlBox = QGroupBox(self.kriptoSatAlBox)
        self.kriptoAlBox.setObjectName(u"kriptoAlBox")
        self.kriptoAlBox.setGeometry(QRect(20, 180, 391, 261))
        self.kriptoAlBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.kriptoAlMiktar = QLineEdit(self.kriptoAlBox)
        self.kriptoAlMiktar.setObjectName(u"kriptoAlMiktar")
        self.kriptoAlMiktar.setGeometry(QRect(20, 70, 281, 41))
        self.kriptoAlMiktar.setFont(font6)
        self.kriptoAlMiktar.setStyleSheet(u"QLineEdit{\n"
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
        self.kriptoAlMiktar.setMaxLength(12)
        self.kriptoAlMiktar.setEchoMode(QLineEdit.Normal)
        self.kriptoAdiAl = QLabel(self.kriptoAlBox)
        self.kriptoAdiAl.setObjectName(u"kriptoAdiAl")
        self.kriptoAdiAl.setGeometry(QRect(20, 10, 351, 41))
        self.kriptoAdiAl.setFont(font7)
        self.kriptoAdiAl.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoAdiAl.setAlignment(Qt.AlignCenter)
        self.kriptoAlButon = QPushButton(self.kriptoAlBox)
        self.kriptoAlButon.setObjectName(u"kriptoAlButon")
        self.kriptoAlButon.setGeometry(QRect(20, 190, 351, 41))
        self.kriptoAlButon.setFont(font6)
        self.kriptoAlButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.kriptoAlButon.setStyleSheet(u"QPushButton {	\n"
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
        self.kriptoAlButon.setIconSize(QSize(20, 20))
        self.kriptoAlMax = QPushButton(self.kriptoAlBox)
        self.kriptoAlMax.setObjectName(u"kriptoAlMax")
        self.kriptoAlMax.setGeometry(QRect(310, 70, 61, 41))
        self.kriptoAlMax.setFont(font6)
        self.kriptoAlMax.setCursor(QCursor(Qt.PointingHandCursor))
        self.kriptoAlMax.setStyleSheet(u"QPushButton {	\n"
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
        self.kriptoAlMax.setIconSize(QSize(20, 20))
        self.kriptoAlSifre = QLineEdit(self.kriptoAlBox)
        self.kriptoAlSifre.setObjectName(u"kriptoAlSifre")
        self.kriptoAlSifre.setGeometry(QRect(20, 130, 351, 41))
        self.kriptoAlSifre.setFont(font6)
        self.kriptoAlSifre.setStyleSheet(u"QLineEdit{\n"
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
        self.kriptoAlSifre.setEchoMode(QLineEdit.Password)
        self.kriptoSatAlIslem = QLabel(self.kriptoSatAlBox)
        self.kriptoSatAlIslem.setObjectName(u"kriptoSatAlIslem")
        self.kriptoSatAlIslem.setGeometry(QRect(210, 450, 421, 31))
        self.kriptoSatAlIslem.setFont(font8)
        self.kriptoSatAlIslem.setStyleSheet(u"")
        self.kriptoSatAlIslem.setAlignment(Qt.AlignCenter)
        self.piyasaGeriButon_2 = QPushButton(self.kriptoSatAlBox)
        self.piyasaGeriButon_2.setObjectName(u"piyasaGeriButon_2")
        self.piyasaGeriButon_2.setGeometry(QRect(20, 20, 61, 31))
        self.piyasaGeriButon_2.setFont(font6)
        self.piyasaGeriButon_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.piyasaGeriButon_2.setStyleSheet(u"QPushButton {	\n"
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
        self.piyasaGeriButon_2.setIconSize(QSize(20, 20))
        self.SayfaWidget.addWidget(self.kriptoSatAlWidget)
        self.kriptoDetayWidget = QWidget()
        self.kriptoDetayWidget.setObjectName(u"kriptoDetayWidget")
        self.kriptoDetayWidget.setStyleSheet(u"background-color: rgb(60, 99, 161);")
        self.groupBox = QGroupBox(self.kriptoDetayWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 841, 551))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgb(210, 210, 210);\n"
"}\n"
"")
        self.kriptoDetayFrame = QFrame(self.groupBox)
        self.kriptoDetayFrame.setObjectName(u"kriptoDetayFrame")
        self.kriptoDetayFrame.setGeometry(QRect(140, 130, 561, 150))
        self.kriptoDetayFrame.setStyleSheet(u"QFrame{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.kriptoDetayFrame.setFrameShape(QFrame.StyledPanel)
        self.kriptoDetayFrame.setFrameShadow(QFrame.Raised)
        self.kriptoDetayHacim = QLabel(self.kriptoDetayFrame)
        self.kriptoDetayHacim.setObjectName(u"kriptoDetayHacim")
        self.kriptoDetayHacim.setGeometry(QRect(290, 100, 271, 51))
        font12 = QFont()
        font12.setFamily(u"Segoe UI Historic")
        font12.setPointSize(13)
        font12.setBold(False)
        font12.setWeight(50)
        self.kriptoDetayHacim.setFont(font12)
        self.kriptoDetayHacim.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayHacim.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayDegisim = QLabel(self.kriptoDetayFrame)
        self.kriptoDetayDegisim.setObjectName(u"kriptoDetayDegisim")
        self.kriptoDetayDegisim.setGeometry(QRect(10, 50, 271, 51))
        self.kriptoDetayDegisim.setFont(font12)
        self.kriptoDetayDegisim.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayDegisim.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayMax = QLabel(self.kriptoDetayFrame)
        self.kriptoDetayMax.setObjectName(u"kriptoDetayMax")
        self.kriptoDetayMax.setGeometry(QRect(290, 0, 271, 51))
        self.kriptoDetayMax.setFont(font12)
        self.kriptoDetayMax.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayMax.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayMin = QLabel(self.kriptoDetayFrame)
        self.kriptoDetayMin.setObjectName(u"kriptoDetayMin")
        self.kriptoDetayMin.setGeometry(QRect(290, 50, 271, 51))
        self.kriptoDetayMin.setFont(font12)
        self.kriptoDetayMin.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayMin.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayAcilis = QLabel(self.kriptoDetayFrame)
        self.kriptoDetayAcilis.setObjectName(u"kriptoDetayAcilis")
        self.kriptoDetayAcilis.setGeometry(QRect(10, 100, 271, 51))
        self.kriptoDetayAcilis.setFont(font12)
        self.kriptoDetayAcilis.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayAcilis.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayAnlik = QLabel(self.kriptoDetayFrame)
        self.kriptoDetayAnlik.setObjectName(u"kriptoDetayAnlik")
        self.kriptoDetayAnlik.setGeometry(QRect(10, 0, 271, 51))
        self.kriptoDetayAnlik.setFont(font12)
        self.kriptoDetayAnlik.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayAnlik.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayGrafik = QWidget(self.groupBox)
        self.kriptoDetayGrafik.setObjectName(u"kriptoDetayGrafik")
        self.kriptoDetayGrafik.setGeometry(QRect(180, 280, 461, 261))
        self.kriptoDetayGrafik.setStyleSheet(u"")
        self.kriptoDetayText = QLabel(self.groupBox)
        self.kriptoDetayText.setObjectName(u"kriptoDetayText")
        self.kriptoDetayText.setGeometry(QRect(290, 20, 401, 81))
        font13 = QFont()
        font13.setFamily(u"Segoe UI Historic")
        font13.setPointSize(35)
        font13.setBold(True)
        font13.setWeight(75)
        self.kriptoDetayText.setFont(font13)
        self.kriptoDetayText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}")
        self.kriptoDetayText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kriptoDetayLogo = QLabel(self.groupBox)
        self.kriptoDetayLogo.setObjectName(u"kriptoDetayLogo")
        self.kriptoDetayLogo.setGeometry(QRect(170, 20, 91, 91))
        self.kriptoDetayLogo.setScaledContents(True)
        self.piyasaGeriButon = QPushButton(self.groupBox)
        self.piyasaGeriButon.setObjectName(u"piyasaGeriButon")
        self.piyasaGeriButon.setGeometry(QRect(20, 20, 61, 31))
        self.piyasaGeriButon.setFont(font6)
        self.piyasaGeriButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.piyasaGeriButon.setStyleSheet(u"QPushButton {	\n"
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
        self.piyasaGeriButon.setIconSize(QSize(20, 20))
        self.SayfaWidget.addWidget(self.kriptoDetayWidget)
        self.UstFrame = QFrame(self.AnaFrame)
        self.UstFrame.setObjectName(u"UstFrame")
        self.UstFrame.setGeometry(QRect(0, 0, 931, 61))
        self.UstFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 75, 121);\n"
"}")
        self.UstFrame.setFrameShape(QFrame.StyledPanel)
        self.UstFrame.setFrameShadow(QFrame.Raised)
        self.LogoFrame = QFrame(self.UstFrame)
        self.LogoFrame.setObjectName(u"LogoFrame")
        self.LogoFrame.setGeometry(QRect(0, 0, 71, 61))
        self.LogoFrame.setFrameShape(QFrame.StyledPanel)
        self.LogoFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.LogoFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 51, 51))
        self.label.setPixmap(QPixmap(u":/simge/simge/logo.png"))
        self.label.setScaledContents(True)
        self.UstIcerikFrame = QFrame(self.UstFrame)
        self.UstIcerikFrame.setObjectName(u"UstIcerikFrame")
        self.UstIcerikFrame.setGeometry(QRect(70, 0, 861, 61))
        self.UstIcerikFrame.setFrameShape(QFrame.StyledPanel)
        self.UstIcerikFrame.setFrameShadow(QFrame.Raised)
        self.UstIcerikButonFrame = QFrame(self.UstIcerikFrame)
        self.UstIcerikButonFrame.setObjectName(u"UstIcerikButonFrame")
        self.UstIcerikButonFrame.setGeometry(QRect(0, 0, 861, 31))
        self.UstIcerikButonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(74, 125, 200);\n"
"}")
        self.UstIcerikButonFrame.setFrameShape(QFrame.StyledPanel)
        self.UstIcerikButonFrame.setFrameShadow(QFrame.Raised)
        self.ProgAdiFrame = QFrame(self.UstIcerikButonFrame)
        self.ProgAdiFrame.setObjectName(u"ProgAdiFrame")
        self.ProgAdiFrame.setGeometry(QRect(0, 0, 781, 31))
        self.ProgAdiFrame.setFrameShape(QFrame.StyledPanel)
        self.ProgAdiFrame.setFrameShadow(QFrame.Raised)
        self.ProgAdiText = QLabel(self.ProgAdiFrame)
        self.ProgAdiText.setObjectName(u"ProgAdiText")
        self.ProgAdiText.setGeometry(QRect(0, 5, 691, 21))
        font14 = QFont()
        font14.setFamily(u"Segoe UI Historic")
        font14.setPointSize(12)
        self.ProgAdiText.setFont(font14)
        self.ProgAdiText.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"	margin-left: 5px;\n"
"}")
        self.ProgButonlar = QFrame(self.UstIcerikButonFrame)
        self.ProgButonlar.setObjectName(u"ProgButonlar")
        self.ProgButonlar.setGeometry(QRect(780, 0, 81, 31))
        self.ProgButonlar.setStyleSheet(u"")
        self.ProgButonlar.setFrameShape(QFrame.StyledPanel)
        self.ProgButonlar.setFrameShadow(QFrame.Raised)
        self.asagiButton = QPushButton(self.ProgButonlar)
        self.asagiButton.setObjectName(u"asagiButton")
        self.asagiButton.setGeometry(QRect(0, 0, 41, 31))
        sizePolicy.setHeightForWidth(self.asagiButton.sizePolicy().hasHeightForWidth())
        self.asagiButton.setSizePolicy(sizePolicy)
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
        icon4 = QIcon()
        icon4.addFile(u":/simge/simge/s-asagi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.asagiButton.setIcon(icon4)
        self.kapatButon = QPushButton(self.ProgButonlar)
        self.kapatButon.setObjectName(u"kapatButon")
        self.kapatButon.setGeometry(QRect(40, 0, 41, 31))
        sizePolicy.setHeightForWidth(self.kapatButon.sizePolicy().hasHeightForWidth())
        self.kapatButon.setSizePolicy(sizePolicy)
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
        icon5 = QIcon()
        icon5.addFile(u":/simge/simge/s-kapat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kapatButon.setIcon(icon5)
        self.UstIcerikButonFrame_2 = QFrame(self.UstIcerikFrame)
        self.UstIcerikButonFrame_2.setObjectName(u"UstIcerikButonFrame_2")
        self.UstIcerikButonFrame_2.setGeometry(QRect(0, 30, 861, 31))
        self.UstIcerikButonFrame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(51, 87, 139);\n"
"}")
        self.UstIcerikButonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.UstIcerikButonFrame_2.setFrameShadow(QFrame.Raised)
        self.kullaniciBakiye = QLabel(self.UstIcerikButonFrame_2)
        self.kullaniciBakiye.setObjectName(u"kullaniciBakiye")
        self.kullaniciBakiye.setGeometry(QRect(430, 0, 291, 31))
        self.kullaniciBakiye.setFont(font14)
        self.kullaniciBakiye.setStyleSheet(u"QLabel{\n"
"	background: transparent;\n"
"}\n"
"")
        self.kullaniciBakiye.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.BakiyeIslemButon = QPushButton(self.UstIcerikButonFrame_2)
        self.BakiyeIslemButon.setObjectName(u"BakiyeIslemButon")
        self.BakiyeIslemButon.setGeometry(QRect(729, 0, 131, 31))
        self.BakiyeIslemButon.setFont(font6)
        self.BakiyeIslemButon.setCursor(QCursor(Qt.PointingHandCursor))
        self.BakiyeIslemButon.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 141, 211);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(53, 110, 163);\n"
"}\n"
"")
        self.BakiyeIslemButon.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.AnaFrame)

        AnaEkran.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.BakiyeIslemButon, self.cuzdanButon)
        QWidget.setTabOrder(self.cuzdanButon, self.piyasaButon)
        QWidget.setTabOrder(self.piyasaButon, self.ayarlarButon)
        QWidget.setTabOrder(self.ayarlarButon, self.cikisButon)
        QWidget.setTabOrder(self.cikisButon, self.asagiButton)
        QWidget.setTabOrder(self.asagiButton, self.kapatButon)
        QWidget.setTabOrder(self.kapatButon, self.MiktarParaAt)
        QWidget.setTabOrder(self.MiktarParaAt, self.KKNoAtma1)
        QWidget.setTabOrder(self.KKNoAtma1, self.KKNoAtma2)
        QWidget.setTabOrder(self.KKNoAtma2, self.KKNoAtma3)
        QWidget.setTabOrder(self.KKNoAtma3, self.KKNoAtma4)
        QWidget.setTabOrder(self.KKNoAtma4, self.CVCAtma)
        QWidget.setTabOrder(self.CVCAtma, self.ParaYatirButon)
        QWidget.setTabOrder(self.ParaYatirButon, self.MiktarParaCek)
        QWidget.setTabOrder(self.MiktarParaCek, self.KKNoCekme1)
        QWidget.setTabOrder(self.KKNoCekme1, self.KKNoCekme2)
        QWidget.setTabOrder(self.KKNoCekme2, self.KKNoCekme3)
        QWidget.setTabOrder(self.KKNoCekme3, self.KKNoCekme4)
        QWidget.setTabOrder(self.KKNoCekme4, self.CVCCekme)
        QWidget.setTabOrder(self.CVCCekme, self.ParaCekButon)
        QWidget.setTabOrder(self.ParaCekButon, self.KriptoBTCAl)
        QWidget.setTabOrder(self.KriptoBTCAl, self.KriptoBTCDetay)
        QWidget.setTabOrder(self.KriptoBTCDetay, self.KriptoETHAl)
        QWidget.setTabOrder(self.KriptoETHAl, self.KriptoETHDetay)
        QWidget.setTabOrder(self.KriptoETHDetay, self.KriptoAVAXAl)
        QWidget.setTabOrder(self.KriptoAVAXAl, self.KriptoAVAXDetay)
        QWidget.setTabOrder(self.KriptoAVAXDetay, self.KriptoCHZAl)
        QWidget.setTabOrder(self.KriptoCHZAl, self.KriptoCHZDetay)
        QWidget.setTabOrder(self.KriptoCHZDetay, self.KriptoDOGEAl)
        QWidget.setTabOrder(self.KriptoDOGEAl, self.KriptoDOGEDetay)
        QWidget.setTabOrder(self.KriptoDOGEDetay, self.KriptoHOTAl)
        QWidget.setTabOrder(self.KriptoHOTAl, self.KriptoHOTDetay)
        QWidget.setTabOrder(self.KriptoHOTDetay, self.KriptoXRPAl)
        QWidget.setTabOrder(self.KriptoXRPAl, self.KriptoXRPDetay)
        QWidget.setTabOrder(self.KriptoXRPDetay, self.KriptoXLMAl)
        QWidget.setTabOrder(self.KriptoXLMAl, self.KriptoXLMDetay)
        QWidget.setTabOrder(self.KriptoXLMDetay, self.IsimText)
        QWidget.setTabOrder(self.IsimText, self.SoyisimText)
        QWidget.setTabOrder(self.SoyisimText, self.MailText)
        QWidget.setTabOrder(self.MailText, self.KaydetButon)
        QWidget.setTabOrder(self.KaydetButon, self.SifreEski)
        QWidget.setTabOrder(self.SifreEski, self.SifreText)
        QWidget.setTabOrder(self.SifreText, self.SifreTekrar)
        QWidget.setTabOrder(self.SifreTekrar, self.SifreGuncelle)
        QWidget.setTabOrder(self.SifreGuncelle, self.HesapSil)
        QWidget.setTabOrder(self.HesapSil, self.kriptoAlMiktar)
        QWidget.setTabOrder(self.kriptoAlMiktar, self.kriptoAlSifre)
        QWidget.setTabOrder(self.kriptoAlSifre, self.kriptoAlButon)
        QWidget.setTabOrder(self.kriptoAlButon, self.kriptoAlMax)
        QWidget.setTabOrder(self.kriptoAlMax, self.kriptoSatMiktar)
        QWidget.setTabOrder(self.kriptoSatMiktar, self.kriptoSatSifre)
        QWidget.setTabOrder(self.kriptoSatSifre, self.kriptoSatButon)
        QWidget.setTabOrder(self.kriptoSatButon, self.kriptoSatMax)
        QWidget.setTabOrder(self.kriptoSatMax, self.piyasaGeriButon)

        self.retranslateUi(AnaEkran)

        self.SayfaWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AnaEkran)
    # setupUi

    def retranslateUi(self, AnaEkran):
        AnaEkran.setWindowTitle(QCoreApplication.translate("AnaEkran", u"MainWindow", None))
        self.cuzdanButon.setText("")
        self.piyasaButon.setText("")
#if QT_CONFIG(tooltip)
        self.cikisButon.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cikisButon.setText("")
        self.ayarlarButon.setText("")
        self.cuzdanIcerik.setTitle("")
        self.LogoXLM.setText("")
        self.TextXLM.setText(QCoreApplication.translate("AnaEkran", u"Stellar (XLM)", None))
        self.AdetXLM.setText(QCoreApplication.translate("AnaEkran", u"0 XLM", None))
        self.TLXLM.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoDOGE.setText("")
        self.TextDOGE.setText(QCoreApplication.translate("AnaEkran", u"Dogecoin (DOGE)", None))
        self.AdetDOGE.setText(QCoreApplication.translate("AnaEkran", u"0 DOGE", None))
        self.TLDOGE.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoHOT.setText("")
        self.TextHOT.setText(QCoreApplication.translate("AnaEkran", u"Holo (HOT)", None))
        self.AdetHOT.setText(QCoreApplication.translate("AnaEkran", u"0 HOT", None))
        self.TLHOT.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoAVAX.setText("")
        self.TextAVAX.setText(QCoreApplication.translate("AnaEkran", u"Avalanche (AVAX)", None))
        self.AdetAVAX.setText(QCoreApplication.translate("AnaEkran", u"0 AVAX", None))
        self.TLAVAX.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoXRP.setText("")
        self.TextXRP.setText(QCoreApplication.translate("AnaEkran", u"Ripple (XRP)", None))
        self.AdetXRP.setText(QCoreApplication.translate("AnaEkran", u"0 XRP", None))
        self.TLXRP.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoCHZ.setText("")
        self.TextCHZ.setText(QCoreApplication.translate("AnaEkran", u"Chiliz (CHZ)", None))
        self.AdetCHZ.setText(QCoreApplication.translate("AnaEkran", u"0 CHZ", None))
        self.TLCHZ.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoBTC.setText("")
        self.TextBTC.setText(QCoreApplication.translate("AnaEkran", u"Bitcoin (BTC)", None))
        self.AdetBTC.setText(QCoreApplication.translate("AnaEkran", u"0 BTC", None))
        self.TLBTC.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.LogoETH.setText("")
        self.TextETH.setText(QCoreApplication.translate("AnaEkran", u"Ethereum (ETH)", None))
        self.AdetETH.setText(QCoreApplication.translate("AnaEkran", u"0 ETH", None))
        self.TLETH.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ParaGoruntu.setTitle("")
        self.toplamParaDegisim.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.toplamPara.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.bakiyeWidgetBox.setTitle("")
        self.ParaAtBox.setTitle("")
        self.MiktarParaAt.setText("")
        self.MiktarParaAt.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Miktar (TL) (\u00d6rn: 1250.5)", None))
        self.CVCAtma.setText("")
        self.CVCAtma.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"CVC", None))
        self.ParaAtmaText.setText(QCoreApplication.translate("AnaEkran", u"Para Atma", None))
        self.ParaYatirButon.setText(QCoreApplication.translate("AnaEkran", u"Yat\u0131r", None))
        self.KKNoAtma1.setText("")
        self.KKNoAtma1.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Kredi", None))
        self.KKNoAtma2.setText("")
        self.KKNoAtma2.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Kart\u0131", None))
        self.KKNoAtma3.setText("")
        self.KKNoAtma3.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"No", None))
        self.KKNoAtma4.setText("")
        self.KKNoAtma4.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"4 Hane", None))
        self.ParaCekBox.setTitle("")
        self.ParaCekmeText.setText(QCoreApplication.translate("AnaEkran", u"Para \u00c7ekme", None))
        self.MiktarParaCek.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Miktar (TL) (\u00d6rn: 1250.5)", None))
        self.KKNoCekme1.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Kredi", None))
        self.CVCCekme.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"CVC", None))
        self.ParaCekButon.setText(QCoreApplication.translate("AnaEkran", u"\u00c7ek", None))
        self.KKNoCekme2.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Kart\u0131", None))
        self.KKNoCekme3.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"No", None))
        self.KKNoCekme4.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"4 Hane", None))
        self.ParaCekMaxButon.setText(QCoreApplication.translate("AnaEkran", u"Max", None))
        self.BakiyeIslemText.setText("")
        self.piyasaIcerik.setTitle("")
        self.LogoBTC_2.setText("")
        self.TextBTC_2.setText(QCoreApplication.translate("AnaEkran", u"Bitcoin (BTC)", None))
        self.DegerBTC.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisBTC.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisBTCYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoBTCAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoBTCDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.LogoETH_2.setText("")
        self.TextETH_2.setText(QCoreApplication.translate("AnaEkran", u"Ethereum (ETH)", None))
        self.DegerETH.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisETH.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisETHYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoETHDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.KriptoETHAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.LogoAVAX_2.setText("")
        self.TextAVAX_2.setText(QCoreApplication.translate("AnaEkran", u"Avalanche (AVAX)", None))
        self.DegerAVAX.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisAVAX.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisAVAXYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoAVAXAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoAVAXDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.LogoCHZ_2.setText("")
        self.TextCHZ_2.setText(QCoreApplication.translate("AnaEkran", u"Chiliz (CHZ)", None))
        self.DegerCHZ.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisCHZ.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisCHZYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoCHZAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoCHZDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.LogoDOGE_2.setText("")
        self.TextDOGE_2.setText(QCoreApplication.translate("AnaEkran", u"Dogecoin (DOGE)", None))
        self.DegerDOGE.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisDOGE.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisDOGEYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoDOGEAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoDOGEDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.LogoHOT_2.setText("")
        self.TextHOT_2.setText(QCoreApplication.translate("AnaEkran", u"Holo (HOT)", None))
        self.DegerHOT.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisHOT.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisHOTYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoHOTAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoHOTDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.LogoXRP_2.setText("")
        self.TextXRP_2.setText(QCoreApplication.translate("AnaEkran", u"Ripple (XRP)", None))
        self.DegerXRP.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisXRP.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisXRPYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoXRPAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoXRPDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.LogoXLM_2.setText("")
        self.TextXLM_2.setText(QCoreApplication.translate("AnaEkran", u"Stellar (XLM)", None))
        self.DegerXLM.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisXLM.setText(QCoreApplication.translate("AnaEkran", u"0 TL", None))
        self.ArtisXLMYuzde.setText(QCoreApplication.translate("AnaEkran", u"0%", None))
        self.KriptoXLMAl.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al/Sat", None))
        self.KriptoXLMDetay.setText(QCoreApplication.translate("AnaEkran", u"Detay", None))
        self.ayarlarIcerik.setTitle("")
        self.HesapAyarBox.setTitle("")
        self.IsimText.setText("")
        self.IsimText.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"\u0130sim", None))
        self.SoyisimText.setText("")
        self.SoyisimText.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Soyisim", None))
        self.MailText.setText("")
        self.MailText.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"E-Posta", None))
        self.HesapAyarText.setText(QCoreApplication.translate("AnaEkran", u"Hesap Ayarlar\u0131", None))
        self.KaydetButon.setText(QCoreApplication.translate("AnaEkran", u"Kaydet", None))
        self.SifreAyarBox.setTitle("")
        self.SifreAyarText.setText(QCoreApplication.translate("AnaEkran", u"\u015eifre Ayarlar\u0131", None))
        self.SifreEski.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Eski \u015eifre", None))
        self.SifreText.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Yeni \u015eifre", None))
        self.SifreTekrar.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Yeni \u015eifre Tekrar\u0131", None))
        self.SifreGuncelle.setText(QCoreApplication.translate("AnaEkran", u"Kaydet", None))
        self.HesapSil.setText(QCoreApplication.translate("AnaEkran", u"Hesab\u0131 Sil", None))
        self.AyarlarIslemText.setText("")
        self.kriptoSatAlBox.setTitle("")
        self.kriptoSatAlLogo.setText("")
        self.kriptoSatAlAdi.setText("")
        self.kriptoSatAlCuzdan.setText("")
        self.kriptoSatAlDeger.setText("")
        self.kriptoSatBox.setTitle("")
        self.kriptoSatMiktar.setText("")
        self.kriptoSatMiktar.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Adet (Kripto) (\u00d6rn: 1000.25)", None))
        self.kriptoAdiSat.setText(QCoreApplication.translate("AnaEkran", u"Kripto Sat", None))
        self.kriptoSatButon.setText(QCoreApplication.translate("AnaEkran", u"Sat", None))
        self.kriptoSatMax.setText(QCoreApplication.translate("AnaEkran", u"Max", None))
        self.kriptoSatSifre.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Hesap \u015eifresi", None))
        self.kriptoAlBox.setTitle("")
        self.kriptoAlMiktar.setText("")
        self.kriptoAlMiktar.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Miktar (TL) (\u00d6rn: 1250.5)", None))
        self.kriptoAdiAl.setText(QCoreApplication.translate("AnaEkran", u"Kripto Sat\u0131n Al", None))
        self.kriptoAlButon.setText(QCoreApplication.translate("AnaEkran", u"Sat\u0131n Al", None))
        self.kriptoAlMax.setText(QCoreApplication.translate("AnaEkran", u"Max", None))
        self.kriptoAlSifre.setPlaceholderText(QCoreApplication.translate("AnaEkran", u"Hesap \u015eifresi", None))
        self.kriptoSatAlIslem.setText("")
        self.piyasaGeriButon_2.setText(QCoreApplication.translate("AnaEkran", u"Geri", None))
        self.groupBox.setTitle("")
        self.kriptoDetayHacim.setText(QCoreApplication.translate("AnaEkran", u"24s  Hacim: 0 TL", None))
        self.kriptoDetayDegisim.setText(QCoreApplication.translate("AnaEkran", u"De\u011fi\u015fim: 0 TL (0%)", None))
        self.kriptoDetayMax.setText(QCoreApplication.translate("AnaEkran", u"En Y\u00fcksek: 0 TL", None))
        self.kriptoDetayMin.setText(QCoreApplication.translate("AnaEkran", u"En D\u00fc\u015f\u00fck: 0 TL", None))
        self.kriptoDetayAcilis.setText(QCoreApplication.translate("AnaEkran", u"A\u00e7\u0131l\u0131\u015f Fiyat\u0131: 0 TL", None))
        self.kriptoDetayAnlik.setText(QCoreApplication.translate("AnaEkran", u"Anl\u0131k De\u011fer: 0 TL", None))
        self.kriptoDetayText.setText("")
        self.kriptoDetayLogo.setText("")
        self.piyasaGeriButon.setText(QCoreApplication.translate("AnaEkran", u"Geri", None))
        self.label.setText("")
        self.ProgAdiText.setText(QCoreApplication.translate("AnaEkran", u"Kriptogram", None))
#if QT_CONFIG(tooltip)
        self.asagiButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.asagiButton.setText("")
#if QT_CONFIG(tooltip)
        self.kapatButon.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.kapatButon.setText("")
        self.kullaniciBakiye.setText(QCoreApplication.translate("AnaEkran", u"Bakiye: 0 TL", None))
        self.BakiyeIslemButon.setText(QCoreApplication.translate("AnaEkran", u"Bakiye \u0130\u015flemleri", None))
    # retranslateUi

