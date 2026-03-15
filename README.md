# YZM212 - Makine Öğrenmesi: Laboratuvar Ödevi 2

**Konu:** MLE ile Akıllı Şehir Planlaması  
**Öğrenci:** Muhammad Ali Gadirli (24290767)

---

## 1. Problem Tanımı
[cite_start]Bu çalışmanın amacı, bir şehir caddesindeki trafik yoğunluğunu modellemek için Poisson dağılımını kullanmaktır[cite: 103]. [cite_start]Verilen trafik verileri üzerinden En Çok Olabilirlik (Maximum Likelihood Estimation - MLE) yöntemiyle trafik yoğunluğu parametresi ($\lambda$) tahmin edilmiş ve bu parametrenin şehir planlama kararlarına etkileri analiz edilmiştir[cite: 103, 144].

## 2. Kullanılan Veri ve Yöntem
* [cite_start]**Veri:** 1 dakikalık zaman dilimlerinde caddeden geçen araç sayıları[cite: 102].
* **Yöntem:**
    * [cite_start]Poisson dağılımı için olabilirlik fonksiyonunun logaritması alınarak analitik türetme yapılmıştır[cite: 109, 110].
    * [cite_start]Negatif Log-Olabilirlik (NLL) fonksiyonu `scipy.optimize` kütüphanesi kullanılarak sayısal olarak minimize edilmiştir[cite: 113, 117].
    * [cite_start]Analitik sonuçlar ile sayısal sonuçlar karşılaştırılmıştır[cite: 137].

## 3. Sonuçlar
* [cite_start]**Analitik Tahmin ($\lambda$):** 12.14 [cite: 62, 63]
* [cite_start]**Sayısal Tahmin ($\lambda$):** 12.14 [cite: 62, 63]
* [cite_start]**Görselleştirme:** Elde edilen $\lambda$ değeri ile oluşturulan Poisson dağılımı (PMF) ve gerçek verilerin histogramı karşılaştırılmış, modelin verilere uyumu değerlendirilmiştir[cite: 139, 140].

## 4. Tartışma ve Aykırı Değer (Outlier) Analizi
* [cite_start]Veri setine 200 gibi uç bir değer eklendiğinde, ortalama tabanlı MLE tahmincisi belirgin şekilde sapmaktadır[cite: 77, 78, 83].
* [cite_start]Bu durum, ham verinin doğrudan kullanılmasının hatalı şehir planlama yatırımlarına yol açabileceğini göstermektedir[cite: 144].
* [cite_start]**Öneri:** Gerçek dünya uygulamalarında veri ön işleme (aykırı değer tespiti ve temizliği) kritik öneme sahiptir[cite: 88, 144].

---