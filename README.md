# OMNI Personality Profiling using Latent Profile Analysis (LPA)

## Deskripsi Proyek
Repositori ini berisi implementasi kode untuk Tugas Akhir berjudul "Pemetaan Profil Kepribadian Mahasiswa pada Data OMNI Melalui Latent Profile Analysis (LPA) untuk Rekomendasi Intervensi Kesehatan Mental Berbasis Data". 

Proyek ini bertujuan mengembangkan Sistem Pendukung Keputusan (DSS) berbasis *data-driven* yang menerapkan pendekatan *person-centered* untuk memetakan profil kepribadian mahasiswa secara otomatis menggunakan instrumen OMNI Personality Inventory.

## Metodologi
Proyek ini dikembangkan menggunakan kerangka kerja **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*):
1. **Business Understanding**: Memahami kebutuhan pemetaan profil kesehatan mental mahasiswa.
2. **Data Understanding**: Eksplorasi 35 skala kepribadian OMNI dan validasi kualitas respons (VRIN & CD).
3. **Data Preparation**: Data cleaning, item scoring, dan standardisasi fitur (Z-score).
4. **Modeling**: Pengujian Measurement Invariance dan pemodelan probabilistik menggunakan Gaussian Mixture Model (GMM).
5. **Evaluation**: Evaluasi model menggunakan AIC, BIC, Entropy, Bootstrapped Likelihood Ratio Test (BLRT), dan Silhouette Score.
6. **Deployment**: Pembuatan dashboard interaktif menggunakan Streamlit.

## Tech Stack
* **Bahasa Pemrograman**: Python 3.10+
* **Manipulasi Data**: Pandas, NumPy
* **Machine Learning (GMM)**: Scikit-learn
* **Visualisasi & Deployment**: Matplotlib, Seaborn, Streamlit

## Struktur Repositori
```text
├── artifacts/                # Model GMM, Scaler Z-Score, & Profile Map dari hasil training
├── dataset_omni_dummy.csv    # Dummy data untuk demonstrasi dashboard
├── app.py                    # Source code untuk Streamlit Dashboard (Tahap 6 CRISP-DM)
├── requirements.txt          # Daftar dependensi library
├── LICENSE                   # MIT License
└── README.md                 # Dokumentasi proyek
```

## Cara Menjalankan Aplikasi (Local)
1. Clone repositori ini: `git clone https://github.com/ulhaqdhifulloh/omni-personality-lpa.git`
2. Masuk ke direktori proyek: `cd omni-personality-lpa`
3. Install dependensi: `pip install -r requirements.txt`
4. Jalankan dashboard Streamlit: `streamlit run app.py`

## Disclaimer Privasi Data
Dataset asli yang digunakan dalam penelitian ini merupakan data sekunder dari instrumen OMNI Universitas Telkom yang bersifat **rahasia dan sensitif**. Oleh karena itu, dataset asli **TIDAK** disertakan dalam repositori ini sesuai dengan protokol pelindungan data pribadi. Skrip yang disediakan dapat dijalankan menggunakan *dummy data* (`dataset_omni_dummy.csv`) yang struktur kolomnya telah disesuaikan.