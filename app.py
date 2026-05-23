import streamlit as st
import pandas as pd
import pickle
import os

# ══════════════════════════════════════════════════════════════
# KONFIGURASI HALAMAN
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Pen Nonton — Rekomendasi Film",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════════════════════
# CUSTOM CSS
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Reset & Base */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Background */
.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

/* Hide default Streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }

/* Hero Title */
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 5.5rem;
    letter-spacing: 4px;
    line-height: 1;
    background: linear-gradient(135deg, #ff6b35 0%, #f7c59f 50%, #ff6b35 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}

.hero-sub {
    font-size: 1.05rem;
    color: #888;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 300;
    margin-top: 0.3rem;
}

.hero-divider {
    width: 80px;
    height: 3px;
    background: #ff6b35;
    margin: 1.5rem 0;
}

/* Search section */
.search-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.4rem;
    letter-spacing: 3px;
    color: #ff6b35;
    margin-bottom: 0.5rem;
}

/* Multiselect styling */
.stMultiSelect > div > div {
    background: #12121a !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 8px !important;
    color: #e8e8f0 !important;
}
.stMultiSelect [data-baseweb="tag"] {
    background: #ff6b35 !important;
    border-radius: 4px !important;
}
.stMultiSelect [data-baseweb="select"] {
    background: #12121a !important;
}

/* Button */
.stButton > button {
    background: #ff6b35 !important;
    color: #0a0a0f !important;
    border: none !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.1rem !important;
    letter-spacing: 3px !important;
    padding: 0.7rem 2.5rem !important;
    border-radius: 6px !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: #f7c59f !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 25px rgba(255, 107, 53, 0.3) !important;
}

/* Film card */
.film-card {
    background: #12121a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 1.2rem;
    transition: border-color 0.2s ease, transform 0.2s ease;
}
.film-card:hover {
    border-color: #ff6b35;
    transform: translateX(4px);
}

.film-rank {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.2rem;
    color: #2a2a3a;
    min-width: 40px;
    line-height: 1;
}
.film-rank.top3 { color: #ff6b35; }

.film-info { flex: 1; }
.film-title {
    font-size: 1rem;
    font-weight: 600;
    color: #e8e8f0;
    margin-bottom: 0.25rem;
}
.film-genre {
    font-size: 0.78rem;
    color: #555;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.film-rating {
    text-align: right;
    min-width: 70px;
}
.rating-score {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.8rem;
    color: #ff6b35;
    line-height: 1;
}
.rating-label {
    font-size: 0.65rem;
    color: #444;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Stars */
.stars {
    color: #ff6b35;
    font-size: 0.7rem;
    margin-top: 0.1rem;
}

/* Section header */
.section-header {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.8rem;
    letter-spacing: 3px;
    color: #e8e8f0;
    margin-bottom: 1.2rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #1e1e2e;
}

/* Info box */
.info-box {
    background: #12121a;
    border-left: 3px solid #ff6b35;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.2rem;
    font-size: 0.88rem;
    color: #888;
    margin-bottom: 1.5rem;
}

/* Genre tag */
.genre-tag {
    display: inline-block;
    background: #1e1e2e;
    color: #888;
    font-size: 0.7rem;
    padding: 2px 8px;
    border-radius: 3px;
    margin: 2px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Stat box */
.stat-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
}
.stat-box {
    background: #12121a;
    border: 1px solid #1e1e2e;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    flex: 1;
    text-align: center;
}
.stat-number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    color: #ff6b35;
    line-height: 1;
}
.stat-label {
    font-size: 0.72rem;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 0.2rem;
}

/* Input hint */
.hint-text {
    font-size: 0.82rem;
    color: #444;
    margin-top: 0.4rem;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# LOAD MODEL & DATA
# Jalankan svd_colab.py dulu di Colab untuk generate file-file ini!
# ══════════════════════════════════════════════════════════════

@st.cache_resource
def load_model():
    with open('svd_model.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    ratings = pd.read_csv('ratings_clean.csv')
    movies  = pd.read_csv('movies_clean.csv', encoding='latin-1')
    return ratings, movies

try:
    model          = load_model()
    ratings_clean  = load_data()[0]
    movies         = load_data()[1]
    model_loaded   = True
except FileNotFoundError:
    model_loaded   = False


# ══════════════════════════════════════════════════════════════
# FUNGSI REKOMENDASI
# ══════════════════════════════════════════════════════════════

def rekomendasikan_film(film_disukai: list, top_n: int = 10):
    """
    Rekomendasikan film menggunakan SVD berdasarkan film yang disukai user.
    Mengembalikan DataFrame dengan kolom Title, Genres, PrediksiRating.
    """
    # Cari MovieID dari judul yang dipilih
    movie_ids_input = []
    for judul in film_disukai:
        cocok = movies[movies['Title'] == judul]
        if not cocok.empty:
            movie_ids_input.append(cocok.iloc[0]['MovieID'])

    if not movie_ids_input:
        return pd.DataFrame()

    # Cari user yang punya selera mirip
    user_mirip = (
        ratings_clean[
            ratings_clean['MovieID'].isin(movie_ids_input) &
            (ratings_clean['Rating'] >= 4)
        ]['UserID'].value_counts().head(50).index.tolist()
    )
    user_id = user_mirip[0] if user_mirip else ratings_clean['UserID'].iloc[0]

    # Film yang sudah ditonton user ini
    sudah_ditonton = set(
        ratings_clean[ratings_clean['UserID'] == user_id]['MovieID']
    )

    # Kandidat film yang belum ditonton
    kandidat = [
        mid for mid in movies['MovieID'].unique()
        if mid not in sudah_ditonton and mid not in movie_ids_input
    ]

    # Prediksi rating
    prediksi = [model.predict(user_id, mid) for mid in kandidat]

    hasil = (
        pd.DataFrame([
            {'MovieID': p.iid, 'PrediksiRating': round(p.est, 3)}
            for p in prediksi
        ])
        .merge(movies, on='MovieID')
        .sort_values('PrediksiRating', ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    hasil.index += 1
    return hasil[['Title', 'Genres', 'PrediksiRating']]

def rating_to_stars(score):
    filled = round(score)
    return '★' * filled + '☆' * (5 - filled)


# ══════════════════════════════════════════════════════════════
# LAYOUT UTAMA
# ══════════════════════════════════════════════════════════════

# --- Header ---
st.markdown('<p class="hero-title">PEN NONTON</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Sistem Rekomendasi Film Personal · Powered by SVD</p>', unsafe_allow_html=True)
st.markdown('<div class="hero-divider"></div>', unsafe_allow_html=True)

# --- Cek apakah model berhasil dimuat ---
if not model_loaded:
    st.error("""
    ⚠️ **File model tidak ditemukan!**

    Pastikan file-file berikut ada di folder yang sama dengan `app.py`:
    - `svd_model.pkl`
    
    - `ratings_clean.csv`
    - `movies_clean.csv`

    Jalankan `svd_colab.py` di Google Colab terlebih dahulu untuk menghasilkan file-file tersebut.
    """)
    st.stop()

# --- Stats row ---
n_movies_total  = movies['MovieID'].nunique()
n_users_total   = ratings_clean['UserID'].nunique()
n_ratings_total = len(ratings_clean)

st.markdown(f"""
<div class="stat-row">
    <div class="stat-box">
        <div class="stat-number">{n_movies_total:,}</div>
        <div class="stat-label">Film Tersedia</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">{n_users_total:,}</div>
        <div class="stat-label">Data User</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">{n_ratings_total:,}</div>
        <div class="stat-label">Total Rating</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">SVD</div>
        <div class="stat-label">Algoritma</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Daftar semua judul film untuk pilihan ---
semua_film = sorted(movies['Title'].unique().tolist())

# --- Kolom kiri: input | kanan: hasil ---
col_input, col_hasil = st.columns([1, 1.6], gap="large")

with col_input:
    st.markdown('<p class="search-label">Pilih Film Favoritmu</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        Pilih minimal 1 film yang kamu suka. Sistem akan mencari 10 film
        yang paling cocok untuk kamu berdasarkan preferensi tersebut.
    </div>
    """, unsafe_allow_html=True)

    film_dipilih = st.multiselect(
        label="Film favorit",
        options=semua_film,
        placeholder="Ketik nama film...",
        label_visibility="collapsed"
    )

    st.markdown(f'<p class="hint-text">💡 {len(semua_film):,} film tersedia · Cari dengan mengetik</p>',
                unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tombol = st.button("🎬  CARI REKOMENDASI", use_container_width=True)

    # Tampilkan film yang dipilih
    if film_dipilih:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<p class="search-label" style="font-size:1rem">Film Dipilih:</p>',
                    unsafe_allow_html=True)
        for f in film_dipilih:
            genre_row = movies[movies['Title'] == f]
            genre     = genre_row['Genres'].values[0] if not genre_row.empty else ""
            genre_tags = "".join([
                f'<span class="genre-tag">{g}</span>'
                for g in genre.split('|')
            ])
            st.markdown(f"""
            <div class="film-card" style="padding: 0.8rem 1rem;">
                <div class="film-info">
                    <div class="film-title" style="font-size:0.88rem">{f}</div>
                    <div style="margin-top:4px">{genre_tags}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

with col_hasil:
    if tombol:
        if not film_dipilih:
            st.warning("⚠️ Pilih minimal 1 film dulu ya!")
        else:
            with st.spinner("Sedang mencari rekomendasi terbaik untukmu..."):
                hasil = rekomendasikan_film(film_dipilih, top_n=10)

            if hasil.empty:
                st.error("Tidak ada rekomendasi ditemukan.")
            else:
                st.markdown(
                    f'<p class="section-header">10 Rekomendasi Untukmu</p>',
                    unsafe_allow_html=True
                )

                for i, row in hasil.iterrows():
                    rank_class = "top3" if i <= 3 else ""
                    genre_tags = "".join([
                        f'<span class="genre-tag">{g}</span>'
                        for g in row['Genres'].split('|')
                    ])
                    stars = rating_to_stars(row['PrediksiRating'])

                    st.markdown(f"""
                    <div class="film-card">
                        <div class="film-rank {rank_class}">{i:02d}</div>
                        <div class="film-info">
                            <div class="film-title">{row['Title']}</div>
                            <div style="margin-top:4px">{genre_tags}</div>
                        </div>
                        <div class="film-rating">
                            <div class="rating-score">{row['PrediksiRating']}</div>
                            <div class="stars">{stars}</div>
                            <div class="rating-label">prediksi</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        # Placeholder sebelum tombol ditekan
        st.markdown("""
        <div style="height: 100%; display: flex; flex-direction: column;
                    justify-content: center; align-items: center;
                    padding: 4rem 2rem; text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 1rem; opacity: 0.3">🎬</div>
            <div style="font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem;
                        letter-spacing: 3px; color: #2a2a3a;">
                REKOMENDASI AKAN MUNCUL DI SINI
            </div>
            <div style="color: #333; font-size: 0.85rem; margin-top: 0.5rem;">
                Pilih film favoritmu di sebelah kiri, lalu tekan tombol cari
            </div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #2a2a3a; font-size: 0.75rem;
            letter-spacing: 2px; text-transform: uppercase; padding: 1rem 0;
            border-top: 1px solid #1a1a24;">
    23.11.5806 · Proyek Data Mining · SVD Algorithm · MovieLens 1M Dataset · Andreasndrn
</div>
""", unsafe_allow_html=True)
