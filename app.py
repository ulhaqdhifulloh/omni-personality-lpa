# app.py  |  Jalankan: streamlit run app.py
# Dashboard Pemetaan Profil Kepribadian Mahasiswa
# Latent Profile Analysis · Omni Personality Inventory
# Universitas Telkom

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
import os

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================
st.set_page_config(
    page_title="OmniLPA Dashboard | Universitas Telkom",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>
/* Main styling */
.main .block-container { padding-top: 1.5rem; }

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border: 1px solid #dee2e6;
    border-radius: 12px;
    padding: 16px 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
div[data-testid="stMetric"] label {
    font-size: 0.85rem !important;
    color: #6c757d !important;
    font-weight: 600 !important;
}
div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: #212529 !important;
}

/* Profile cards */
.profile-card {
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 12px;
    border-left: 5px solid;
    background: #ffffff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.profile-rentan { border-left-color: #e74c3c; background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%); }
.profile-achiever { border-left-color: #27ae60; background: linear-gradient(135deg, #f0fff4 0%, #ffffff 100%); }
.profile-resilient { border-left-color: #2980b9; background: linear-gradient(135deg, #ebf5fb 0%, #ffffff 100%); }
.profile-impulsive { border-left-color: #e67e22; background: linear-gradient(135deg, #fef9e7 0%, #ffffff 100%); }

/* Hero section */
.hero-box {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white;
    padding: 30px 40px;
    border-radius: 16px;
    margin-bottom: 24px;
}
.hero-box h1 { color: white !important; margin-bottom: 8px; }
.hero-box p { color: #b0b0b0; font-size: 1.05rem; }

/* Process steps */
.step-box {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 16px;
    text-align: center;
    border: 1px solid #e9ecef;
    height: 100%;
}
.step-number {
    background: #0f3460;
    color: white;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    margin-bottom: 8px;
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px 8px 0 0;
    padding: 8px 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# CONSTANTS
# ==========================================================
VRIN_THRESHOLD = 70  # T-Score threshold
CD_THRESHOLD = 70    # T-Score threshold

# Load skala dari artifact (hasil feature selection)
try:
    SCALE_COLS = joblib.load('artifacts/scale_columns.pkl')
except FileNotFoundError:
    st.error("⚠️ File artifacts/scale_columns.pkl tidak ditemukan. Harap jalankan model dulu.")
    SCALE_COLS = []

DEMOG_COLS = ['Student_ID', 'Gender', 'Fakultas', 'Program_Studi', 'Angkatan']

PROFILE_CONFIG = {
    'Rentan': {
        'color': '#e74c3c', 'icon': '⚠️', 'css_class': 'profile-rentan',
        'deskripsi': (
            'Mahasiswa menunjukkan kecemasan dan depresi tinggi, '
            'moodiness tidak stabil, energi dan sosiabilitas rendah. '
            'Memiliki kecenderungan ciri Avoidant dan Borderline yang perlu dipantau.'
        ),
        'traits_tinggi': ['Anxiety', 'Depression', 'Moodiness', 'Avoidant', 'Borderline'],
        'traits_rendah': ['Energy', 'Sociability', 'Warmth', 'Trustfulness'],
        'rekomendasi': [
            '🎯 Prioritaskan sesi konseling individual dengan psikolog kampus',
            '🧘 Program Mindfulness-Based Stress Reduction (MBSR) terstruktur',
            '👥 Kelompok dukungan sebaya (peer support group) difasilitasi konselor',
            '📋 Koordinasi dosen wali untuk pemantauan akademik dan kehadiran',
            '🏃 Program aktivitas fisik ringan terstruktur (yoga, jalan pagi)',
            '📚 Penyesuaian beban akademik jika diperlukan',
        ]
    },
    'High_Achiever': {
        'color': '#27ae60', 'icon': '🏆', 'css_class': 'profile-achiever',
        'deskripsi': (
            'Mahasiswa ambisius, terorganisir, dan bertanggung jawab. '
            'Risiko gangguan kepribadian rendah. Rentan terhadap '
            'perfeksionisme berlebihan dan burnout akademik.'
        ),
        'traits_tinggi': ['Ambition', 'Dutifulness', 'Orderliness', 'SelfReliance', 'Intellect'],
        'traits_rendah': ['Impulsiveness', 'Depression', 'Borderline'],
        'rekomendasi': [
            '⚖️ Edukasi work-life balance dan burnout prevention',
            '🔬 Fasilitasi keterlibatan dalam penelitian dan kompetisi akademik',
            '💬 Coaching karir dan pengembangan kepemimpinan',
            '🧘 Workshop manajemen ekspektasi dan penetapan batas diri yang sehat',
            '🌐 Koneksi ke program beasiswa, exchange, atau magang bergengsi',
        ]
    },
    'Resilient': {
        'color': '#2980b9', 'icon': '💪', 'css_class': 'profile-resilient',
        'deskripsi': (
            'Mahasiswa dengan keseimbangan psikologis optimal: hangat, '
            'empatik, fleksibel, dan adaptif. Kelompok tersehat secara '
            'psikologis dalam populasi kampus.'
        ),
        'traits_tinggi': ['Warmth', 'Trustfulness', 'Tolerance', 'Sociability', 'Flexibility'],
        'traits_rendah': ['Hostility', 'Paranoid', 'Borderline'],
        'rekomendasi': [
            '✅ Lanjutkan intervensi universal (seminar kesehatan mental rutin)',
            '🌟 Rekrut sebagai peer educator atau fasilitator kelompok dukungan',
            '🎨 Fasilitasi eksplorasi minat ekstrakurikuler dan pengembangan diri',
            '📊 Monitoring berkala tahunan untuk mempertahankan resiliensi',
        ]
    },
    'Impulsive': {
        'color': '#e67e22', 'icon': '⚡', 'css_class': 'profile-impulsive',
        'deskripsi': (
            'Mahasiswa enerjik dan ekstrover namun impulsif, kurang terstruktur, '
            'dan cenderung mencari sensasi. Perlu dukungan regulasi emosi '
            'dan pengarahan energi secara produktif.'
        ),
        'traits_tinggi': ['Impulsiveness', 'Excitement', 'Exhibitionism', 'Energy'],
        'traits_rendah': ['Dutifulness', 'Orderliness', 'Conventionality'],
        'rekomendasi': [
            '🎮 Salurkan energi ke UKM, olahraga kompetitif, atau kepanitiaan',
            '📐 Bimbingan manajemen waktu dan perencanaan studi terstruktur',
            '🧠 Workshop regulasi emosi dan pengambilan keputusan sadar',
            '📋 Monitoring kehadiran dan progres akademik lebih intensif',
            '💼 Konseling karir untuk mengarahkan ambisi secara produktif',
        ]
    },
    'Campuran': {
        'color': '#8e44ad', 'icon': '🧩', 'css_class': 'profile-card',
        'deskripsi': (
            'Mahasiswa dengan karakteristik campuran yang tidak menunjukkan '
            'kecenderungan ekstrem pada kelompok trait tertentu. Skor berada di kisaran rata-rata '
            'atau mencerminkan variasi moderat.'
        ),
        'traits_tinggi': ['Cenderung rata-rata pada skala primer'],
        'traits_rendah': ['Cenderung rata-rata pada skala primer'],
        'rekomendasi': [
            '✅ Lanjutkan intervensi universal (seminar kesehatan mental rutin)',
            '🎯 Fasilitasi workshop pengembangan diri dan soft-skills',
            '📋 Observasi perubahan drastis dalam perilaku atau performa akademik',
            '🌟 Arahkan untuk mengikuti mentoring karir dan bakat',
        ]
    }
}

# ==========================================================
# LOAD MODEL (cached)
# ==========================================================
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load('artifacts/gmm_final_model.pkl')
        scaler = joblib.load('artifacts/scaler.pkl')
        prof_map = joblib.load('artifacts/profile_mapping.pkl')
        return model, scaler, prof_map
    except FileNotFoundError as e:
        return None, None, None

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================
def run_pipeline(df_input, model, scaler, prof_map):
    """Cleaning → Scaling → Predict → Merge"""
    steps_log = []

    # 1. Handle missing values in scales
    n_start = len(df_input)
    df_work = df_input.dropna(subset=SCALE_COLS).copy()
    n_after_na = len(df_work)
    steps_log.append(f"Missing values: {n_start - n_after_na} baris dihapus")

    # 2. Drop duplicates
    n_before_dup = len(df_work)
    df_work = df_work.drop_duplicates(subset=['Student_ID'], keep='first')
    n_after_dup = len(df_work)
    steps_log.append(f"Duplikat ID: {n_before_dup - n_after_dup} baris dihapus")

    # 3. Normalize Gender
    gender_map = {
        'Laki-laki': 'Laki-laki', 'Laki-Laki': 'Laki-laki',
        'laki-laki': 'Laki-laki', 'L': 'Laki-laki',
        'Perempuan': 'Perempuan', 'perempuan': 'Perempuan',
        'PEREMPUAN': 'Perempuan', 'P': 'Perempuan'
    }
    if 'Gender' in df_work.columns:
        df_work['Gender'] = df_work['Gender'].map(gender_map)

    # 4. Clip out-of-range values
    n_clipped = 0
    for col in SCALE_COLS:
        if col in df_work.columns:
            mask = (df_work[col] < 20) | (df_work[col] > 90)
            n_clipped += mask.sum()
            df_work[col] = df_work[col].clip(20.0, 90.0)
    steps_log.append(f"Out-of-range: {n_clipped} nilai di-clip")

    # 5. VRIN/CD filtering (T-Score based)
    n_before_valid = len(df_work)
    df_clean = df_work[
        (df_work['Val_VRIN'] < VRIN_THRESHOLD) &
        (df_work['Val_CD'] < CD_THRESHOLD)
    ].copy().reset_index(drop=True)
    n_removed_valid = n_before_valid - len(df_clean)
    steps_log.append(f"VRIN/CD filtering (T≥{VRIN_THRESHOLD}): {n_removed_valid} baris dihapus")

    total_removed = n_start - len(df_clean)
    steps_log.append(f"TOTAL: {n_start} → {len(df_clean)} ({total_removed} baris dihapus)")

    # 6. Scaling
    X_scaled = scaler.transform(df_clean[SCALE_COLS].values)

    # 7. Predict
    labels = model.predict(X_scaled)
    proba = model.predict_proba(X_scaled)

    # 8. Merge
    df_clean['Profile_ID'] = labels
    df_clean['Profile_Name'] = pd.Series(labels).map(prof_map).values
    df_clean['Prob_Klasifikasi'] = proba.max(axis=1).round(4)

    # Add probability columns
    for i in range(model.n_components):
        prof_name = prof_map.get(i, f'Profil_{i}')
        df_clean[f'Prob_{prof_name}'] = proba[:, i].round(4)

    return df_clean, total_removed, X_scaled, proba, steps_log

def compute_entropy(proba):
    N, K = proba.shape
    safe = np.clip(proba, 1e-10, 1.0)
    return 1 - (-np.sum(safe * np.log(safe))) / (N * np.log(K))


def render_profile_card(profile_name, count, total, cfg):
    """Render a styled profile card."""
    pct = count / total * 100
    st.markdown(f"""
    <div class="profile-card {cfg['css_class']}">
        <h3>{cfg['icon']} {profile_name.replace('_', ' ')} — {count} mahasiswa ({pct:.1f}%)</h3>
        <p style="color:#555; font-size:0.95rem;">{cfg['deskripsi']}</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================
with st.sidebar:
    st.markdown("### 🧠 OmniLPA System")
    st.caption("Personality Profiling · Universitas Telkom")
    st.divider()

    page = st.radio(
        "📑 Navigasi",
        ["🏠 Beranda", "📊 Prediksi Batch", "🔍 Prediksi Individual",
         "📈 Analisis & Insight", "💡 Rekomendasi Intervensi"],
        label_visibility="collapsed"
    )

    st.divider()

    # Load model
    model, scaler, prof_map = load_artifacts()
    if model is not None:
        st.success("✅ Model Loaded")
        st.caption(f"**Profil (k):** {model.n_components}  \n"
                   f"**Covariance:** Full  \n"
                   f"**VRIN/CD Threshold:** T≥{VRIN_THRESHOLD}")
    else:
        st.warning("⚠️ Model belum tersedia.\n\nJalankan notebook terlebih dahulu.")

    st.divider()
    st.caption("© 2025 Dhifulloh Dhiya Ulhaq\nTugas Akhir – Sistem Informasi\nUniversitas Telkom")

# ==========================================================
# PAGE: BERANDA
# ==========================================================
if page == "🏠 Beranda":
    st.markdown("""
    <div class="hero-box">
        <h1>🧠 Dashboard Pemetaan Profil Kepribadian Mahasiswa</h1>
        <p>Latent Profile Analysis (LPA) · Omni Personality Inventory · Universitas Telkom</p>
        <p style="color:#7f8c8d; font-size:0.9rem; margin-top:16px;">
        Sistem pendukung keputusan berbasis data untuk memetakan profil kepribadian
        mahasiswa dan menyediakan rekomendasi intervensi kesehatan mental yang tepat sasaran.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Alur Proses (CRISP-DM)")
    cols = st.columns(6)
    steps = [
        ("1", "Business\nUnderstanding", "Identifikasi kebutuhan dan tujuan analisis"),
        ("2", "Data\nUnderstanding", "Eksplorasi data Omni Test, cek kualitas"),
        ("3", "Data\nPreparation", "Cleaning VRIN/CD, seleksi fitur, Z-Score"),
        ("4", "Modeling", "GMM/LPA dengan k=2-5, estimasi parameter"),
        ("5", "Evaluation", "BIC, Entropy, BLRT, interpretasi profil"),
        ("6", "Deployment", "Dashboard interaktif + rekomendasi")
    ]
    for col, (num, title, desc) in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div class="step-box">
                <div class="step-number">{num}</div>
                <br><strong>{title}</strong>
                <p style="font-size:0.8rem; color:#666; margin-top:8px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    st.subheader("🧩 Cara Menggunakan Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 📊 Prediksi Batch (Angkatan Baru)
        Upload file CSV data Omni Test angkatan baru. Sistem akan:
        1. Membersihkan data (VRIN/CD filtering, missing values)
        2. Menstandarkan skor (Z-Score)
        3. Memprediksi profil kepribadian setiap mahasiswa
        4. Menampilkan distribusi dan insight
        """)
    with col2:
        st.markdown("""
        #### 🔍 Prediksi Individual
        Input skor kepribadian satu mahasiswa secara manual. Sistem akan:
        1. Memvalidasi skor VRIN/CD
        2. Memprediksi profil kepribadian
        3. Menampilkan probabilitas per profil
        4. Memberikan rekomendasi intervensi spesifik
        """)

    if model is not None:
        st.divider()
        st.subheader("🏷️ Profil Kepribadian yang Ditemukan")
        profile_cols = st.columns(len(PROFILE_CONFIG))
        for col, (pname, cfg) in zip(profile_cols, PROFILE_CONFIG.items()):
            with col:
                st.markdown(f"""
                <div class="profile-card {cfg['css_class']}" style="height:100%;">
                    <h4>{cfg['icon']} {pname.replace('_', ' ')}</h4>
                    <p style="font-size:0.85rem; color:#555;">{cfg['deskripsi'][:120]}...</p>
                </div>
                """, unsafe_allow_html=True)

# ==========================================================
# PAGE: PREDIKSI BATCH
# ==========================================================
elif page == "📊 Prediksi Batch":
    st.title("📊 Prediksi Batch — Upload Data Angkatan Baru")
    st.caption("Upload file CSV data Omni Test untuk memprediksi profil kepribadian secara massal.")

    if model is None:
        st.error("❌ Model belum tersedia. Jalankan notebook terlebih dahulu.")
        st.stop()

    st.divider()

    uploaded = st.file_uploader(
        "📁 Upload CSV Omni Test",
        type=['csv'],
        help="Kolom wajib: Student_ID, Gender, Fakultas, Program_Studi, "
             "Angkatan, Val_VRIN, Val_CD, dan 42 kolom Sc_*"
    )

    # Option to use default data
    use_default = False
    if uploaded is None:
        default_path = 'dataset_omni_dummy.csv'
        if os.path.exists(default_path):
            use_default = st.button("📂 Gunakan Data Bawaan (Demo)")
            demo_path = default_path

    if uploaded is not None:
        df_input = pd.read_csv(uploaded)
    elif use_default:
        df_input = pd.read_csv(demo_path)
    else:
        st.info("👆 Upload file CSV atau gunakan data bawaan untuk memulai.")
        st.stop()

    # Preview data
    with st.expander("🔎 Preview Data Input", expanded=False):
        st.dataframe(df_input.head(10), use_container_width=True)
        st.caption(f"Jumlah baris: {len(df_input)} | Jumlah kolom: {len(df_input.columns)}")

    st.divider()

    # Run pipeline
    with st.spinner("⏳ Memproses: Cleaning → Scaling → Predicting..."):
        df_res, n_removed, X_sc, proba, steps_log = run_pipeline(
            df_input, model, scaler, prof_map
        )
    entropy = compute_entropy(proba)

    # Show process steps
    st.subheader("🔄 Proses Data Cleaning")
    process_cols = st.columns(len(steps_log))
    for i, (col, log) in enumerate(zip(process_cols, steps_log)):
        with col:
            parts = log.split(": ")
            label = parts[0] if len(parts) > 1 else "Step"
            value = parts[1] if len(parts) > 1 else log
            st.metric(label, value)

    st.divider()

    # KPI Cards
    st.subheader("📊 Ringkasan Hasil Analisis")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Input", f"{len(df_input):,}")
    c2.metric("Valid (Dianalisis)", f"{len(df_res):,}",
              delta=f"-{n_removed} dihapus", delta_color="inverse")
    c3.metric("Entropy Model", f"{entropy:.3f}",
              delta="Baik ✅" if entropy >= 0.80 else "Cukup ⚠️",
              delta_color="normal" if entropy >= 0.80 else "off")
    c4.metric("Jumlah Profil", model.n_components)
    dominant = df_res['Profile_Name'].value_counts().idxmax()
    c5.metric("Profil Dominan", dominant.replace('_', ' '))

    st.divider()

    # Distribution charts
    st.subheader("🥧 Distribusi Profil Kepribadian")
    dist = df_res['Profile_Name'].value_counts().reset_index()
    dist.columns = ['Profil', 'Jumlah']
    dist['Persen'] = (dist['Jumlah'] / dist['Jumlah'].sum() * 100).round(1)

    col_p, col_b = st.columns(2)
    with col_p:
        fig = px.pie(
            dist, names='Profil', values='Jumlah',
            title='Proporsi Profil (Keseluruhan)',
            color='Profil',
            color_discrete_map={v: PROFILE_CONFIG[v]['color']
                                for v in PROFILE_CONFIG if v in dist['Profil'].values},
            hole=0.45
        )
        fig.update_traces(textinfo='percent+label+value', textfont_size=12)
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        fig2 = px.bar(
            dist, x='Profil', y='Jumlah',
            title='Jumlah Mahasiswa per Profil',
            color='Profil',
            color_discrete_map={v: PROFILE_CONFIG[v]['color']
                                for v in PROFILE_CONFIG if v in dist['Profil'].values},
            text='Jumlah'
        )
        fig2.update_traces(textposition='outside')
        fig2.update_layout(showlegend=False, xaxis_tickangle=0)
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # Result table
    st.subheader("📋 Tabel Hasil Prediksi per Mahasiswa")
    show_cols = DEMOG_COLS + ['Profile_Name', 'Prob_Klasifikasi']
    df_disp = df_res[show_cols].rename(columns={
        'Profile_Name': 'Profil Kepribadian',
        'Prob_Klasifikasi': 'Prob. Klasifikasi'
    })

    # Filter
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        filter_profile = st.multiselect(
            "Filter Profil:",
            options=df_disp['Profil Kepribadian'].unique(),
            default=df_disp['Profil Kepribadian'].unique()
        )
    with col_f2:
        search_id = st.text_input("🔍 Cari Student ID:", "")

    df_show = df_disp[df_disp['Profil Kepribadian'].isin(filter_profile)]
    if search_id:
        df_show = df_show[df_show['Student_ID'].str.contains(search_id, case=False, na=False)]

    st.dataframe(df_show, use_container_width=True, height=400)

    st.download_button(
        label="⬇️ Download Hasil Prediksi (CSV)",
        data=df_res.to_csv(index=False).encode('utf-8'),
        file_name="hasil_profiling_omni.csv",
        mime="text/csv"
    )

# ==========================================================
# PAGE: PREDIKSI INDIVIDUAL
# ==========================================================
elif page == "🔍 Prediksi Individual":
    st.title("🔍 Prediksi Individual — Input Manual")
    st.caption("Masukkan skor kepribadian mahasiswa untuk memprediksi profil kepribadiannya.")

    if model is None:
        st.error("❌ Model belum tersedia. Jalankan notebook terlebih dahulu.")
        st.stop()

    st.divider()

    with st.form("individual_form"):
        st.subheader("📝 Data Demografis")
        d1, d2, d3, d4 = st.columns(4)
        with d1:
            inp_id = st.text_input("Student ID", "STxxxx")
        with d2:
            inp_gender = st.selectbox("Gender", ["Laki-laki", "Perempuan"])
        with d3:
            inp_fak = st.selectbox("Fakultas", ["FIF", "FTE", "FRI", "FEB", "FKS"])
        with d4:
            inp_angkatan = st.selectbox("Angkatan", [2021, 2022, 2023, 2024])

        v1, v2 = st.columns(2)
        with v1:
            inp_vrin = st.number_input("Val_VRIN (T-Score)", 20.0, 90.0, 45.0, 0.5)
        with v2:
            inp_cd = st.number_input("Val_CD (T-Score)", 20.0, 90.0, 45.0, 0.5)

        st.subheader("📏 Skor 42 Skala Kepribadian")
        st.caption("Masukkan skor T (rentang 20-90) untuk setiap skala.")

        scale_values = {}
        # Layout: 5 columns x 7 rows
        for row_start in range(0, len(SCALE_COLS), 5):
            cols = st.columns(5)
            for j, col in enumerate(cols):
                idx = row_start + j
                if idx < len(SCALE_COLS):
                    scale_name = SCALE_COLS[idx]
                    label = scale_name.replace('Sc_', '')
                    with col:
                        scale_values[scale_name] = st.number_input(
                            label, 20.0, 90.0, 50.0, 0.5, key=f"sc_{idx}"
                        )

        submitted = st.form_submit_button("🔮 Prediksi Profil", use_container_width=True)

    if submitted:
        # Validate VRIN/CD
        if inp_vrin > VRIN_THRESHOLD or inp_cd > CD_THRESHOLD:
            st.error(
                f"⚠️ Skor Val_VRIN ({inp_vrin}) atau Val_CD ({inp_cd}) melebihi threshold (T≥{VRIN_THRESHOLD}). "
                f"Respons dianggap tidak valid (careless responding). "
                f"Data ini akan di-filter pada tahap cleaning."
            )
        else:
            # Prepare data
            input_arr = np.array([[scale_values[c] for c in SCALE_COLS]])
            input_scaled = scaler.transform(input_arr)

            # Predict
            pred_label = model.predict(input_scaled)[0]
            pred_proba = model.predict_proba(input_scaled)[0]
            pred_name = prof_map[pred_label]
            cfg = PROFILE_CONFIG.get(pred_name, {})

            st.divider()
            st.subheader("🎯 Hasil Prediksi")

            # Profile card
            render_profile_card(pred_name, 1, 1, cfg)

            # Probability distribution
            st.markdown("**📊 Probabilitas Keanggotaan per Profil:**")
            prob_cols = st.columns(len(prof_map))
            for i, (pid, pname) in enumerate(prof_map.items()):
                pcfg = PROFILE_CONFIG.get(pname, {'icon': '📌', 'color': '#95a5a6'})
                with prob_cols[i]:
                    pct = pred_proba[pid] * 100
                    st.metric(
                        f"{pcfg['icon']} {pname.replace('_', ' ')}",
                        f"{pct:.1f}%"
                    )

            # Recommendations
            st.divider()
            st.subheader("💡 Rekomendasi Intervensi")
            if 'rekomendasi' in cfg:
                for rec in cfg['rekomendasi']:
                    st.markdown(f"- {rec}")

# ==========================================================
# PAGE: ANALISIS & INSIGHT
# ==========================================================
elif page == "📈 Analisis & Insight":
    st.title("📈 Analisis & Insight — Distribusi Lintas Demografis")

    if model is None:
        st.error("❌ Model belum tersedia.")
        st.stop()

    # Load data
    data_paths = ['dataset_omni_dummy.csv']
    df_data = None
    for p in data_paths:
        if os.path.exists(p):
            df_data = pd.read_csv(p)
            break

    if df_data is None:
        st.warning("⚠️ Tidak ada data untuk dianalisis. Upload data di halaman Prediksi Batch terlebih dahulu.")
        st.stop()

    # Check if Profile_Name already exists
    if 'Profile_Name' not in df_data.columns:
        with st.spinner("Memproses data..."):
            df_data, _, _, _, _ = run_pipeline(df_data, model, scaler, prof_map)

    st.divider()

    # Filters
    st.subheader("🔍 Filter Demografis")
    cf1, cf2, cf3, cf4 = st.columns(4)
    with cf1:
        sel_fak = st.multiselect("Fakultas",
            options=sorted(df_data['Fakultas'].dropna().unique()),
            default=sorted(df_data['Fakultas'].dropna().unique()))
    with cf2:
        sel_prodi = st.multiselect("Program Studi",
            options=sorted(df_data['Program_Studi'].dropna().unique()),
            default=sorted(df_data['Program_Studi'].dropna().unique()))
    with cf3:
        sel_angk = st.multiselect("Angkatan",
            options=sorted(df_data['Angkatan'].dropna().unique()),
            default=sorted(df_data['Angkatan'].dropna().unique()))
    with cf4:
        sel_gender = st.multiselect("Gender",
            options=sorted(df_data['Gender'].dropna().unique()),
            default=sorted(df_data['Gender'].dropna().unique()))

    df_f = df_data[
        df_data['Fakultas'].isin(sel_fak) &
        df_data['Program_Studi'].isin(sel_prodi) &
        df_data['Angkatan'].isin(sel_angk) &
        df_data['Gender'].isin(sel_gender)
    ]

    st.caption(f"📌 **{len(df_f):,}** mahasiswa ditampilkan setelah filter")
    st.divider()

    # Charts
    color_map = {v: PROFILE_CONFIG[v]['color'] for v in PROFILE_CONFIG}

    cg1, cg2 = st.columns(2)
    with cg1:
        ct_fak = (pd.crosstab(df_f['Fakultas'], df_f['Profile_Name'],
                               normalize='index') * 100).reset_index()
        ct_fak = ct_fak.melt(id_vars='Fakultas', var_name='Profil', value_name='Persen')
        fig3 = px.bar(ct_fak, x='Fakultas', y='Persen', color='Profil',
                      barmode='stack', title='Distribusi Profil per Fakultas (%)',
                      color_discrete_map=color_map)
        fig3.update_layout(xaxis_tickangle=-20)
        st.plotly_chart(fig3, use_container_width=True)

    with cg2:
        ct_ang = (pd.crosstab(df_f['Angkatan'], df_f['Profile_Name'],
                               normalize='index') * 100).reset_index()
        ct_ang = ct_ang.melt(id_vars='Angkatan', var_name='Profil', value_name='Persen')
        fig4 = px.bar(ct_ang, x='Angkatan', y='Persen', color='Profil',
                      barmode='stack', title='Distribusi Profil per Angkatan (%)',
                      color_discrete_map=color_map)
        st.plotly_chart(fig4, use_container_width=True)

    cg3, cg4 = st.columns(2)
    with cg3:
        ct_prodi = (pd.crosstab(df_f['Program_Studi'], df_f['Profile_Name'],
                                 normalize='index') * 100).reset_index()
        ct_prodi = ct_prodi.melt(id_vars='Program_Studi', var_name='Profil', value_name='Persen')
        fig5 = px.bar(ct_prodi, x='Program_Studi', y='Persen', color='Profil',
                      barmode='stack', title='Distribusi Profil per Program Studi (%)',
                      color_discrete_map=color_map)
        fig5.update_layout(xaxis_tickangle=-30)
        st.plotly_chart(fig5, use_container_width=True)

    with cg4:
        ct_gender = (pd.crosstab(df_f['Gender'], df_f['Profile_Name'],
                                  normalize='index') * 100).reset_index()
        ct_gender = ct_gender.melt(id_vars='Gender', var_name='Profil', value_name='Persen')
        fig6 = px.bar(ct_gender, x='Gender', y='Persen', color='Profil',
                      barmode='stack', title='Distribusi Profil per Gender (%)',
                      color_discrete_map=color_map)
        st.plotly_chart(fig6, use_container_width=True)

    st.divider()

    # Heatmap
    st.subheader("🔥 Heatmap Proporsi Profil per Program Studi")
    if len(df_f) > 0:
        ct_heat = pd.crosstab(df_f['Program_Studi'], df_f['Profile_Name'],
                               normalize='index') * 100
        fig_heat = px.imshow(
            ct_heat.round(1),
            text_auto=True,
            color_continuous_scale='RdYlGn_r',
            aspect='auto',
            title='Proporsi Profil per Program Studi (%)'
        )
        fig_heat.update_layout(height=400)
        st.plotly_chart(fig_heat, use_container_width=True)

# ==========================================================
# PAGE: REKOMENDASI INTERVENSI
# ==========================================================
elif page == "💡 Rekomendasi Intervensi":
    st.title("💡 Rekomendasi Intervensi Kesehatan Mental")
    st.caption(
        "Rekomendasi program intervensi dihasilkan berdasarkan karakteristik masing-masing "
        "profil kepribadian yang ditemukan oleh model LPA. Rekomendasi bersifat panduan umum "
        "dan perlu divalidasi oleh psikolog profesional."
    )

    if model is None:
        st.error("❌ Model belum tersedia.")
        st.stop()

    st.divider()

    # Load data to show stats
    data_paths = ['dataset_omni_dummy.csv']
    df_data = None
    for p in data_paths:
        if os.path.exists(p):
            df_data = pd.read_csv(p)
            break

    has_data = False
    if df_data is not None:
        if 'Profile_Name' not in df_data.columns:
            try:
                df_data, _, _, _, _ = run_pipeline(df_data, model, scaler, prof_map)
                has_data = True
            except Exception:
                has_data = False
        else:
            has_data = True

    profiles_to_show = []
    if has_data:
        profiles_to_show = df_data['Profile_Name'].dropna().unique()
    elif model is not None and prof_map is not None:
        st.info("⚠️ Menampilkan rekomendasi berdasarkan profil dari model yang sedang aktif.")
        profiles_to_show = list(prof_map.values())

    for pname in profiles_to_show:
        cfg = PROFILE_CONFIG.get(pname, {
            'color': '#95a5a6', 'icon': '📌', 'css_class': 'profile-card',
            'deskripsi': 'Profil ini belum memiliki deskripsi spesifik.',
            'rekomendasi': ['Evaluasi lebih lanjut oleh tim konseling.']
        })

        count = 0
        pct = 0
        if has_data:
            subset = df_data[df_data['Profile_Name'] == pname]
            count = len(subset)
            pct = count / len(df_data) * 100

        with st.expander(
            f"{cfg['icon']} **{pname.replace('_', ' ')}**"
            + (f" — {count} mahasiswa ({pct:.1f}%)" if has_data else ""),
            expanded=(pct >= 20 if has_data else False)
        ):
            col_desc, col_rec = st.columns([1, 1])

            with col_desc:
                st.markdown("**📌 Deskripsi Profil:**")
                st.info(cfg['deskripsi'])

                st.markdown("**📊 Ciri Dominan:**")
                traits_up = ", ".join(cfg.get('traits_tinggi', []))
                traits_dn = ", ".join(cfg.get('traits_rendah', []))
                st.markdown(f"- 🔺 **Tinggi:** {traits_up}")
                st.markdown(f"- 🔻 **Rendah:** {traits_dn}")

                if has_data and count > 0:
                    st.markdown("**📍 Sebaran per Fakultas:**")
                    mini = subset['Fakultas'].value_counts().reset_index()
                    mini.columns = ['Fakultas', 'n']
                    fig_mini = px.bar(mini, x='Fakultas', y='n',
                                     title=f'Sebaran {pname.replace("_", " ")} per Fakultas',
                                     color_discrete_sequence=[cfg['color']])
                    fig_mini.update_layout(height=260, showlegend=False,
                                           margin=dict(t=35, b=0, l=0, r=0))
                    st.plotly_chart(fig_mini, use_container_width=True)

            with col_rec:
                st.markdown("**🎯 Rekomendasi Program Intervensi:**")
                for rec in cfg['rekomendasi']:
                    st.markdown(f"- {rec}")

                if pname == 'Rentan':
                    st.warning(
                        "⚠️ **Prioritas tinggi.** Kelompok ini memerlukan intervensi "
                        "selektif dan indikasi segera. Koordinasikan dengan unit konseling."
                    )
                elif pname == 'Impulsive':
                    st.info(
                        "💡 **Pendekatan positif.** Alihkan energi ke kegiatan produktif, "
                        "bukan pendekatan restriktif."
                    )

    st.divider()
    st.markdown("""
    > **Catatan Penting:**
    > - Rekomendasi ini bersifat panduan umum berdasarkan pola data, bukan diagnosis klinis
    > - Implementasi program tetap memerlukan validasi dan supervisi psikolog profesional
    > - Profil bersifat probabilistik — setiap mahasiswa memiliki derajat keanggotaan di semua profil
    > - Evaluasi efektivitas program perlu dilakukan secara berkala (siklus tahunan)
    """)