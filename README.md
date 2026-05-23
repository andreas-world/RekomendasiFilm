# 🎬 CineMatch — Sistem Rekomendasi Film berbasis SVD

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?style=flat-square&logo=streamlit)
![Algorithm](https://img.shields.io/badge/Algorithm-SVD-orange?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-MovieLens%201M-green?style=flat-square)

**CineMatch** adalah sistem rekomendasi film personal yang dibangun menggunakan algoritma **SVD (Singular Value Decomposition)** dengan dataset **MovieLens 1M**. Proyek ini merupakan implementasi *Collaborative Filtering* berbasis matrix factorization yang di-deploy sebagai web aplikasi interaktif menggunakan Streamlit.

---

## 📌 Deskripsi Proyek

Proyek ini dikembangkan sebagai bagian dari mata kuliah **Proyek Data Mining (ST167)** — Universitas AMIKOM Yogyakarta, Semester Genap 2025/2026.

Sistem menerima input berupa film-film yang disukai pengguna, kemudian memprediksi dan merekomendasikan film lain yang kemungkinan besar akan disukai berdasarkan pola rating dari jutaan pengguna lain dalam dataset MovieLens 1M.

---

## 🧠 Algoritma & Teknik

| Komponen | Detail |
|---|---|
| Algoritma | SVD (Singular Value Decomposition) |
| Library | `scikit-surprise` |
| n_factors | 100 |
| n_epochs | 20 |
| lr_all | 0.005 |
| reg_all | 0.02 |
| Evaluasi | RMSE: **0.8726** · MAE: **0.6857** |
| Cross-Validation | CV RMSE: 0.8735 ± 0.0013 |

---

## 📊 Dataset

- **Sumber**: [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) — GroupLens Research
- **Total Rating**: ~1.000.209
- **Total User**: 6.040
- **Total Film**: 3.883
- **Format**: `.dat` (separator `::`)

| File | Isi |
|---|---|
| `movies.dat` | MovieID, Title, Genres |
| `ratings.dat` | UserID, MovieID, Rating, Timestamp |
| `users.dat` | UserID, Gender, Age, Occupation, Zip-code |

---

## 🚀 Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/andreas-world/RekomendasiFilm.git
cd cinematch
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Siapkan File Model
Jalankan notebook `UTS_ProyekDM.ipynb` di Google Colab untuk menghasilkan:
- `svd_model.pkl` — model SVD terlatih
- `ratings_clean.csv` — data rating bersih
- `movies_clean.csv` — data film bersih

Lalu download dan letakkan di folder yang sama dengan `app.py`.

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```

Buka browser di `http://localhost:8501`

---

## 📁 Struktur Folder

```
cinematch/
├── app.py                  # Web app Streamlit
├── UTS_ProyekDM.ipynb      # Notebook Colab (EDA + Training)
├── requirements.txt        # Dependencies
├── README.md               # Dokumentasi
├── svd_model.pkl           # Model terlatih (generate dari Colab)
├── ratings_clean.csv       # Data rating bersih
└── movies_clean.csv        # Data film bersih
```

---

## ✨ Fitur Aplikasi

- 🔍 **Pencarian film** — cari dan pilih film favorit via dropdown
- 🤖 **Rekomendasi personal** — top-N film berdasarkan preferensi
- ⭐ **Prediksi rating** — estimasi rating yang akan diberikan user
- 🎭 **Info genre** — tampil genre tiap film rekomendasi
- 📊 **Statistik dataset** — total film, user, dan rating

---

## 📈 Pipeline Proyek

```
Data Collection → EDA → Preprocessing → Modelling (SVD) → Evaluasi → Deployment
```

1. **Data Collection** — Load dataset MovieLens 1M (.dat files)
2. **EDA** — Analisis distribusi rating, genre populer, aktivitas user
3. **Preprocessing** — Cleaning, format konversi, split train/test
4. **Modelling** — Training SVD dengan scikit-surprise
5. **Evaluasi** — RMSE, MAE, Cross-Validation
6. **Deployment** — Web app Streamlit

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit** — Web framework
- **scikit-surprise** — Recommender system library
- **Pandas & NumPy** — Data processing
- **Google Colab** — Training environment

---

## 👨‍💻 Developer

| Info | Detail |
|---|---|
| Nama | *(Nama kamu)* |
| NIM | *(NIM kamu)* |
| Prodi | S1 Informatika |
| Universitas | Universitas AMIKOM Yogyakarta |
| Mata Kuliah | Proyek Data Mining (ST167) |
| Dosen | Theopilus Bayu Sasongko, S.Kom.,M.Eng · Anna Baita, M.Kom · Kusnawi, S.Kom, M.Eng |

---

> *"Dibuat dengan ☕ dan semangat belajar untuk UTS Proyek Data Mining 2025/2026"*
