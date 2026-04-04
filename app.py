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
.profile-vulnerable { border-left-color: #e74c3c; background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%); }
.profile-resilient { border-left-color: #2980b9; background: linear-gradient(135deg, #ebf5fb 0%, #ffffff 100%); }
.profile-energetic { border-left-color: #e67e22; background: linear-gradient(135deg, #fef9e7 0%, #ffffff 100%); }

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
# CONSTANTS - 7 BROAD SCALES (Factor Scales)
# ==========================================================
BROAD_SCALES = [
    'Sc_Agreeableness', 'Sc_Conscientiousness', 'Sc_Extraversion',
    'Sc_Narcissism', 'Sc_Neuroticism', 'Sc_Openness', 'Sc_SensationSeeking'
]

DEMOG_COLS = ['Student_ID', 'Gender', 'Fakultas', 'Program_Studi', 'Angkatan']

# Profile configuration based on profile_mapping.pkl from training
# Keys match the actual profile names from the labeled dataset
PROFILE_CONFIG = {
    'The Energetic & Socially Active': {
        'color': '#e67e22',
        'icon': '⚡',
        'css_class': 'profile-energetic',
        'label_short': 'Energetic',
        'kategori': 'Intervensi Pengembangan Diri',
        'deskripsi': (
            'Dominan secara sosial dan asertif, namun rendahnya keteraturan '
            'memicu risiko impulsivitas tinggi.'
        ),
        'traits_tinggi': ['Extraversion', 'SensationSeeking', 'Narcissism'],
        'traits_rendah': ['Conscientiousness'],
        'rekomendasi': [
            '📈 Daftarkan ke workshop manajemen waktu dan penetapan skala prioritas.',
            '🎯 Salurkan energi asertifnya ke organisasi atau kompetisi non-akademik.',
            '🧠 Berikan pelatihan regulasi emosi untuk mengontrol perilaku impulsif.'
        ]
    },
    'The Resilient & Adaptive': {
        'color': '#2980b9',
        'icon': '💪',
        'css_class': 'profile-resilient',
        'label_short': 'Resilient',
        'kategori': 'Baseline / Normatif',
        'deskripsi': (
            'Stabilitas emosi tinggi, memiliki daya tahan stres (resilient), '
            'dan sangat kooperatif.'
        ),
        'traits_tinggi': ['Agreeableness', 'Conscientiousness', 'Openness'],
        'traits_rendah': ['Neuroticism'],
        'rekomendasi': [
            '🌟 Tawarkan rekrutmen sebagai Peer Counselor (Konselor Sebaya) kampus.',
            '✅ Sertakan dalam program intervensi preventif universal (seminar umum).',
            '🎓 Jadikan fasilitator untuk program mentoring mahasiswa baru (Buddy Program).'
        ]
    },
    'The Vulnerable / At-Risk': {
        'color': '#e74c3c',
        'icon': '⚠️',
        'css_class': 'profile-vulnerable',
        'label_short': 'Vulnerable',
        'kategori': 'Kelompok Risiko Tinggi',
        'deskripsi': (
            'Neuroticism sangat tinggi (>65 T-Score), rentan mengalami '
            'isolasi sosial dan distres.'
        ),
        'traits_tinggi': ['Neuroticism'],
        'traits_rendah': ['Extraversion', 'Agreeableness', 'Conscientiousness'],
        'rekomendasi': [
            '🆘 Jadwalkan prioritas utama untuk konseling klinis tatap muka.',
            '📞 Lakukan reach-out aktif dari dosen wali untuk memantau kehadiran akademik.',
            '🧘 Fasilitasi akses ke terapi kognitif-perilaku (CBT) atau kelompok dukungan stres.'
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
        rule_base = joblib.load('artifacts/rule_base_intervensi.pkl')
        scale_cols = joblib.load('artifacts/scale_columns.pkl')
        return model, scaler, prof_map, rule_base, scale_cols
    except FileNotFoundError as e:
        return None, None, None, None, None

@st.cache_data
def load_labeled_dataset():
    try:
        df = pd.read_csv('artifacts/dataset_omni_final_labeled.csv')
        return df
    except FileNotFoundError:
        return None

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================
def compute_entropy(proba):
    N, K = proba.shape
    safe = np.clip(proba, 1e-10, 1.0)
    return 1 - (-np.sum(safe * np.log(safe))) / (N * np.log(K))

def get_profile_config(profile_name):
    return PROFILE_CONFIG.get(profile_name, {
        'color': '#95a5a6', 'icon': '📌', 'css_class': 'profile-card',
        'label_short': profile_name.split()[0] if profile_name else 'Unknown',
        'kategori': 'Tidak Terklasifikasi',
        'deskripsi': 'Profil ini belum memiliki deskripsi spesifik.',
        'rekomendasi': ['Evaluasi lebih lanjut oleh tim konseling.']
    })

def render_profile_card(profile_name, count, total, cfg):
    pct = count / total * 100
    st.markdown(f"""
    <div class="profile-card {cfg['css_class']}">
        <h3>{cfg['icon']} {profile_name} — {count} mahasiswa ({pct:.1f}%)</h3>
        <p style="color:#555; font-size:0.95rem;">{cfg['deskripsi']}</p>
        <p style="color:#666; font-size:0.85rem;"><b>Kategori:</b> {cfg['kategori']}</p>
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

    model, scaler, prof_map, rule_base, scale_cols = load_artifacts()
    if model is not None:
        st.success("✅ Model Loaded")
        st.caption(f"**Profil (k):** {model.n_components}  \n"
                   f"**Covariance:** Full  \n"
                   f"**Fitur:** {len(scale_cols) if scale_cols else 7} Broad Scales")
    else:
        st.warning("⚠️ Model belum tersedia.\n\nJalankan notebook terlebih dahulu.")

    st.divider()
    st.caption("© 2026 Dhifulloh Dhiya Ulhaq\nTugas Akhir – Sistem Informasi\nUniversitas Telkom")

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
        mahasiswa menggunakan <b>7 Factor Scales (Broad Scales)</b> dari OMNI Test.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Alur Proses (CRISP-DM)")
    cols = st.columns(6)
    steps = [
        ("1", "Business\nUnderstanding", "Identifikasi kebutuhan dan tujuan analisis"),
        ("2", "Data\nUnderstanding", "Eksplorasi data Omni Test, cek kualitas"),
        ("3", "Data\nPreparation", "Cleaning VRIN/CD, seleksi 7 fitur, Z-Score"),
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

    st.subheader("📊 Fitur Input: 7 Factor Scales (Broad Scales)")
    st.info("""
    Model LPA menggunakan **7 Factor Scales** dari OMNI Personality Inventory sebagai fitur utama:
    - **Sc_Agreeableness** - Keagreeableness (kemudahan bergaul)
    - **Sc_Conscientiousness** - Conscientiousness (keteraturan)
    - **Sc_Extraversion** - Extraversion (ekstraversi)
    - **Sc_Narcissism** - Narcissism (narsisme)
    - **Sc_Neuroticism** - Neuroticism (neurotisisme)
    - **Sc_Openness** - Openness (keterbukaan)
    - **Sc_SensationSeeking** - Sensation Seeking (pencarian sensasi)
    """)

    st.divider()

    st.subheader("🏷️ Profil Kepribadian yang Ditemukan")
    if model is not None and prof_map is not None:
        profile_cols = st.columns(len(prof_map))
        for col, (pid, info) in zip(profile_cols, prof_map.items()):
            profile_name = info['label']
            cfg = get_profile_config(profile_name)
            with col:
                st.markdown(f"""
                <div class="profile-card {cfg['css_class']}" style="height:100%;">
                    <h4>{cfg['icon']} {cfg['label_short']}</h4>
                    <p style="font-size:0.75rem; color:#888;"><b>{info['kategori']}</b></p>
                    <p style="font-size:0.85rem; color:#555;">{cfg['deskripsi'][:100]}...</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Model belum tersedia.")

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

    st.info(f"""
    📋 **Format CSV yang Diharapkan:**
    - Kolom wajib: {', '.join(DEMOG_COLS)}
    - Kolom skala: {', '.join(BROAD_SCALES)}
    """)

    uploaded = st.file_uploader(
        "📁 Upload CSV Omni Test",
        type=['csv'],
        help="Pastikan file CSV memiliki kolom yang sesuai dengan format."
    )

    use_default = False
    if uploaded is None:
        if os.path.exists('artifacts/dataset_omni_final_labeled.csv'):
            use_default = st.button("📂 Gunakan Data Labeling Hasil Training (Demo)")
            demo_path = 'artifacts/dataset_omni_final_labeled.csv'

    if uploaded is not None:
        df_input = pd.read_csv(uploaded)
    elif use_default:
        df_input = pd.read_csv(demo_path)
    else:
        st.info("👆 Upload file CSV atau gunakan data bawaan untuk memulai.")
        st.stop()

    with st.expander("🔎 Preview Data Input", expanded=False):
        st.dataframe(df_input.head(10), use_container_width=True)
        st.caption(f"Jumlah baris: {len(df_input)} | Jumlah kolom: {len(df_input.columns)}")

    st.divider()

    required_cols = list(set(DEMOG_COLS + BROAD_SCALES))
    missing_cols = [c for c in required_cols if c not in df_input.columns]
    
    if missing_cols:
        st.warning(f"⚠️ Kolom yang hilang: {missing_cols}")
        if st.checkbox("Lanjutkan dengan kolom yang ada (untuk demo)"):
            pass
        else:
            st.stop()

    with st.spinner("⏳ Memproses: Preprocessing → Scaling → Predicting..."):
        steps_log = []
        n_start = len(df_input)
        
        df_work = df_input.copy()
        
        missing_rows = df_work[BROAD_SCALES].isnull().any(axis=1).sum()
        df_work = df_work.dropna(subset=BROAD_SCALES)
        steps_log.append(f"Missing values: {missing_rows} baris dihapus")

        dup_before = len(df_work)
        df_work = df_work.drop_duplicates(subset=['Student_ID'], keep='first')
        dup_removed = dup_before - len(df_work)
        steps_log.append(f"Duplikat ID: {dup_removed} baris dihapus")

        gender_map = {
            'Laki-laki': 'Laki-laki', 'Laki-Laki': 'Laki-laki',
            'laki-laki': 'Laki-laki', 'L': 'Laki-laki',
            'Perempuan': 'Perempuan', 'perempuan': 'Perempuan',
            'PEREMPUAN': 'Perempuan', 'P': 'Perempuan'
        }
        if 'Gender' in df_work.columns:
            df_work['Gender'] = df_work['Gender'].map(gender_map)

        n_valid = len(df_work)
        steps_log.append(f"Data valid: {n_valid} baris siap prediksi")

        total_removed = n_start - n_valid
        steps_log.append(f"TOTAL: {n_start} → {n_valid} ({total_removed} baris dihapus)")

        cols_to_scale = [c for c in BROAD_SCALES if c in df_work.columns]
        X_scaled = scaler.transform(df_work[cols_to_scale].values)
        labels = model.predict(X_scaled)
        proba = model.predict_proba(X_scaled)

        df_work['Klaster'] = labels
        df_work['Profile_Name'] = [prof_map[l]['label'] for l in labels]
        df_work['Prob_Klasifikasi'] = proba.max(axis=1).round(4)
        df_work['Kategori_Risiko'] = [prof_map[l]['kategori'] for l in labels]

        for i in range(model.n_components):
            prof_name = prof_map.get(i, {}).get('label', f'Profil_{i}')
            df_work[f'Prob_{prof_name}'] = proba[:, i].round(4)

    entropy = compute_entropy(proba)

    st.subheader("🔄 Proses Data Preprocessing")
    process_cols = st.columns(len(steps_log))
    for i, (col, log) in enumerate(zip(process_cols, steps_log)):
        with col:
            parts = log.split(": ")
            label = parts[0] if len(parts) > 1 else "Step"
            value = parts[1] if len(parts) > 1 else log
            st.metric(label, value)

    st.divider()

    st.subheader("📊 Ringkasan Hasil Analisis")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Input", f"{n_start:,}")
    c2.metric("Valid (Dianalisis)", f"{n_valid:,}",
              delta=f"-{total_removed} dihapus", delta_color="inverse")
    c3.metric("Entropy Model", f"{entropy:.3f}",
              delta="Baik ✅" if entropy >= 0.80 else "Cukup ⚠️",
              delta_color="normal" if entropy >= 0.80 else "off")
    c4.metric("Jumlah Profil", model.n_components)
    
    profile_counts = df_work['Profile_Name'].value_counts()
    if len(profile_counts) > 0:
        dominant = profile_counts.idxmax()
        cfg_dom = get_profile_config(dominant)
        c5.metric("Profil Dominan", cfg_dom['label_short'])

    st.divider()

    st.subheader("🥧 Distribusi Profil Kepribadian")
    dist = df_work['Profile_Name'].value_counts().reset_index()
    dist.columns = ['Profil', 'Jumlah']
    dist['Persen'] = (dist['Jumlah'] / dist['Jumlah'].sum() * 100).round(1)

    color_map = {name: get_profile_config(name)['color'] for name in dist['Profil'].unique()}

    col_p, col_b = st.columns(2)
    with col_p:
        fig = px.pie(
            dist, names='Profil', values='Jumlah',
            title='Proporsi Profil (Keseluruhan)',
            color='Profil',
            color_discrete_map=color_map,
            hole=0.45
        )
        fig.update_traces(textinfo='percent+label+value', textfont_size=12)
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        fig2 = px.bar(
            dist, x='Profil', y='Jumlah',
            title='Jumlah Mahasiswa per Profil',
            color='Profil',
            color_discrete_map=color_map,
            text='Jumlah'
        )
        fig2.update_traces(textposition='outside')
        fig2.update_layout(showlegend=False, xaxis_tickangle=-15)
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("📋 Tabel Hasil Prediksi per Mahasiswa")
    show_cols = ['Student_ID', 'Gender', 'Fakultas', 'Program_Studi', 'Angkatan', 'Profile_Name', 'Prob_Klasifikasi']
    show_cols = [c for c in show_cols if c in df_work.columns]
    df_disp = df_work[show_cols].rename(columns={
        'Profile_Name': 'Profil Kepribadian',
        'Prob_Klasifikasi': 'Prob. Klasifikasi'
    })

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
        data=df_work.to_csv(index=False).encode('utf-8'),
        file_name="hasil_profiling_omni.csv",
        mime="text/csv"
    )

# ==========================================================
# PAGE: PREDIKSI INDIVIDUAL
# ==========================================================
elif page == "🔍 Prediksi Individual":
    st.title("🔍 Prediksi Individual — Input Manual")
    st.caption("Masukkan skor 7 Factor Scales mahasiswa untuk memprediksi profil kepribadiannya.")

    if model is None:
        st.error("❌ Model belum tersedia. Jalankan notebook terlebih dahulu.")
        st.stop()

    st.divider()

    st.info("""
    📊 **Input: 7 Factor Scales (T-Score)**
    Rentang nilai T-Score: 20 - 90
    """)

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

        st.subheader("📏 Skor 7 Factor Scales (T-Score)")
        
        scale_labels = {
            'Sc_Agreeableness': 'Agreeableness (Kemudahan Bergaul)',
            'Sc_Conscientiousness': 'Conscientiousness (Keteraturan)',
            'Sc_Extraversion': 'Extraversion (Ekstraversi)',
            'Sc_Narcissism': 'Narcissism (Narsisme)',
            'Sc_Neuroticism': 'Neuroticism (Neurotisisme)',
            'Sc_Openness': 'Openness (Keterbukaan)',
            'Sc_SensationSeeking': 'Sensation Seeking (Pencarian Sensasi)'
        }

        scale_values = {}
        cols = st.columns(4)
        for i, scale in enumerate(BROAD_SCALES):
            with cols[i % 4]:
                label = scale_labels.get(scale, scale.replace('Sc_', ''))
                scale_values[scale] = st.number_input(
                    label, 20.0, 90.0, 50.0, 1.0, key=f"sc_{i}"
                )

        submitted = st.form_submit_button("🔮 Prediksi Profil", use_container_width=True)

    if submitted:
        input_arr = np.array([[scale_values[c] for c in BROAD_SCALES]])
        input_scaled = scaler.transform(input_arr)

        pred_label = model.predict(input_scaled)[0]
        pred_proba = model.predict_proba(input_scaled)[0]
        pred_name = prof_map[pred_label]['label']
        cfg = get_profile_config(pred_name)

        st.divider()
        st.subheader("🎯 Hasil Prediksi")

        render_profile_card(pred_name, 1, 1, cfg)

        st.markdown("**📊 Probabilitas Keanggotaan per Profil:**")
        prob_cols = st.columns(len(prof_map))
        for i, (pid, info) in enumerate(prof_map.items()):
            pname = info['label']
            pcfg = get_profile_config(pname)
            with prob_cols[i]:
                pct = pred_proba[pid] * 100
                st.metric(
                    f"{pcfg['icon']} {pcfg['label_short']}",
                    f"{pct:.1f}%"
                )

        st.divider()
        st.subheader("💡 Rekomendasi Intervensi")
        for rec in cfg['rekomendasi']:
            st.markdown(f"- {rec}")

        if pred_name == 'The Vulnerable / At-Risk':
            st.warning(
                "⚠️ **Prioritas tinggi.** Kelompok ini memerlukan intervensi "
                "selektif dan indikasi segera. Koordinasikan dengan unit konseling."
            )

# ==========================================================
# PAGE: ANALISIS & INSIGHT
# ==========================================================
elif page == "📈 Analisis & Insight":
    st.title("📈 Analisis & Insight — Distribusi Lintas Demografis")

    if model is None:
        st.error("❌ Model belum tersedia.")
        st.stop()

    df_data = load_labeled_dataset()

    if df_data is None:
        st.warning("⚠️ Dataset hasil labeling tidak ditemukan.")
        st.stop()

    st.caption(f"📌 Data: **{len(df_data):,}** mahasiswa dari dataset hasil training")

    st.divider()

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

    color_map = {name: get_profile_config(name)['color'] 
                 for name in df_data['Profile_Name'].unique()}

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

    st.divider()

    st.subheader("📊 Rata-rata Skor per Profil (Centroid)")
    centroids = df_data.groupby('Profile_Name')[BROAD_SCALES].mean().round(1)
    fig_centroid = px.imshow(
        centroids.T,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        aspect='auto',
        title='Rata-rata T-Score per Profil'
    )
    fig_centroid.update_layout(height=400)
    st.plotly_chart(fig_centroid, use_container_width=True)

# ==========================================================
# PAGE: REKOMENDASI INTERVENSI
# ==========================================================
elif page == "💡 Rekomendasi Intervensi":
    st.title("💡 Rekomendasi Intervensi Kesehatan Mental")
    st.caption(
        "Rekomendasi program intervensi dihasilkan berdasarkan karakteristik masing-masing "
        "profil kepribadian yang ditemukan oleh model LPA."
    )

    if model is None:
        st.error("❌ Model belum tersedia.")
        st.stop()

    st.divider()

    df_data = load_labeled_dataset()

    for pname in PROFILE_CONFIG.keys():
        cfg = PROFILE_CONFIG[pname]
        
        count = 0
        pct = 0
        if df_data is not None and 'Profile_Name' in df_data.columns:
            subset = df_data[df_data['Profile_Name'] == pname]
            count = len(subset)
            pct = count / len(df_data) * 100 if len(df_data) > 0 else 0

        with st.expander(
            f"{cfg['icon']} **{cfg['label_short']}**"
            + (f" — {count} mahasiswa ({pct:.1f}%)" if df_data is not None else ""),
            expanded=(pct >= 20 if df_data is not None else False)
        ):
            col_desc, col_rec = st.columns([1, 1])

            with col_desc:
                st.markdown("**📌 Deskripsi Profil:**")
                st.info(cfg['deskripsi'])

                st.markdown(f"**📊 Kategori:** {cfg['kategori']}")

                st.markdown("**📊 Ciri Dominan:**")
                traits_up = ", ".join(cfg.get('traits_tinggi', []))
                traits_dn = ", ".join(cfg.get('traits_rendah', []))
                st.markdown(f"- 🔺 **Tinggi:** {traits_up}")
                st.markdown(f"- 🔻 **Rendah:** {traits_dn}")

                if df_data is not None and count > 0:
                    st.markdown("**📍 Sebaran per Fakultas:**")
                    mini = subset['Fakultas'].value_counts().reset_index()
                    mini.columns = ['Fakultas', 'n']
                    fig_mini = px.bar(mini, x='Fakultas', y='n',
                                     title=f'Sebaran {cfg["label_short"]} per Fakultas',
                                     color_discrete_sequence=[cfg['color']])
                    fig_mini.update_layout(height=260, showlegend=False,
                                          margin=dict(t=35, b=0, l=0, r=0))
                    st.plotly_chart(fig_mini, use_container_width=True)

            with col_rec:
                st.markdown("**🎯 Rekomendasi Program Intervensi:**")
                for rec in cfg['rekomendasi']:
                    st.markdown(f"- {rec}")

                if pname == 'The Vulnerable / At-Risk':
                    st.warning(
                        "⚠️ **Prioritas tinggi.** Kelompok ini memerlukan intervensi "
                        "selektif dan indikasi segera. Koordinasikan dengan unit konseling."
                    )
                elif pname == 'The Energetic & Socially Active':
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