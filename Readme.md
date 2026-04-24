# 📊 Dashboard Analisis Penyewaan Sepeda

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan Bike Sharing Dataset. Analisis difokuskan pada pengaruh kondisi cuaca serta tren penyewaan sepeda per bulan selama periode 2011–2012.

---

## ❓ Pertanyaan Bisnis

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda pada tahun 2011–2012?
2. Bagaimana tren penyewaan sepeda per bulan selama periode 2011–2012?

---

## 📂 Struktur Folder

```
submission/
│
├── dashboard/
│   ├── dashboard.py
│   └── day.csv
│
├── data/
│   └── day.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## ⚙️ Setup Environment

Pastikan Python sudah terinstall di komputer.

(Opsional) Membuat virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install library yang dibutuhkan:

```
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Dashboard

Masuk ke folder dashboard:

```
cd dashboard
```

Jalankan aplikasi Streamlit:

```
streamlit run dashboard.py
```

Buka browser dan akses:

```
http://localhost:8501
```

---

## 📊 Fitur Dashboard

* Visualisasi pengaruh kondisi cuaca terhadap penyewaan sepeda
* Visualisasi tren penyewaan sepeda per bulan
* Filter interaktif berdasarkan kondisi cuaca

---

## 📈 Insight Utama

* Penyewaan sepeda tertinggi terjadi pada kondisi cuaca cerah
* Penyewaan menurun pada kondisi berawan dan turun drastis saat hujan
* Terdapat pola fluktuatif dalam penyewaan sepeda setiap bulan
* Pola tersebut menunjukkan adanya kecenderungan musiman dalam penggunaan sepeda


## 📌 Dataset

Dataset yang digunakan adalah Bike Sharing Dataset (day.csv) yang berisi data harian penyewaan sepeda.
