"""
DERS: Yöneylem Arastirmasi
"""

"""
1. Grafik cizimi icin matplotlib kutuphanesi
2. Cizimde cozum alanindaki kose noktalarini siralamak icin scipy kutuphanesinden ConvexHull kullanilmistir.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.spatial import ConvexHull

def cozum_alani_icinde_mi(x, y):
    """
        1. Verilen (x,y) noktasinin kordinat sisteminin 1. bölgesinde olup olmadigini ve
            tum kisitlari saglayip saglamadigini kontrol eder.
        2. 0.0000000001 eklenmesinin sebebi, bilgisayarin ondalik sayilarla calisirken
            kucuk yuvarlama hatalarindan dolayi kisitlari saglayan noktalari disari atmasini engellemektir.
    """
    if x < 0 or y < 0:
        return False
    for x_katsayisi, y_katsayisi, kisit in kisitlar:
        if x_katsayisi*x + y_katsayisi*y > kisit + 0.0000000001:
            return False
    return True

def cozumdeki_kose_noktalari_bul():
    kose_noktalari = []

    """
        1. Orjin noktasi cozum alani icerisindeyse onuda cizime eklemek icin 
            kose_noktalari listesine ekler.
    """
    if cozum_alani_icinde_mi(0, 0):
        kose_noktalari.append((0,0))

    for x_katsayisi, y_katsayisi, kisit in kisitlar:
        """
            1. cozum alani icerisinde y = 0 icin x degerini bulur.
        """
        if x_katsayisi != 0 and cozum_alani_icinde_mi(kisit/x_katsayisi, 0):
            kose_noktalari.append((kisit/x_katsayisi, 0))
        """
            1. cozum alani icerisinde x = 0 icin y degerini bulur.
        """
        if y_katsayisi != 0 and cozum_alani_icinde_mi(0, kisit/y_katsayisi):
            kose_noktalari.append((0, kisit/y_katsayisi))

    """
        1. Cramer metodunu kullanarak iki bilinmeyenli iki denklem sisteminin cozumu bulunur.
            x = 1.sutun_degistirilmis_determinant / determinant
            y = 2.sutun_degistirilmis_determinant / determinant
        2. Bulunan (x,y) cozum alani icerisinde ise kose_noktalari listesine eklenir.
    """
    for i in range(len(kisitlar)):
        for j in range(i+1, len(kisitlar)):
            kisit1_x_katsayi, kisit1_y_katsayi, kisit1 = kisitlar[i]
            kisit2_x_katsayi, kisit2_y_katsayi, kisit2 = kisitlar[j]
            determinant = kisit1_x_katsayi*kisit2_y_katsayi - kisit2_x_katsayi*kisit1_y_katsayi
            """
                NOT: Eger determinant 0 ise paralel veya cakisik dogrular demektir. (cozum yok ya sonsuz cozum var)

                1. Determinant sifirdan farkli ise Cramer metodu uygulanir.
                2. 0.0000000001 eklenme sebebi, determinantin mutlak degeri 0'a cok yakin ise (0.0000000001)
                    bilgisayarin ondalik sayilarla calisirken kucuk yuvarlama hatalarindan dolayi
                    determinantin sifir olarak algilanmasini engellemektir.
            """
            if abs(determinant) > 0 + 0.0000000001:
                x = (kisit1*kisit2_y_katsayi - kisit2*kisit1_y_katsayi) / determinant
                y = (kisit1_x_katsayi*kisit2 - kisit2_x_katsayi*kisit1) / determinant
                if cozum_alani_icinde_mi(x, y):
                    kose_noktalari.append((x, y))
    
    return list(set(kose_noktalari))

def cozum(zx, zy):
    kose_noktalari = cozumdeki_kose_noktalari_bul()
    
    """
        1. Bulunan (x,y) kose noktalarina gore z = zx*x + zy*y degerleri hesaplanir ve listeye eklenir.
        2. Ayrica daha sonra grafigin sinirlarini ayarlamak icin,
            kose noktalarinin x ve y degerleri listelere eklenir.
    """
    z_degerleri = []
    kose_x_noktalari = []
    kose_y_noktalari = []
    for x, y in kose_noktalari:
        z = zx*x + zy*y
        z_degerleri.append(z)
        kose_x_noktalari.append(x)
        kose_y_noktalari.append(y)

    """
        1. Zmax ve Zmin degerleri hesaplanir.
    """
    max_z = max(z_degerleri)
    min_z = min(z_degerleri)
    x_max, y_max = kose_noktalari[z_degerleri.index(max_z)]
    x_min, y_min = kose_noktalari[z_degerleri.index(min_z)]
    
    
    """
        1. Matplotlib kullanilarak 800x600 boyutlarinda bir grafik olusturulur.
    """
    _, ax = plt.subplots(figsize=(8, 6))
    
    """
        1. Cozum alanini duzgun cizmek icin ConvexHull ile kose noktalari siralanir. (Capraz cizmemesi icin)
        2. Kose noktalari kullanilarak cozum alani acik maviye
            cozum alanin sinirlari ise koyu maviye boyanir.
    """
    hull = ConvexHull(kose_noktalari)
    kose_noktalari = [kose_noktalari[i] for i in hull.vertices]
    
    polygon = Polygon(kose_noktalari, facecolor='lightblue', edgecolor='darkblue', linewidth=3)
    ax.add_patch(polygon)
    
    """
        1. Sag ust koseye kisit denklemi,
            kose noktalari ve z degerleri,
            Zmax ve Zmin degerleri yazdirilir.
    """
    corner_text = f'z = {zx}x + {zy}y\n\nKose Noktalari ve z degerleri:\n'
    for x, y in kose_noktalari:
        z = zx*x + zy*y
        corner_text += f"({x:.2f}, {y:.2f}): z={z:.2f}\n"
    corner_text += f"\n\nZmax={max_z:.2f} - ({x_max:.2f}, {y_max:.2f})"
    corner_text += f"\nZmin={min_z:.2f} - ({x_min:.2f}, {y_min:.2f})"
    ax.text(0.98, 0.98, corner_text, transform=ax.transAxes, verticalalignment='top', horizontalalignment='right',)
    
    """
        1. Grafigin sinirlarini en buyuk kose noktasina gore ayarlar.
    """
    oran = max(kose_x_noktalari) / max(kose_y_noktalari)
    if oran > 1:
        ax.set_xlim(0, max(kose_x_noktalari)*1.1)
        ax.set_ylim(0, max(kose_y_noktalari)*1/1.1*oran)
    else:
        ax.set_xlim(0, max(kose_x_noktalari)*1.1/oran)
        ax.set_ylim(0, max(kose_y_noktalari)*1.1)
    plt.show()


if __name__ == "__main__":
    global kisitlar

    """
        1. kisitlar (x_katsayisi, y_katsayisi, kisit) seklinde olusan listedir
            ve x_katsayisi*x + y_katsayisi*y <= kisit seklinde ifade edilir.
        2. Eger buyuk esit (>=) seklinde bir kisit varsa,
            x_katsayisi, y_katsayisi ve kisit (-) ile carpilip
            kucuk esit (<=) seklinde ifade edilebilir.
    """
    kisitlar = [
        (1, 3, 3),   # 1x + 3y <= 3
        (2, 1, 2),   # 2x + 1y <= 2
        (3, 1, 3),   # 3x + 1y <= 3
    ]

    """
        1. Hedef fonksiyonun katsayilari girilir (zx, zy).
            z = zx*x + zy*y seklinde ifade edilir.
    """
    cozum(1, 2) # z = 1x + 2y

"""
NOT: Kod Zmax'in sonsuz veya Zmin'in (-)sonsuz oldugu durumlari hesaplayamiyor.
"""
