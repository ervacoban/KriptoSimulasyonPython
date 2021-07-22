from kutuphaneler import *
baglanti = sqlite3.connect('\\KriptogramVT.db')
cursor = baglanti.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS hesaplar ("
               "id INTEGER PRIMARY KEY, "
               "isim TEXT, soyisim TEXT, "
               "eposta TEXT, sifre TEXT)"
               )
baglanti.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS cuzdan (id INT, "
               "bakiye REAL DEFAULT 0.0, "
               "DOGE REAL DEFAULT 0.0, "
               "BTC REAL DEFAULT 0.0, "
               "HOT REAL DEFAULT 0.0, "
               "XRP REAL DEFAULT 0.0, "
               "AVAX REAL DEFAULT 0.0, "
               "CHZ REAL DEFAULT 0.0, "
               "ETH REAL DEFAULT 0.0, "
               "XLM REAL DEFAULT 0.0)"
               )
baglanti.commit()


class HesapOlustur:
    def __init__(self, isim, soyisim, eposta, sifre):
        self._con = baglanti
        self._cursor = self._con.cursor()
        self._kontrol = 0
        self._isim = isim
        self._soyisim = soyisim
        self._eposta = eposta
        self._sifre = sifre
        self.eposta_kontrol = eposta

    @property
    def eposta_kontrol(self):
        return self._kontrol

    @eposta_kontrol.setter
    def eposta_kontrol(self, eposta):
        kontrol = VeriTabaniIslem('hesaplar')
        kon = kontrol.oku('eposta="' + str(eposta) + '"')
        if len(kon) != 0:
            self._kontrol = 1  # eposta var
        else:
            self._kontrol = -2  # eposta yok

    def hesap_olustur(self):
        self._cursor.execute('INSERT INTO hesaplar(isim, soyisim, eposta, sifre) VALUES(?, ?, ?, ?)', (self._isim,
                                                                                                       self._soyisim,
                                                                                                       self._eposta,
                                                                                                       self._sifre
                                                                                                       ))
        self._con.commit()
        self._cursor.execute('INSERT INTO cuzdan(id) SELECT id FROM hesaplar WHERE eposta = ?', (self._eposta, ))
        self._con.commit()


class HesapGiris:
    def __init__(self, eposta, sifre):
        self._id = 0
        self._eposta = eposta
        self._sifre = sifre
        self._isim = ""
        self._soyisim = ""
        self._con = baglanti
        self._cursor = self._con.cursor()
        self.kullanici_id = eposta

    @property
    def kullanici_id(self):
        return self._id

    @kullanici_id.setter
    def kullanici_id(self, eposta):
        self._cursor.execute('SELECT * FROM hesaplar WHERE eposta = ?', (eposta, ))
        hesaplar = self._cursor.fetchall()
        if len(hesaplar) != 0:
            if hesaplar[0][4] == self._sifre:
                self._id = hesaplar[0][0]
                self.kullanici_isim = hesaplar[0][1]
                self.kullanici_soyisim = hesaplar[0][2]
            else:
                self._id = -1  # -1 = şifre yanlış
        else:
            self._id = -2  # -2 = hesap yok

    @property
    def kullanici_eposta(self):
        return self._eposta

    @kullanici_eposta.setter
    def kullanici_eposta(self, eposta):
        vt = VeriTabaniIslem('hesaplar')
        vt.guncelle('eposta="' + str(eposta) + '"', 'id=' + str(self._id))
        self._eposta = eposta

    @property
    def kullanici_sifre(self):
        return self._sifre

    @kullanici_sifre.setter
    def kullanici_sifre(self, sifre):
        vt = VeriTabaniIslem('hesaplar')
        vt.guncelle('sifre="' + str(sifre) + '"', 'id=' + str(self._id))
        self._sifre = sifre

    @property
    def kullanici_isim(self):
        return self._isim

    @kullanici_isim.setter
    def kullanici_isim(self, isim):
        vt = VeriTabaniIslem('hesaplar')
        vt.guncelle('isim="' + str(isim) + '"', 'id=' + str(self._id))
        self._isim = isim

    @property
    def kullanici_soyisim(self):
        return self._soyisim

    @kullanici_soyisim.setter
    def kullanici_soyisim(self, soyisim):
        vt = VeriTabaniIslem('hesaplar')
        vt.guncelle('soyisim="' + str(soyisim) + '"', 'id=' + str(self._id))
        self._soyisim = soyisim


class CuzdanBilgi(HesapGiris):
    def __init__(self, eposta, sifre):
        super().__init__(eposta, sifre)
        self._id = super().kullanici_id
        self._isim = super().kullanici_isim
        self._soyisim = super().kullanici_soyisim

    @property
    def kullanici_bakiye(self):
        bakiye = VeriTabaniIslem('cuzdan')
        miktar = bakiye.oku('id='+str(self._id))
        if len(miktar) != 0:
            miktar = miktar[0][1]
        else:
            miktar = -2  # Kullanici yok
        miktar = Decimal(miktar)
        return round(miktar, 3)

    @kullanici_bakiye.setter
    def kullanici_bakiye(self, miktar):
        bakiye = VeriTabaniIslem('cuzdan')
        miktar = Decimal(miktar)
        miktar = round(miktar, 3)
        bakiye.guncelle('bakiye='+str(miktar), 'id='+str(self._id))

    @property
    def kullanici_kripto(self):
        coinlar = [0 for i in range(8)]
        kripto = VeriTabaniIslem('cuzdan')
        sahip = kripto.oku('id=' + str(self._id))
        for i in range(8):
            coinlar[i] = round(sahip[0][i+2], 3)
        return coinlar

    @kullanici_kripto.setter
    def kullanici_kripto(self, sorgu):
        vt = VeriTabaniIslem('cuzdan')
        vt.guncelle(sorgu, 'id=' + str(self._id))


class VeriTabaniIslem:
    def __init__(self, tablo):
        self._con = baglanti
        self._cursor = self._con.cursor()
        self._tablo = tablo

    def oku(self, kosul):
        sorgu = f'SELECT * FROM {self._tablo} WHERE {kosul}'
        self._cursor.execute(sorgu)
        kontrol = self._cursor.fetchall()
        return kontrol

    def guncelle(self, sutun, kosul):
        sorgu = f'UPDATE {self._tablo} SET {sutun} WHERE {kosul}'
        self._cursor.execute(sorgu)
        self._con.commit()

    def sil(self, kosul):
        sorgu = f'DELETE FROM {self._tablo} WHERE {kosul}'
        self._cursor.execute(sorgu)
        self._con.commit()


def kripto_bilgi(id):
    coin_liste = [
        ("DOGE", "Dogecoin", '#ba9f33'),
        ("BTC", "Bitcoin", '#ff9416'),
        ("HOT", "Holocoin", '#19a8ae'),
        ("XRP", "Ripple", '#0881b8'),
        ("AVAX", "Avalanche", '#e84142'),
        ("CHZ", "Chiliz", '#cd0124'),
        ("ETH", "Ethereum", '#343434'),
        ("XLM", "Stellar", '#000000')
    ]
    return coin_liste[id]


def kripto_fiyat():
    fiyatlar = [[0 for i in range(8)] for j in range(8)]
    try:
        link = 'https://api.binance.com/api/v1/ticker/24hr?'
        url = requests.get(link)
        data = url.json()
        for i in data:
            for j in range(8):
                if i['symbol'] == (str(kripto_bilgi(j)[0] + 'TRY')):
                    fiyatlar[j][0] = round(float(i["lastPrice"]), 2)
                    fiyatlar[j][1] = round(float(i["priceChange"]), 2)
                    fiyatlar[j][2] = round(float(i["priceChangePercent"]), 2)
                    fiyatlar[j][3] = i['symbol']
                    fiyatlar[j][4] = round(float(i["highPrice"]), 2)
                    fiyatlar[j][5] = round(float(i["lowPrice"]), 2)
                    fiyatlar[j][6] = round(float(i["quoteVolume"]), 2)
                    fiyatlar[j][7] = round(float(i["prevClosePrice"]), 2)
        return fiyatlar
    except requests.exceptions.RequestException:
        for i in range(8):
            fiyatlar[i][0] = 0.0
            fiyatlar[i][1] = 0.0
            fiyatlar[i][2] = 0.0
            fiyatlar[i][3] = 'h'
            fiyatlar[i][4] = 0.0
            fiyatlar[i][5] = 0.0
            fiyatlar[i][6] = 0.0
            fiyatlar[i][7] = 0.0
        return fiyatlar


def eposta_kontrol(id, eposta):
    kontrol = VeriTabaniIslem('hesaplar')
    kon = kontrol.oku('id IS NOT ' + str(id) + ' AND eposta = "' + str(eposta) + '"')
    if len(kon) != 0:
        return 1  # eposta var
    else:
        return -2  # eposta yok
