# HMM Tabanlı İzole Kelime Tanıma

Bu projede Hidden Markov Model (HMM) kullanılarak basit bir izole kelime tanıma sistemi oluşturulmuştur.

Bu çalışmada iki Türkçe kelime modellenmiştir:

* EV
* OKUL

## Amaç

Bu ödevin amacı, izole kelimeleri tanıyabilen basit bir Hidden Markov Model (HMM) sistemi geliştirmektir.

Her kelime için ayrı bir HMM modeli oluşturulmuştur.
Her model şu parametreleri içermektedir:

* Başlangıç olasılıkları (Start Probabilities)
* Geçiş olasılıkları (Transition Probabilities)
* Yayılım olasılıkları (Emission Probabilities)

## HMM Modeli

Her kelime için ayrı bir HMM modeli oluşturulmuştur.

Model şu bileşenlerden oluşmaktadır:

* 2 adet gizli durum (hidden state)
* Geçiş matrisi (transition matrix)
* Yayılım matrisi (emission matrix)

## Gerçekleme (Implementation)

Sistem Python programlama dili kullanılarak geliştirilmiştir ve hesaplamalar için NumPy kütüphanesinden yararlanılmıştır.

İki farklı model oluşturulmuştur:

### EV Modeli

EV kelimesi için:

* Başlangıç olasılıkları tanımlanmıştır
* Geçiş matrisi oluşturulmuştur
* Yayılım matrisi belirlenmiştir

### OKUL Modeli

OKUL kelimesi için:

* Başlangıç olasılıkları tanımlanmıştır
* Geçiş matrisi oluşturulmuştur
* Yayılım matrisi belirlenmiştir

## Programın Çalıştırılması

Programı çalıştırmak için terminalde aşağıdaki komutu yazmanız yeterlidir:

python odev1.py

## Sonuç

Program verilen gözlem dizilerinin olasılığını HMM parametrelerini kullanarak hesaplar ve hangi kelime modelinin gözleme daha uygun olduğunu belirler.

## Yazar

Ad Soyad: Muhammad Ali Gadirli
Ders: makine ogrenmesi
Ödev: HMM Tabanlı Kelime Tanıma
