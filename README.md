# YZM212 - Makine Öğrenmesi: Laboratuvar Ödevi 2

**Konu:** MLE ile Akıllı Şehir Planlaması  
**Öğrenci:** Muhammad Ali Gadirli (24290767)

---

## 1. Problem Tanımı
Bu çalışmanın amacı, bir şehir caddesindeki trafik yoğunluğunu modellemek için Poisson dağılımını kullanmaktırVerilen trafik verileri üzerinden En Çok Olabilirlik (Maximum Likelihood Estimation - MLE) yöntemiyle trafik yoğunluğu parametresi ($\lambda$) tahmin edilmiş ve bu parametrenin şehir planlama kararlarına etkileri analiz edilmiştir[cite: 103, 144].

## 2. Kullanılan Veri ve Yöntem
* **Veri:** 1 dakikalık zaman dilimlerinde caddeden geçen araç sayıları[cite: 102].
* **Yöntem:**
    * Poisson dağılımı için olabilirlik fonksiyonunun logaritması alınarak analitik türetme yapılmıştır.
    * Negatif Log-Olabilirlik (NLL) fonksiyonu `scipy.optimize` kütüphanesi kullanılarak sayısal olarak minimize edilmiştir.
    * Analitik sonuçlar ile sayısal sonuçlar karşılaştırılmıştır.

## 3. Sonuçlar
* **Analitik Tahmin ($\lambda$):** 12.14 
* **Sayısal Tahmin ($\lambda$):** 12.14 
* **Görselleştirme:** Elde edilen $\lambda$ değeri ile oluşturulan Poisson dağılımı (PMF) ve gerçek verilerin histogramı karşılaştırılmış, modelin verilere uyumu değerlendirilmiştir.

## 4. Tartışma ve Aykırı Değer (Outlier) Analizi
* Veri setine 200 gibi uç bir değer eklendiğinde, ortalama tabanlı MLE tahmincisi belirgin şekilde sapmaktadır.
* Bu durum, ham verinin doğrudan kullanılmasının hatalı şehir planlama yatırımlarına yol açabileceğini göstermektedir.
* **Öneri:** Gerçek dünya uygulamalarında veri ön işleme (aykırı değer tespiti ve temizliği) kritik öneme sahiptir.

---