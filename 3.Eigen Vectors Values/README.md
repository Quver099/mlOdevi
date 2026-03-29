# Eigenvalues and Eigenvectors Analysis (YZM212 - ML Lab 3)

## 📌 Proje Açıklaması

Bu projede, karesel bir matrisin **özdeğerleri (eigenvalues)** ve **özvektörleri (eigenvectors)** hem NumPy kütüphanesi kullanılarak hem de manuel yöntemlerle hesaplanmıştır. Elde edilen sonuçlar karşılaştırılarak doğruluk analizi yapılmıştır.

---

## 🧠 Teorik Arka Plan

### 🔹 Özdeğer ve Özvektör Nedir?

Bir A matrisi için:

A * v = λ * v

* **λ (lambda)** → özdeğer
* **v** → özvektör

Bu ifade, v vektörünün A dönüşümü altında sadece ölçeklendiğini gösterir.

---

### 🔹 Karakteristik Denklem

Özdeğerleri bulmak için:

det(A - λI) = 0

2x2 matris için bu denklem şu hale gelir:

λ² - (trace(A))λ + det(A) = 0

* **trace(A)** = köşegen elemanların toplamı
* **det(A)** = determinant

---

## ⚙️ Kullanılan Yöntemler

### 1. NumPy ile Hesaplama

NumPy kütüphanesinin `linalg.eig` fonksiyonu kullanılarak:

* Özdeğerler
* Özvektörler

hesaplanmıştır.

---

### 2. Manuel Hesaplama

2x2 matrisler için karakteristik denklem kullanılarak özdeğerler bulunmuştur:

* Trace ve determinant hesaplandı
* Diskriminant (Δ) bulundu
* İkinci dereceden denklem çözüldü

---

### 3. Karşılaştırma

* NumPy sonuçları ile manuel sonuçlar karşılaştırıldı
* Fark (hata) hesaplandı

---

## 🧪 Kullanılan Matris

```python
A = [[4, 2],
     [1, 3]]
```

---

## 📊 Sonuçlar

* NumPy ve manuel hesaplamalar aynı sonuçları vermiştir.
* Hesaplanan fark ≈ 0’dır (sayısal yuvarlama hataları dışında).

---

## 📁 Proje Yapısı

```
EigenVectorsValues/
│
├── EigenVectorsValues.ipynb
├── README.md
```

---

## 🚀 Kullanım

Projeyi çalıştırmak için:

```bash
pip install numpy
```

ve ardından Python veya Jupyter Notebook üzerinden çalıştırabilirsiniz.

---

## 📚 Kaynaklar

* NumPy Documentation: https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html
* Machine Learning Mastery (Eigenvalues & Matrices)
* https://github.com/LucasBN/Eigenvalues-and-Eigenvectors

---

## ✅ Sonuç

Bu çalışmada:

* Özdeğer ve özvektör kavramları anlaşılmıştır
* NumPy fonksiyonları incelenmiştir
* Manuel hesaplama ile doğrulama yapılmıştır

Bu tür işlemler, özellikle **PCA (Principal Component Analysis)** gibi makine öğrenmesi algoritmalarında önemli rol oynamaktadır.

---
