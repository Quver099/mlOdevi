## Hesaplamalar

Bu bölümde HMM modeli kullanılarak gözlem dizisinin olasılığı nasıl hesaplandığı gösterilmiştir.

### EV Kelimesi İçin Parametreler

Başlangıç olasılığı:

π = [1.0, 0.0]

Bu değer modelin ilk durumdan başladığını gösterir.

Geçiş matrisi:

A =

[0.6  0.4
0.2  0.8]

Yayılım matrisi:

B =

[0.7  0.3
0.1  0.9]

Burada:

* ilk sütun **e** harfini
* ikinci sütun **v** harfini temsil eder.

---

### Örnek Gözlem Dizisi

Gözlem dizisi şu şekilde alınmıştır:

O = (e, v)

Bu dizinin EV modeli altında olasılığı hesaplanmıştır.

İlk adımda model S1 durumundan başlar ve **e** gözlemi üretilir:

P = 1.0 × 0.7
P = 0.7

İkinci adımda S1 durumundan S2 durumuna geçiş olur ve **v** gözlemi üretilir:

P = 0.7 × 0.4 × 0.9

P ≈ 0.252

Sonuç olarak gözlem dizisinin EV modeli altında olasılığı yaklaşık olarak **0.252** bulunmuştur.

---

### Model Karşılaştırması

Aynı gözlem dizisi OKUL kelimesi için oluşturulan HMM modeli ile de hesaplanabilir.

Daha yüksek olasılık hangi modelde çıkarsa sistem o kelimenin söylendiğini tahmin eder.
