# 🚗📊 Araba Fiyat Tahmini – Multiple Linear Regression & Flask

Bu proje, araç özelliklerine bağlı olarak araç satış fiyatını tahmin eden bir çoklu doğrusal regresyon (Multiple Linear Regression) modeli geliştirilmesini ve bu modelin Flask tabanlı bir web arayüzü üzerinden kullanılmasını amaçlamaktadır.

Bu çalışma, BLG-407 Makine Öğrenmesi dersi kapsamında, derste işlenen lineer regresyon, veri ön işleme ve Backward Elimination konuları temel alınarak geliştirilmiştir.

---

# 👩‍🎓 Geliştirici Bilgileri

Ad: Melek

Soyad: ÇATAL

Okul Numarası: 2212721039

Ders: BLG-407 Makine Öğrenmesi

GitHub Repo:
https://github.com/melekcatal/MLP_Flask

---

# 📑 İçindekiler

- Proje Açıklaması

- Kullanılan Veri Seti

- Kullanılan Teknolojiler

- Veri Ön İşleme

- Özellik Seçimi ve Backward Elimination

- Model Eğitimi ve Değerlendirme

- Flask Web Arayüzü

- Kurulum ve Çalıştırma

- Dosya Yapısı

- Sonuç ve Değerlendirme

---

# 📌 Proje Açıklaması

Bu projede, araçlara ait yıl, kilometre, motor özellikleri ve temel nitelikler kullanılarak araç satış fiyatını tahmin eden bir regresyon modeli geliştirilmiştir.

Model:

- Veri ön işleme adımlarından geçirilmiş

- Kategorik değişkenler sayısallaştırılmış

- Backward Elimination yöntemi ile istatistiksel olarak anlamlı öznitelikler seçilmiştir

Eğitilen model, Flask tabanlı bir web uygulaması ile kullanıcıdan alınan araç bilgilerine göre fiyat tahmini yapmaktadır.

---

# 📊 Kullanılan Veri Seti

- Kaynak: İkinci el araç satış verileri (CSV formatı) (Kaggle)

- Gözlem sayısı: 8000+ araç

- Hedef değişken: selling_price

- Ham özellikler: yıl, kilometre, yakıt türü, motor hacmi, güç, vites, satıcı tipi vb.

Veri setinde yer alan bazı sütunlar (ör. name, torque)
yüksek kategori sayısı veya temizlenme zorluğu nedeniyle modele dahil edilmemiştir.

---

# 🛠️ Kullanılan Teknolojiler

🐍 Python 3
Veri analizi, model geliştirme ve web uygulaması için ana programlama dili

📊 Pandas & NumPy
Veri okuma, temizleme, dönüştürme ve sayısal işlemler

🧠 Scikit-learn
Çoklu doğrusal regresyon modeli, train-test split ve performans metrikleri (R², MAE, MSE)

📈 Statsmodels
OLS tabanlı regresyon ve Backward Elimination yöntemi ile istatistiksel özellik seçimi

🌐 Flask
Eğitilen modelin web tabanlı bir arayüz üzerinden kullanıcıya sunulması

☁️ Google Colab
Model geliştirme, eğitim ve deneylerin yürütülmesi

💾 Pickle
Eğitilen modelin ve öznitelik sırasının dosya olarak kaydedilmesi ve Flask uygulamasında kullanılması

# Neden Bu Teknolojiler?

Seçilen teknolojiler, çoklu doğrusal regresyon problemine uygun,
ders kapsamında işlenen yöntemlerle uyumlu ve
modelin uçtan uca (veri → model → web arayüzü) geliştirilmesini sağlayacak şekilde tercih edilmiştir.

---

# 🧹 Veri Ön İşleme

Projede aşağıdaki veri ön işleme adımları uygulanmıştır:

- Birim içeren string değişkenlerin temizlenmesi

   - "23.4 kmpl" → 23.4

   - "1248 CC" → 1248

- Sayısal dönüşüm sırasında oluşan eksik değerlerin median yöntemi ile doldurulması

- Kategorik değişkenlerin One-Hot Encoding ile sayısallaştırılması

- Dummy trap problemini önlemek için drop_first=True kullanımı

---

# 🧠 Özellik Seçimi – Backward Elimination

Modelde kullanılan öznitelik sayısı maksimum 10 ile sınırlandırılmıştır.

Bu amaçla:

- statsmodels kütüphanesi ile OLS modeli kurulmuş

- p-value > 0.05 olan değişkenler adım adım modelden çıkarılmış

- Tüm değişkenler istatistiksel olarak anlamlı hale gelene kadar işlem sürdürülmüştür

---

🎯 Final Modelde Kullanılan Özellikler

- year

- km_driven

- mileage

- engine

- max_power

- seats

- fuel_Petrol

- transmission_Manual

- seller_type_Individual

- owner_Second Owner

---

# 📈 Model Eğitimi ve Değerlendirme

Final model, Multiple Linear Regression yöntemi ile eğitilmiştir.

Kullanılan metrikler:

- R² (Determinasyon Katsayısı)

- MAE (Mean Absolute Error)

- MSE (Mean Squared Error)

Performans:

- R² ≈ 0.68

Bu sonuç, modelin araç fiyatlarındaki varyansın yaklaşık %68’ini açıkladığını göstermektedir.
Model, genelleme yeteneği açısından yeterli ve istikrarlı bir performans sergilemektedir.

---

# 🌐 Flask Web Arayüzü

Eğitilen model, kullanıcı dostu bir Flask tabanlı web arayüzü ile sunulmuştur.

Arayüz özellikleri:

- Kullanıcıdan araç bilgilerini alma

- Anında fiyat tahmini

- Girilen değerlerin tahmin sonrası korunması

- Arka plan görseli ve modern tasarım

- Responsive (ekrana uyumlu) yapı

Model (model.pkl) ve öznitelik sırası (features.pkl) Flask uygulamasında birebir kullanılmaktadır.

Aşağıda Flask Web Arayüzü'ne ait örnek ekran görüntüleri yer almaktadır.

<img width="1832" height="865" alt="image" src="https://github.com/user-attachments/assets/79300159-b52c-4247-83e3-bff813223731" />

<img width="1820" height="865" alt="image" src="https://github.com/user-attachments/assets/dd26d41d-8f4a-4e73-a120-2ba96efd165d" />

<img width="1817" height="859" alt="image" src="https://github.com/user-attachments/assets/417751cb-a0cd-4c49-86ed-083fe0d7fa70" />

---

# ⚙️ Kurulum ve Çalıştırma

Gerekli kütüphaneler
```bash
pip install flask numpy pandas scikit-learn statsmodels
```

Flask uygulamasını çalıştırmak için
```bash
python app.py
```

Tarayıcıdan:
```bash
http://127.0.0.1:5000
```
adresine gidilerek uygulama kullanılabilir.

---

# 📁 Dosya Yapısı
```bash
MLP_Flask/
│
├── Proje3.ipynb
├── app.py
├── model.pkl
├── features.pkl
├── README.md
│
├── data/
│   └── cars.csv
│
└── templates/
    └── index.html
```

---

# 🧾 Sonuç ve Değerlendirme

Bu proje kapsamında:

- Veri ön işleme

- İstatistiksel özellik seçimi

- Çoklu doğrusal regresyon modelleme

- Model değerlendirme

- Flask ile web arayüz geliştirme

adımları uçtan uca gerçekleştirilmiştir.

Çalışma, hem makine öğrenmesi hem de basit web uygulaması geliştirme açısından bütüncül bir örnek sunmaktadır. ✅

---

# 📌 Not

Bu proje, BLG-407 Makine Öğrenmesi dersi kapsamında hazırlanmıştır.
