from fonksiyonlar import *
global fiyat


class AnaEkran(QMainWindow):
    def __init__(self, eposta, sifre):
        QMainWindow.__init__(self, parent=None)
        self.ui = Ui_AnaEkran()
        self.ui.setupUi(self)
        self.setWindowTitle('Kriptogram')
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(45, 75, 121))
        self.ui.AnaFrame.setGraphicsEffect(self.shadow)
        self.ui.ProgAdiFrame.mouseMoveEvent = self.moveWindow
        self._kripto_fiyat = fiyat
        self._anlik_ekran = 0
        self.vt = CuzdanBilgi(eposta, sifre)
        self._id = self.vt.kullanici_id
        self._eposta = self.vt.kullanici_eposta
        self._sifre = self.vt.kullanici_sifre
        self._isim = self.vt.kullanici_isim
        self._soyisim = self.vt.kullanici_soyisim
        self._bakiye = self.vt.kullanici_bakiye
        self._cuzdancoin = self.vt.kullanici_kripto
        self._secilencoin = -1
        self.bakiye_islem()
        self._sayac = 0
        self._cuzdandeger = 0
        self.ui.cuzdanButon.clicked.connect(lambda: self.cuzdan_goruntule())
        self.ui.piyasaButon.clicked.connect(lambda: self.piyasa_goster())
        self.ui.piyasaGeriButon.clicked.connect(lambda: self.piyasa_goster())
        self.ui.piyasaGeriButon_2.clicked.connect(lambda: self.piyasa_goster())
        self.ui.ayarlarButon.clicked.connect(lambda: self.ayarlar_goruntule(1))
        self.ui.cikisButon.clicked.connect(lambda: self.cikis_yap())
        self.ui.asagiButton.clicked.connect(lambda: self.showMinimized())
        self.ui.kapatButon.clicked.connect(lambda: self.close())
        self.ui.HesapSil.clicked.connect(lambda: self.hesap_silme())
        self.ui.BakiyeIslemButon.clicked.connect(lambda: self.bakiye_goruntule(1))
        self.ui.KriptoDOGEAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(0, 1))
        self.ui.KriptoBTCAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(1, 1))
        self.ui.KriptoHOTAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(2, 1))
        self.ui.KriptoXRPAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(3, 1))
        self.ui.KriptoAVAXAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(4, 1))
        self.ui.KriptoCHZAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(5, 1))
        self.ui.KriptoETHAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(6, 1))
        self.ui.KriptoXLMAl.clicked.connect(lambda: self.kripto_al_sat_goruntule(7, 1))
        self.ui.KriptoDOGEDetay.clicked.connect(lambda: self.kripto_detay_goruntule(0))
        self.ui.KriptoBTCDetay.clicked.connect(lambda: self.kripto_detay_goruntule(1))
        self.ui.KriptoHOTDetay.clicked.connect(lambda: self.kripto_detay_goruntule(2))
        self.ui.KriptoXRPDetay.clicked.connect(lambda: self.kripto_detay_goruntule(3))
        self.ui.KriptoAVAXDetay.clicked.connect(lambda: self.kripto_detay_goruntule(4))
        self.ui.KriptoCHZDetay.clicked.connect(lambda: self.kripto_detay_goruntule(5))
        self.ui.KriptoETHDetay.clicked.connect(lambda: self.kripto_detay_goruntule(6))
        self.ui.KriptoXLMDetay.clicked.connect(lambda: self.kripto_detay_goruntule(7))
        self.ui.kriptoAlButon.clicked.connect(lambda: self.kripto_al())
        self.ui.kriptoSatButon.clicked.connect(lambda: self.kripto_sat())
        self.ui.kriptoAlMax.clicked.connect(lambda: self.ui.kriptoAlMiktar.setText(str(self._bakiye)))
        self.ui.kriptoSatMax.clicked.connect(lambda: self.ui.kriptoSatMiktar.setText(str(self._cuzdancoin[self._secilencoin])))
        self.ui.ParaCekMaxButon.clicked.connect(lambda: self.ui.MiktarParaCek.setText(str(self._bakiye)))
        self.ui.SifreGuncelle.clicked.connect(lambda: self.sifre_degis())
        self.ui.KaydetButon.clicked.connect(lambda: self.hesap_bilgi_degis())
        self.ui.ParaYatirButon.clicked.connect(lambda: self.para_atma())
        self.ui.ParaCekButon.clicked.connect(lambda: self.para_cekme())

        # Pasta grafiği yapısı
        self.figure_pasta = Figure()
        self.figure_pasta.patch.set_facecolor('#3c63a1')
        self.figure_pasta.subplots_adjust(0.15, 0.05, 0.85, 0.95)
        self.figure_pasta.tight_layout()
        self.canvas_pasta = FigureCanvas(self.figure_pasta)
        duzen_pasta = QVBoxLayout()
        duzen_pasta.addWidget(self.canvas_pasta)
        self.ui.cuzdanPastaGrafik.setLayout(duzen_pasta)

        # Cüzdan grafiği yapısı
        self.figure_cuzdan = Figure()
        self.figure_cuzdan.patch.set_facecolor('#3c63a1')
        self.figure_cuzdan.subplots_adjust(0.2, 0.1, 0.87, 0.9)
        self.figure_cuzdan.tight_layout()
        self.canvas_cuzdan = FigureCanvas(self.figure_cuzdan)
        layout_cuzdan = QVBoxLayout()
        layout_cuzdan.addWidget(self.canvas_cuzdan)
        self.ui.cuzdanDegerGrafik.setLayout(layout_cuzdan)

        # Kripto detay grafiği yapısı
        self.figure_detay = Figure()
        self.figure_detay.patch.set_facecolor('#3c63a1')
        self.figure_detay.subplots_adjust(0.2, 0.1, 0.9, 0.9)
        self.figure_detay.tight_layout()
        self.canvas_detay = FigureCanvas(self.figure_detay)
        layout_detay = QVBoxLayout()
        layout_detay.addWidget(self.canvas_detay)
        self.ui.kriptoDetayGrafik.setLayout(layout_detay)
        self.t = threading.Thread(target=self.calis)
        self.t.daemon = True
        self.t.start()
        self.show()

    def arayuz_ayarlar(self):
        if self._id != 0:  # Giriş yapılmış ise çalışacak
            if self._anlik_ekran == 0:  # Cüzdanın bilgileri güncelleniyor
                self.ui.SayfaWidget.setCurrentWidget(self.ui.cuzdanWidget)
                self.pasta_plot_fonk()
                self.cuzdan_plot_fonk()
                kriptodeger = numpy.empty(8, dtype=float)
                oncekideger = self._cuzdandeger
                self._cuzdandeger = 0
                for i in range(8):
                    kriptodeger[i] = self._cuzdancoin[i] * float(self._kripto_fiyat[i][0])  # Kripto paraların Veri tabanı fiyatları güncelleniyor
                    self._cuzdandeger += kriptodeger[i]  # Cüzdanın toplam değeri hesaplanıyor
                self.ui.toplamPara.setText(f'{self._cuzdandeger:,.2f} TL')
                if self._sayac != 0:
                    oncekideger = self._cuzdandeger - oncekideger  # Kar zarar hesabı yapılıyor
                self.ui.toplamParaDegisim.setText(f'{oncekideger:,.2f} TL' if oncekideger <= 0 else f'+{oncekideger:,.2f} TL')
                self._sayac += 1
                for i in range(8):
                    obj = eval('self.ui.Adet' + kripto_bilgi(i)[0])  # Kripto paranın Veri tabanı adeti yazılıyor arayüze
                    obj.setText(f'{self._cuzdancoin[i]:,.2f} ' + kripto_bilgi(i)[0])
                    obj2 = eval('self.ui.TL' + kripto_bilgi(i)[0])  # Kripto paranın Veri tabanı adetine göre değeri yazılıyor
                    obj2.setText(f'{kriptodeger[i]:,.2f} TL')
            elif self._anlik_ekran == 2:  # Piyasa ekranının güncellenmesi
                self.ui.SayfaWidget.setCurrentWidget(self.ui.piyasaWidget)
                for i in range(8):  # Her kripto paranın değerleri yazdırılıyor (döngüde)
                    obj = eval('self.ui.Deger' + kripto_bilgi(i)[0])
                    obj.setText(f'{self._kripto_fiyat[i][0]:,.2f}' + ' TL')  # Kripto paranın değeri yazılıyor
                    obj2 = eval('self.ui.Artis' + kripto_bilgi(i)[0])
                    obj2.setText(f'{self._kripto_fiyat[i][1]:,.2f}' + ' TL')  # Kripto paranın değişimi yazılıyor
                    obj3 = eval('self.ui.Artis' + kripto_bilgi(i)[0] + 'Yuzde')
                    obj3.setText(f'{self._kripto_fiyat[i][2]:,.2f}' + '%')  # Kripto paranın değişimi (Yüzde) yazılıyor
            elif self._anlik_ekran == 4:  # Kripto alım-satım'da kripto paranın değeri yazdırılıyor
                self.ui.kriptoSatAlDeger.setText(f'1 {kripto_bilgi(self._secilencoin)[0]} = {self._kripto_fiyat[self._secilencoin][0]:,.2f} TL')
            elif self._anlik_ekran == 5:  # Detay ekranında kripto paranın verilerin güncellenmesi
                self.ui.kriptoDetayAnlik.setText(f'Anlık Değer: {self._kripto_fiyat[self._secilencoin][0]:,.2f} TL')
                self.ui.kriptoDetayDegisim.setText(f'Değişim: {self._kripto_fiyat[self._secilencoin][1]:,.2f} TL ({self._kripto_fiyat[self._secilencoin][2]:,.2f}%)')
                self.ui.kriptoDetayAcilis.setText(f'Açılış Fiyatı: {self._kripto_fiyat[self._secilencoin][7]:,.2f} TL')
                self.ui.kriptoDetayMax.setText(f'En Yüksek: {self._kripto_fiyat[self._secilencoin][4]:,.2f} TL')
                self.ui.kriptoDetayMin.setText(f'En Düşük: {self._kripto_fiyat[self._secilencoin][5]:,.2f} TL')
                self.ui.kriptoDetayHacim.setText(f'24s Hacim: {self._kripto_fiyat[self._secilencoin][6]:,.2f} TL')
                self.detay_plot_fonk(self._secilencoin)

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def para_cekme(self):
        kredikart = self.ui.KKNoCekme1.text() + self.ui.KKNoCekme2.text() + self.ui.KKNoCekme3.text() + self.ui.KKNoCekme4.text()
        cvc = self.ui.CVCCekme.text()
        if self.ui.MiktarParaCek.text() != "" and kredikart != "" and cvc != "":
            if (re.match('^\d*[.,]?\d*$', self.ui.MiktarParaCek.text(), re.IGNORECASE)) and (re.match('^[0-9]+$', kredikart, re.IGNORECASE)) and (re.match('^[0-9]+$', cvc, re.IGNORECASE)):
                miktar = Decimal(self.ui.MiktarParaCek.text().replace(',', '.'))
                if miktar > 0:
                    if miktar <= self._bakiye:
                        if re.search(r'^[0-9]{16}$', kredikart) and re.search(r'^[0-9]{3}$', cvc):
                            self._bakiye -= miktar
                            self.vt.kullanici_bakiye = str(self._bakiye)
                            self._bakiye = self.vt.kullanici_bakiye
                            self.bakiye_islem()
                            self.bakiye_goruntule(0)
                            self.ui.BakiyeIslemText.setText('Para hesabınızdan çekildi!')
                        else:
                            self.ui.BakiyeIslemText.setText('Kredi Kartı bilgileri hatalı!')
                    else:
                        self.ui.BakiyeIslemText.setText('Bakiyeden fazla para çekemezsiniz!')
                else:
                    self.ui.BakiyeIslemText.setText('Miktar sıfır\'dan büyük olmalı!')
            else:
                self.ui.BakiyeIslemText.setText('Bilgiler hatalı!')
        else:
            self.ui.BakiyeIslemText.setText('Boş bırakmayınız!')

    def para_atma(self):
        kredikart = self.ui.KKNoAtma1.text() + self.ui.KKNoAtma2.text() + self.ui.KKNoAtma3.text() + self.ui.KKNoAtma4.text()
        cvc = self.ui.CVCAtma.text()
        if self.ui.MiktarParaAt.text() != "" and kredikart != "" and cvc != "":
            if (re.match('^\d*[.,]?\d*$', self.ui.MiktarParaAt.text(), re.IGNORECASE)) and (re.match('^[0-9]+$', kredikart, re.IGNORECASE)) and (re.match('^[0-9]+$', cvc, re.IGNORECASE)):
                miktar = Decimal(self.ui.MiktarParaAt.text().replace(',', '.'))
                if miktar > 0:
                    if re.search(r'^[0-9]{16}$', kredikart) and re.search(r'^[0-9]{3}$', cvc):
                        miktar += self._bakiye
                        self.vt.kullanici_bakiye = str(miktar)
                        self._bakiye = self.vt.kullanici_bakiye
                        self.bakiye_islem()
                        self.bakiye_goruntule(0)
                        self.ui.BakiyeIslemText.setText('Para hesabınıza yatırıldı!')
                    else:
                        self.ui.BakiyeIslemText.setText('Kredi Kartı bilgileri hatalı!')
                else:
                    self.ui.BakiyeIslemText.setText('Miktar sıfır\'dan büyük olmalı!')
            else:
                self.ui.BakiyeIslemText.setText('Bilgiler hatalı!')
        else:
            self.ui.BakiyeIslemText.setText('Boş bırakmayınız!')

    def hesap_silme(self):
        onay = QMessageBox
        secim = onay.question(self, 'Hesap Silme', "Hesabınızı silmek istediğinizden emin misiniz?", onay.Yes | onay.No)
        if secim == onay.Yes:
            vt = VeriTabaniIslem('hesaplar')
            vt.sil('id=' + str(self._id))
            vt = VeriTabaniIslem('cuzdan')
            vt.sil('id=' + str(self._id))
            self.cikis_yap()

    def hesap_bilgi_degis(self):
        if self.ui.IsimText.text() != "" and self.ui.SoyisimText.text() != "" and self.ui.MailText.text() != "":
            isim = self.ui.IsimText.text()
            soyisim = self.ui.SoyisimText.text()
            eposta = self.ui.MailText.text()
            if ((re.match('^[A-ZÇŞĞİÜÖa-zçşğıüö]+$', isim, re.IGNORECASE)) or (re.match('^[A-ZÇŞĞİÜÖa-zçşğıüö\sA-ZÇŞĞIÜÖa-zçşğıüö]+$', isim, re.IGNORECASE))) and (re.match('^[A-ZÇŞĞİÜÖa-zçşğıüö]+$', soyisim, re.IGNORECASE)):
                if re.search(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', eposta):
                    if eposta_kontrol(self._id, eposta) == -2:  # -2 = Eposta mevcut değil (geçerli) | -1 = Eposta mevcut (geçersiz)
                        isim = re.sub(r'\s+', ' ', isim)  # 2. isim eklenirse aradaki boşluk sayısını bir yapar
                        self.vt.kullanici_eposta = str(eposta)  # Setterlara gönderiliyor (Veri tabanında güncellemek için)
                        self.vt.kullanici_isim = str(isim.upper())
                        self.vt.kullanici_soyisim = str(soyisim.upper())
                        self._eposta = self.vt.kullanici_eposta
                        self._isim = self.vt.kullanici_isim
                        self._soyisim = self.vt.kullanici_soyisim
                        self.ui.AyarlarIslemText.setText('Güncelleme başarılı!')
                        self.ayarlar_goruntule(0)
                    else:
                        self.ui.AyarlarIslemText.setText('Eposta mevcut!')
                else:
                    self.ui.AyarlarIslemText.setText('Mail hatalı!')
            else:
                self.ui.AyarlarIslemText.setText('İsim hatalı!')
        else:
            self.ui.AyarlarIslemText.setText('Boş bırakmayınız!')

    def sifre_degis(self):
        if self.ui.SifreEski.text() != "" and self.ui.SifreText.text() != "" and self.ui.SifreTekrar.text() != "":
            sifrekontrol = self.ui.SifreEski.text()
            yenisifre = self.ui.SifreText.text()
            yenisifretekrar = self.ui.SifreTekrar.text()
            if sifrekontrol == self._sifre:
                if yenisifre == yenisifretekrar:
                    self.vt.kullanici_sifre = str(yenisifre)  # Şifre setter
                    self._sifre = self.vt.kullanici_sifre
                    self.ui.AyarlarIslemText.setText("Güncelleme başarılı!")
                    self.ayarlar_goruntule(0)
                else:
                    self.ui.AyarlarIslemText.setText('Yeni şifre yanlış girildi!')
            else:
                self.ui.AyarlarIslemText.setText('Eski şifre yanlış girildi!')
        else:
            self.ui.AyarlarIslemText.setText('Boş bırakmayınız!')

    def kripto_al_sat_goruntule(self, kripto_id, islem):
        self._anlik_ekran = 4
        self._secilencoin = kripto_id
        if islem == 1:
            self.ui.kriptoSatAlIslem.setText('')
        self.ui.kriptoSatAlAdi.setText(f'{kripto_bilgi(kripto_id)[1]} ({kripto_bilgi(kripto_id)[0]})')
        konum = u":/simge/simge/{COIN}.png".replace('{COIN}', kripto_bilgi(kripto_id)[0])
        self.ui.kriptoSatAlLogo.setPixmap(QPixmap(konum))
        self.ui.kriptoSatAlCuzdan.setText(f'Cüzdan: {self._cuzdancoin[kripto_id]:,.2f} Adet {kripto_bilgi(kripto_id)[0]}')
        self.ui.SayfaWidget.setCurrentWidget(self.ui.kriptoSatAlWidget)
        self.ui.kriptoAlMiktar.setText('')
        self.ui.kriptoAlSifre.setText('')
        self.ui.kriptoSatMiktar.setText('')
        self.ui.kriptoSatSifre.setText('')
        self.arayuz_ayarlar()

    def kripto_al(self):
        if self.ui.kriptoAlMiktar.text() != "" and self.ui.kriptoAlSifre.text() != "":
            if re.match('^\d*[.,]?\d*$', self.ui.kriptoAlMiktar.text(), re.IGNORECASE):
                miktar = Decimal(self.ui.kriptoAlMiktar.text().replace(',', '.'))
                sifre_kontrol = self.ui.kriptoAlSifre.text()
                if not miktar <= Decimal('0.0'):
                    if sifre_kontrol == self._sifre:
                        if miktar <= self._bakiye:
                            self._bakiye -= miktar
                            self.vt.kullanici_bakiye = str(self._bakiye)  # bakiye setter (veri tabanı güncelleme kısmı)
                            self._bakiye = self.vt.kullanici_bakiye
                            miktar /= Decimal(self._kripto_fiyat[self._secilencoin][0])
                            miktar = round(miktar, 3)
                            sorgu = str(kripto_bilgi(self._secilencoin)[0]) + '=' + str(kripto_bilgi(self._secilencoin)[0]) + '+' + str(miktar)
                            # mevcut kripto adeti + aldığımız adet
                            self.vt.kullanici_kripto = sorgu  # cüzdan kripto setter (veri tabanı güncelleme kısmı)
                            self._cuzdancoin = self.vt.kullanici_kripto
                            self.bakiye_islem()
                            self.ui.kriptoSatAlIslem.setText(f'{miktar:,.2f} adet {kripto_bilgi(self._secilencoin)[0]} satın alındı!')
                            self.kripto_al_sat_goruntule(self._secilencoin, 0)
                        else:
                            self.ui.kriptoSatAlIslem.setText('Miktar bakiyeyi geçemez!')
                    else:
                        self.ui.kriptoSatAlIslem.setText('Şifre yanlış!')
                else:
                    self.ui.kriptoSatAlIslem.setText('Miktar sıfır\'dan büyük olmalı!')
            else:
                self.ui.kriptoSatAlIslem.setText('Hatalı miktar girişi!')
        else:
            self.ui.kriptoSatAlIslem.setText('Boş bırakmayınız!')

    def kripto_sat(self):
        if self.ui.kriptoSatMiktar.text() != "" and self.ui.kriptoSatSifre.text() != "":
            if re.match('^\d*[.,]?\d*$', self.ui.kriptoSatMiktar.text(), re.IGNORECASE):
                miktar = Decimal(self.ui.kriptoSatMiktar.text().replace(',', '.'))
                sifre_kontrol = self.ui.kriptoSatSifre.text()
                if not miktar <= Decimal('0.0'):
                    if sifre_kontrol == self._sifre:
                        if miktar <= round(Decimal(self._cuzdancoin[self._secilencoin]), 3):
                            self._bakiye += miktar * Decimal(self._kripto_fiyat[self._secilencoin][0])
                            self.vt.kullanici_bakiye = str(self._bakiye)
                            self._bakiye = self.vt.kullanici_bakiye # bakiye setter
                            eklenen = miktar * Decimal(self._kripto_fiyat[self._secilencoin][0])
                            miktar = round(miktar, 3)
                            sorgu = str(kripto_bilgi(self._secilencoin)[0]) + '=' + str(kripto_bilgi(self._secilencoin)[0]) + '-' + str(miktar)
                            # mevcut kripto adeti - sattığımız adet
                            self.vt.kullanici_kripto = sorgu # cüzdan kripto setter (veri tabanı güncelleme kısmı)
                            self._cuzdancoin = self.vt.kullanici_kripto
                            self.bakiye_islem()
                            self.ui.kriptoSatAlIslem.setText(f'{miktar:,.2f} adet {kripto_bilgi(self._secilencoin)[0]} satıldı. Bakiye\'ye {eklenen:,.2f} TL eklendi!')
                            self.kripto_al_sat_goruntule(self._secilencoin, 0)
                        else:
                            self.ui.kriptoSatAlIslem.setText('Miktar adeti geçemez!')
                    else:
                        self.ui.kriptoSatAlIslem.setText('Şifre yanlış!')
                else:
                    self.ui.kriptoSatAlIslem.setText('Miktar sıfır\'dan büyük olmalı!')
            else:
                self.ui.kriptoSatAlIslem.setText('Hatalı miktar girişi!')
        else:
            self.ui.kriptoSatAlIslem.setText('Boş bırakmayınız!')

    def bakiye_goruntule(self, islem):
        self.bakiye_islem()
        if islem == 1:
            self.ui.BakiyeIslemText.setText('')
        self._anlik_ekran = 1
        self.ui.SayfaWidget.setCurrentWidget(self.ui.bakiyeWidget)

    def bakiye_islem(self):
        self.ui.kullaniciBakiye.setText(f'Bakiye: {self._bakiye:,.2f} TL')
        self.ui.MiktarParaAt.setText('')
        self.ui.KKNoAtma1.setText('')
        self.ui.KKNoAtma2.setText('')
        self.ui.KKNoAtma3.setText('')
        self.ui.KKNoAtma4.setText('')
        self.ui.CVCAtma.setText('')
        self.ui.MiktarParaCek.setText('')
        self.ui.KKNoCekme1.setText('')
        self.ui.KKNoCekme2.setText('')
        self.ui.KKNoCekme3.setText('')
        self.ui.KKNoCekme4.setText('')
        self.ui.CVCCekme.setText('')

    def kripto_detay_goruntule(self, kripto_id):
        self._anlik_ekran = 5
        self._secilencoin = kripto_id
        self.ui.SayfaWidget.setCurrentWidget(self.ui.kriptoDetayWidget)
        self.ui.kriptoDetayText.setText(f'{kripto_bilgi(kripto_id)[1]} ({kripto_bilgi(kripto_id)[0]})')
        konum = u":/simge/simge/{COIN}.png".replace('{COIN}', kripto_bilgi(kripto_id)[0])
        self.ui.kriptoDetayLogo.setPixmap(QPixmap(konum))
        self.arayuz_ayarlar()

    def detay_plot_fonk(self, kripto_id):  # Detay grafiğin içeriği
        self.figure_detay.clear()
        ax_detay = self.figure_detay.add_subplot(111)
        y_ekseni = ['Açılış', 'Düşük', 'Yüksek', 'Anlık']
        x_ekseni = [self._kripto_fiyat[kripto_id][7], self._kripto_fiyat[kripto_id][5], self._kripto_fiyat[kripto_id][4], self._kripto_fiyat[kripto_id][0]]
        ax_detay.plot(y_ekseni, x_ekseni, '.-.', color='white')
        ax_detay.tick_params(colors='white')
        ax_detay.set_facecolor('#55AAFF')
        for x, y in zip(y_ekseni, x_ekseni):
            ax_detay.annotate(y, xy=(x, y), textcoords='offset points', xytext=(0, 10), va='top', ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
        self.canvas_detay.draw()

    def pasta_plot_fonk(self):  # Pasta grafiğin içeriği
        self.figure_pasta.clear()
        veri = []
        veriisim = []
        verirenkler = []
        for i in range(8):
            if self._cuzdancoin[i] != 0:
                veri.append(self._cuzdancoin[i] * float(self._kripto_fiyat[i][0]))
                verirenkler.append(kripto_bilgi(i)[2])
                veriisim.append(kripto_bilgi(i)[0])
        ax = self.figure_pasta.add_subplot(111)
        ax.clear()
        if veriisim:
            ax.pie(veri, colors=verirenkler, labels=veriisim, startangle=270, wedgeprops=dict(width=0.5), shadow=True, textprops={'size': 8, 'color': 'white'})
        else:
            ax.pie([1], colors=['white'], labels=[""])
        self.canvas_pasta.draw()

    def cuzdan_plot_fonk(self):  # Cüzdan grafiğin içeriği
        self.figure_cuzdan.clear()
        deger_anlik = 0
        deger_max = 0
        deger_min = 0
        deger_acilis = 0
        for i in range(8):
            if self._cuzdancoin[i] != 0:
                deger_anlik += self._cuzdancoin[i] * float(self._kripto_fiyat[i][0])
                deger_max += self._cuzdancoin[i] * float(self._kripto_fiyat[i][4])
                deger_min += self._cuzdancoin[i] * float(self._kripto_fiyat[i][5])
                deger_acilis += self._cuzdancoin[i] * float(self._kripto_fiyat[i][7])
        ax_cuzdan = self.figure_cuzdan.add_subplot(111)
        y_ekseni = ['Açılış', 'Düşük', 'Yüksek', 'Anlık']
        x_ekseni = [round(deger_acilis, 2), round(deger_min, 2), round(deger_max, 2), round(deger_anlik, 2)]
        ax_cuzdan.plot(y_ekseni, x_ekseni, '.-.', color='white')
        ax_cuzdan.tick_params(colors='white')
        ax_cuzdan.set_facecolor("#55AAFF")
        for x, y in zip(y_ekseni, x_ekseni):
            ax_cuzdan.annotate(y, xy=(x, y), textcoords="offset points", xytext=(0, 10), va='top', ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
        self.canvas_cuzdan.draw()

    def cuzdan_goruntule(self):
        self._anlik_ekran = 0
        self.arayuz_ayarlar()

    def piyasa_goster(self):
        self._anlik_ekran = 2
        self.arayuz_ayarlar()

    def ayarlar_goruntule(self, islem):
        self._anlik_ekran = 3

        self.ui.IsimText.setText(self._isim)
        self.ui.SoyisimText.setText(self._soyisim)
        self.ui.MailText.setText(self._eposta)
        self.ui.SifreEski.setText("")
        self.ui.SifreText.setText("")
        self.ui.SifreTekrar.setText("")
        if islem == 1:
            self.ui.AyarlarIslemText.setText("")
        self.ui.SayfaWidget.setCurrentWidget(self.ui.ayarlarWidget)

    def calis(self):
        while True and self._id != 0:
            self.arayuz_ayarlar()
            self._kripto_fiyat = kripto_fiyat()
            time.sleep(10)

    def cikis_yap(self):
        self._id = 0
        self.close()
        self.main = GirisKayitEkran()
        self.main.show()


class GirisKayitEkran(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.ui = Ui_GirisKayitEkran()
        self.ui.setupUi(self)
        self.setWindowTitle('Kriptogram')
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(45, 75, 121))
        self.ui.AnaFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.ui.GirisButon.clicked.connect(lambda: self.giris_yap())
        self.ui.KayitOlButon.clicked.connect(lambda: self.kayit_ol())
        self.ui.GirisEkranButon.clicked.connect(lambda: self.giris_yap_goster())
        self.ui.KayitEkranButon.clicked.connect(lambda: self.kayit_ol_goster())
        self.ui.asagiButton.clicked.connect(lambda: self.showMinimized())
        self.ui.kapatButon.clicked.connect(lambda: self.close())
        self.ui.ProgAdiFrame.mouseMoveEvent = self.moveWindow
        self._id = 0
        self._eposta = ""
        self._sifre = ""
        self._sayac = 0
        self.show()
        self.dragPos = 0

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def ilerleme(self):
        value = self._sayac
        self.ui.LoadEkrani.setEnabled(True)
        self.ui.YukleniyorYuzdeText.setText('%' + str(int(self._sayac)))
        if value >= 100:
            value = 1.000
        self.load_ekran_deger(value)
        if self._sayac == 52:
            global fiyat
            fiyat = kripto_fiyat()
            if fiyat[0][3] == 'h':
                self.timer.stop()
                self.ui.SayfaWidget.setCurrentWidget(self.ui.GirisEkrani)
                self.ui.GirisErrorLabel.setText('Bağlantı hatası!')
        if self._sayac > 99:
            self.timer.stop()
            self.main = AnaEkran(self._eposta, self._sifre)
            self.main.show()
            self.close()
            self._sayac = 0
        self._sayac += 2

    def load_ekran_deger(self, value):
        guicss = """QFrame{
            border-radius: 140px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(167, 10, 10, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }"""
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.0001)
        stop_2 = str(progress)
        yeniguicss = guicss.replace('{STOP_1}', stop_1).replace('{STOP_2}', stop_2)
        self.ui.progressBarFrameIc.setStyleSheet(yeniguicss)

    def kayit_ol_goster(self):
        self.ui.IsimText.setText('')
        self.ui.SoyisimText.setText('')
        self.ui.MailTextKayit.setText('')
        self.ui.MailSifreKayit.setText('')
        self.ui.MailSifreKayitTekrar.setText('')
        self.ui.KayitErrorLabel.setText('')
        self.ui.SayfaWidget.setCurrentWidget(self.ui.KayitEkrani)

    def giris_yap_goster(self):
        self.ui.MailText.setText('')
        self.ui.SifreText.setText('')
        self.ui.GirisErrorLabel.setText('')
        self.ui.KayitErrorLabel.setText('')
        self.ui.SayfaWidget.setCurrentWidget(self.ui.GirisEkrani)

    def kayit_ol(self):
        isim = self.ui.IsimText.text()
        soyisim = self.ui.SoyisimText.text()
        eposta = self.ui.MailTextKayit.text()
        sifre = self.ui.MailSifreKayit.text()
        sifretekrar = self.ui.MailSifreKayitTekrar.text()
        if isim != "" and soyisim != "" and eposta != "" and sifre != "" and sifretekrar != "":
            if ((re.match('^[A-ZÇŞĞİÜÖa-zçşğıüö]+$', isim, re.IGNORECASE)) or (re.match('^[A-ZÇŞĞİÜÖa-zçşğıüö\sA-ZÇŞĞIÜÖa-zçşğıüö]+$', isim, re.IGNORECASE))) and (re.match('^[A-ZÇŞĞİÜÖa-zçşğıüö]+$', soyisim, re.IGNORECASE)):
                if sifre == sifretekrar:
                    if re.search(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', eposta):
                        isim = re.sub(r'\s+', ' ', isim)
                        vt = HesapOlustur(isim.upper(), soyisim.upper(), eposta, sifre)
                        if vt.eposta_kontrol != 1:
                            vt.hesap_olustur()
                            self.ui.IsimText.setText('')
                            self.ui.SoyisimText.setText('')
                            self.ui.MailTextKayit.setText('')
                            self.ui.MailSifreKayit.setText('')
                            self.ui.MailSifreKayitTekrar.setText('')
                            self.ui.KayitErrorLabel.setText('')
                            self.giris_yap_goster()
                            self.ui.GirisErrorLabel.setText('Kayıt başarılı!')
                        else:
                            self.ui.KayitErrorLabel.setText('Eposta mevcut!')
                    else:
                        self.ui.KayitErrorLabel.setText('Mail hatalı!')
                else:
                    self.ui.KayitErrorLabel.setText('Şifreler uyuşmuyor!')
            else:
                self.ui.KayitErrorLabel.setText('İsim hatalı!')
        else:
            self.ui.KayitErrorLabel.setText('Boş bırakmayınız!')

    def giris_yap(self):
        eposta = self.ui.MailText.text()
        sifre = self.ui.SifreText.text()
        if eposta != "" and sifre != "":
            vt = HesapGiris(eposta, sifre)
            if vt.kullanici_id != -2:
                if vt.kullanici_id != -1:
                    self.ui.GirisErrorLabel.setText('Giriş başarılı!')
                    self._id = vt.kullanici_id
                    self._eposta = vt.kullanici_eposta
                    self._sifre = vt.kullanici_sifre
                    self.ui.SayfaWidget.setCurrentWidget(self.ui.LoadEkrani)
                    self.timer.timeout.connect(self.ilerleme)
                    self.timer.start(20)
                else:
                    self.ui.GirisErrorLabel.setText('Şifre yanlış!')
            else:
                self.ui.GirisErrorLabel.setText('Böyle bir hesap yok!')
        else:
            self.ui.GirisErrorLabel.setText('Boş bırakmayınız!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GirisKayitEkran()
    sys.exit(app.exec_())
