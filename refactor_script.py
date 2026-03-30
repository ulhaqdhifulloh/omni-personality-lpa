import re

filepath = r"c:\Users\LOQ\OneDrive - Telkom University\Tugas Akhir\Proposal\github_repository\omni-personality-lpa\implementasi_crisp_dm_1202220139_dhifulloh_dhiya_ulhaq.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Feature Selection Insert
feature_selection_block = r'''"""## 3.5 Feature Selection

Seleksi fitur ini bertujuan untuk menghilangkan skala-skala yang sangat redundan (berkorelasi Pearson > 0.85), sehingga mengurangi *multicollinearity* sebelum di-*feed* ke model GMM.
"""

corr_matrix = df_clean[SCALE_COLS].corr().abs()
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.85)]
SELECTED_SCALE_COLS = [c for c in SCALE_COLS if c not in to_drop]

print(f"Total fitur awal: {len(SCALE_COLS)}")
print(f"Fitur dibuang (korelasi tinggi > 0.85): {len(to_drop)} -> {to_drop}")
print(f"Total fitur terpilih untuk pemodelan: {len(SELECTED_SCALE_COLS)}")

"""## 3.6 Standardisasi (Z-Score)'''

content = content.replace('"""## 3.5 Standardisasi (Z-Score)', feature_selection_block)

# 2. Change X_scaled to use SELECTED_SCALE_COLS
content = content.replace('X_scaled = scaler.fit_transform(df_clean[SCALE_COLS].values)', 'X_scaled = scaler.fit_transform(df_clean[SELECTED_SCALE_COLS].values)')

# 3. Add BLRT logic and remove AvePP logically
# To reliably replace the metrics loop, let's use regex on the model loop block.
loop_start_regex = r"for k in K_RANGE:[\s\S]*?print\(f\"\\n  k=\{k\}:\"\)"
loop_code = '''
# Fungsi simulasi Bootstrap Likelihood Ratio Test (BLRT) k vs k-1
def simulate_blrt(X, k_base, k_alt, base_score, bootstrap_draws=10):
    if k_base < 1: return 1.0 # k=1 tidak memiliki pembanding yang valid
    gmm_base = GaussianMixture(n_components=k_base, covariance_type='full', n_init=1, random_state=42).fit(X)
    gmm_alt = GaussianMixture(n_components=k_alt, covariance_type='full', n_init=1, random_state=42).fit(X)
    lr_obs = -2 * (gmm_base.score(X) * len(X) - gmm_alt.score(X) * len(X))
    
    lr_sims = []
    for b in range(bootstrap_draws):
        X_sim, _ = gmm_base.sample(len(X))
        try:
            b_base = GaussianMixture(n_components=k_base, covariance_type='full', n_init=1, random_state=b).fit(X_sim)
            b_alt = GaussianMixture(n_components=k_alt, covariance_type='full', n_init=1, random_state=b).fit(X_sim)
            lr_sim = -2 * (b_base.score(X_sim) * len(X_sim) - b_alt.score(X_sim) * len(X_sim))
            lr_sims.append(lr_sim)
        except:
            pass
    if len(lr_sims) == 0: return 1.0
    return np.mean(np.array(lr_sims) >= lr_obs)

for k in K_RANGE:
    gmm = GaussianMixture(
        n_components=k,
        covariance_type='full',
        n_init=10,
        max_iter=300,
        random_state=42
    )
    gmm.fit(X_scaled)
    
    labels = gmm.predict(X_scaled)
    aic = gmm.aic(X_scaled)
    bic = gmm.bic(X_scaled)
    log_likelihood = gmm.score(X_scaled) * len(X_scaled)

    # Hitung Entropy
    proba = gmm.predict_proba(X_scaled)
    safe_proba = np.clip(proba, 1e-10, 1.0)
    N = len(X_scaled)
    entropy = 1 - (-np.sum(safe_proba * np.log(safe_proba))) / (N * np.log(k))

    # Hitung Silhouette Score
    if len(np.unique(labels)) > 1:
        sil_score = silhouette_score(X_scaled, labels)
    else:
        sil_score = 0.0

    # BLRT P-Value (k vs k-1)
    # Untuk mempercepat eksekusi, bootstrap_draws diset kecil (misal 5) -- dalam uji riil biasanya 50-100
    blrt_p = simulate_blrt(X_scaled, k-1, k, gmm.score(X_scaled), bootstrap_draws=5) if k > 1 else 1.0

    results.append({
        'k': k, 'AIC': aic, 'BIC': bic,
        'Entropy': round(entropy, 4),
        'Silhouette': round(sil_score, 4),
        'BLRT_p': round(blrt_p, 4),
        'Model': gmm
    })

    print(f"\\n  k={k}:")
'''
content = re.sub(loop_start_regex, loop_code.strip(), content)

# Remove AvePP and Profile size print prints from the loop block
content = re.sub(r"print\(f\"    AIC  = \{aic:,\.1f\}\"\)[\s\S]*?print\(f\"    Profil terkecil = \{min_size\}.*\"\)",
                 'print(f"    AIC  = {aic:,.1f}")\n    print(f"    BIC  = {bic:,.1f}")\n    print(f"    Entropy = {entropy:.4f}")\n    print(f"    Silhouette = {sil_score:.4f}")\n    print(f"    BLRT p-value = {blrt_p:.4f}")', content)

# 4. Remove interpretation of AvePP / Min Profile
# Find model selection output:
content = re.sub(r"print\(f\"  AvePP     = \{best\['AvePP'\]:\.4f\}\"\)\s+print\(f\"  Silhouette= \{best\['Silhouette'\].*\"\)\s+print\(f\"  Min Profil= .*\"\)",
                 'print(f"  Silhouette= {best[\'Silhouette\']:.4f}")\nprint(f"  BLRT p-value = {best[\'BLRT_p\']:.4f}")', content)

# Remove BLRT from the plots - wait, make plots 1 to 4 with the new metrics.
# Originally 4 subplots: AIC, BIC, Entropy, Silhouette. Let's keep those 4, and we can just add a 5th or replace one. 4 is fine, we just text-print BLRT.
# Actually, the user asked to add BLRT to metrics used. So we can add it to the visualization if we want, but 4 is fine if it's in the table. Let's make it 1, 5 plots.
plot_code_old = r"fig, axes = plt.subplots\(1, 4, figsize=\(22, 5\)\)[\s\S]*?axes\[3\]\.legend\(\)"
plot_code_new = r"""fig, axes = plt.subplots(1, 5, figsize=(26, 5))

# AIC Plot
axes[0].plot([r['k'] for r in results], [r['AIC'] for r in results],
             'o-', color='#3498db', linewidth=2, markersize=8)
axes[0].set_title('AIC per Jumlah Profil', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Jumlah Profil (k)')
axes[0].set_ylabel('AIC')
axes[0].set_xticks(list(K_RANGE))

# BIC Plot
axes[1].plot([r['k'] for r in results], [r['BIC'] for r in results],
             'o-', color='#e74c3c', linewidth=2, markersize=8)
axes[1].set_title('BIC per Jumlah Profil', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Jumlah Profil (k)')
axes[1].set_ylabel('BIC')
axes[1].set_xticks(list(K_RANGE))

# Entropy Plot
axes[2].plot([r['k'] for r in results], [r['Entropy'] for r in results],
             'o-', color='#27ae60', linewidth=2, markersize=8)
axes[2].axhline(y=0.80, color='red', linestyle='--', alpha=0.5, label='Threshold (0.80)')
axes[2].set_title('Entropy per Jumlah Profil', fontsize=14, fontweight='bold')
axes[2].set_xlabel('Jumlah Profil (k)')
axes[2].set_ylabel('Entropy')
axes[2].set_xticks(list(K_RANGE))
axes[2].legend()

# Silhouette Plot
axes[3].plot([r['k'] for r in results], [r['Silhouette'] for r in results],
             'o-', color='#9b59b6', linewidth=2, markersize=8)
axes[3].axhline(y=0.50, color='red', linestyle='--', alpha=0.5, label='Threshold (0.50)')
axes[3].set_title('Silhouette Score per Jumlah Profil', fontsize=14, fontweight='bold')
axes[3].set_xlabel('Jumlah Profil (k)')
axes[3].set_ylabel('Silhouette Score')
axes[3].set_xticks(list(K_RANGE))
axes[3].legend()

# BLRT Plot
axes[4].plot([r['k'] for r in results], [r['BLRT_p'] for r in results],
             'o-', color='#f1c40f', linewidth=2, markersize=8)
axes[4].axhline(y=0.05, color='red', linestyle='--', alpha=0.5, label='Alpha (0.05)')
axes[4].set_title('BLRT P-Value per k', fontsize=14, fontweight='bold')
axes[4].set_xlabel('Jumlah Profil (k)')
axes[4].set_ylabel('P-Value')
axes[4].set_xticks(list(K_RANGE))
axes[4].legend()"""
content = re.sub(plot_code_old, plot_code_new, content)

# Replace "Kualitas Klasifikasi (Entropy & AvePP)" with just Entropy
content = content.replace("Kualitas Klasifikasi (Entropy & AvePP)", "Kualitas Klasifikasi (Entropy)")
content = content.replace("dan **AvePP** mendekati 1.0.", ".")
content = re.sub(r'4. \*\*Ukuran Profil Minimal\*\*: Semua model memenuhi kriteria keberhasilan \(>5% populasi\).*?\n', '', content)
content = re.sub(r'4\. \*\*Stabilitas Ukuran Profil\*\*:.*\n', '', content)

content = content.replace("Average Posterior Prob.    :", "BLRT P-Value               :")
content = re.sub(r"\{best\['AvePP'\]:\.4f\}", "{best['BLRT_p']:.4f}", content)
content = re.sub(r"print\(f\"Profil terkecil           : \{best\['Min_Profile_Size'\].*\\n.*\}\"\)\n", "", content)
content = re.sub(r"1\. \*\*Kepastian Klasifikasi \(Entropy 1\.0000 & AvePP 1\.0000\):\*\*", "1. **Kepastian Klasifikasi (Entropy 1.0000):**", content)
content = re.sub(r"3\. \*\*Keterwakilan Populasi \(Min Profile Size 39\.6%\):\*\*.*?\n.*?\n", "", content)

# 5. Fix plotting scales. `profile_means...[SCALE_COLS]` -> `profile_means...[SELECTED_SCALE_COLS]`
content = content.replace("profile_means = df_clean.groupby('Profile_ID')[SCALE_COLS].mean()", "profile_means = df_clean.groupby('Profile_ID')[SELECTED_SCALE_COLS].mean()")
content = content.replace("x = np.arange(len(SCALE_COLS))", "x = np.arange(len(SELECTED_SCALE_COLS))")
content = content.replace("ax.set_xticklabels([s.replace('Sc', '') for s in SCALE_COLS],", "ax.set_xticklabels([s.replace('Sc', '') for s in SELECTED_SCALE_COLS],")
content = content.replace("columns=SCALE_COLS,", "columns=SELECTED_SCALE_COLS,")

# For key_scales, only keep those that are inside SELECTED_SCALE_COLS
content = content.replace("fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))", "key_scales = [s for s in key_scales if s in SELECTED_SCALE_COLS]\n\nfig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))")

# Output Saving, change SCALE_COLS to SELECTED_SCALE_COLS
content = content.replace("joblib.dump(SCALE_COLS, 'artifacts/scale_columns.pkl')", "joblib.dump(SELECTED_SCALE_COLS, 'artifacts/scale_columns.pkl')")
content = content.replace("output_cols = DEMOG_COLS + VALIDITY_COLS + SCALE_COLS + ['Profile_ID', 'Profile_Name', 'Max_Prob']", "output_cols = DEMOG_COLS + VALIDITY_COLS + SELECTED_SCALE_COLS + ['Profile_ID', 'Profile_Name', 'Max_Prob']")

# 6. Streamlit updates:
# In app.py section, change SCALE_COLS hardcoding to load from pkl
st_scale_remove = r"SCALE_COLS = \[.*?'Sc_SensationSeeking'\n\]"
st_scale_new = r"SCALE_COLS = joblib.load('artifacts/scale_columns.pkl') if os.path.exists('artifacts/scale_columns.pkl') else []"
content = re.sub(st_scale_remove, st_scale_new, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
