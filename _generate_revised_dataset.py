"""
Script untuk merevisi dataset_omni_dummy.csv sesuai proposal Bab 3
- Rename semua kolom ke format Bab 3 (Sc_ prefix, Val_ prefix)
- Ubah VRIN/CD ke T-Score: 90% normal (40-60), 10% invalid (70-85)
- Tambahkan 7 Skala Faktor baru

=== CARA MENJALANKAN ===
Buka terminal/cmd di folder repository, lalu jalankan:
    python _generate_revised_dataset.py

Pastikan file dataset_omni_dummy.csv ada di folder yang sama.
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# ============================================================
# 1. Load dataset lama
# ============================================================
df = pd.read_csv('dataset_omni_dummy.csv')
print(f"Dataset lama: {df.shape[0]} baris, {df.shape[1]} kolom")
print(f"Kolom lama: {list(df.columns)}")

# ============================================================
# 2. Rename kolom sesuai Bab 3
# ============================================================
rename_map = {
    'VRIN_Score': 'Val_VRIN',
    'CD_Score': 'Val_CD',
    'ScAestheticism': 'Sc_Aestheticism',
    'ScAmbition': 'Sc_Ambition',
    'ScAnxiety': 'Sc_Anxiety',
    'ScAssertiveness': 'Sc_Assertiveness',
    'ScConventionality': 'Sc_Conventionality',
    'ScDepression': 'Sc_Depression',
    'ScDutifulness': 'Sc_Dutifulness',
    'ScEnergy': 'Sc_Energy',
    'ScExcitement': 'Sc_Excitement',
    'ScExhibitionism': 'Sc_Exhibitionism',
    'ScFlexibility': 'Sc_Flexibility',
    'ScHostility': 'Sc_Hostility',
    'ScImpulsiveness': 'Sc_Impulsiveness',
    'ScIntellect': 'Sc_Intellect',
    'ScIrritability': 'Sc_Irritability',
    'ScModesty': 'Sc_Modesty',
    'ScMoodiness': 'Sc_Moodiness',
    'ScOrderliness': 'Sc_Orderliness',
    'ScSelfIndulgence': 'Sc_SelfIndulgence',
    'ScSelfReliance': 'Sc_SelfReliance',
    'ScSincerity': 'Sc_Sincerity',
    'ScSociability': 'Sc_Sociability',
    'ScTolerance': 'Sc_Tolerance',
    'ScTrustfulness': 'Sc_Trustfulness',
    'ScWarmth': 'Sc_Warmth',
    'ScParanoid': 'Sc_Paranoid',
    'ScSchizoid': 'Sc_Schizoid',
    'ScSchizotypal': 'Sc_Schizotypal',
    'ScAntisocial': 'Sc_Antisocial',
    'ScBorderline': 'Sc_Borderline',
    'ScHistrionic': 'Sc_Histrionic',
    'ScNarcissistic': 'Sc_Narcissistic',
    'ScAvoidant': 'Sc_Avoidant',
    'ScDependent': 'Sc_Dependent',
    'ScObsessiveCompulsive': 'Sc_ObsessiveCompulsive',
}

df = df.rename(columns=rename_map)
print(f"\nKolom setelah rename: {list(df.columns)}")

# ============================================================
# 3. Ubah Val_VRIN & Val_CD ke T-Score
# ============================================================
n_rows = len(df)
n_invalid = max(int(n_rows * 0.10), 8)  # ~10% tapi minimal 8 baris
n_normal = n_rows - n_invalid

# Buat index untuk baris invalid (careless responding)
invalid_indices = np.random.choice(n_rows, size=n_invalid, replace=False)
normal_indices = np.array([i for i in range(n_rows) if i not in invalid_indices])

print(f"\nTotal baris: {n_rows}")
print(f"Baris normal (VRIN/CD 40-60): {len(normal_indices)} ({len(normal_indices)/n_rows*100:.1f}%)")
print(f"Baris invalid (VRIN/CD 70-85): {len(invalid_indices)} ({len(invalid_indices)/n_rows*100:.1f}%)")

# Generate VRIN T-Scores
vrin_values = np.zeros(n_rows)
vrin_values[normal_indices] = np.random.uniform(40, 60, size=len(normal_indices)).round(1)
vrin_values[invalid_indices] = np.random.uniform(70, 85, size=len(invalid_indices)).round(1)
df['Val_VRIN'] = vrin_values

# Generate CD T-Scores
cd_values = np.zeros(n_rows)
cd_values[normal_indices] = np.random.uniform(40, 60, size=len(normal_indices)).round(1)
# Some invalid rows have high VRIN only, some have high CD only, some have both
# Make ~60% of invalid rows have high CD too, rest have normal CD
n_invalid_cd = int(n_invalid * 0.6)
invalid_cd_indices = np.random.choice(invalid_indices, size=n_invalid_cd, replace=False)
invalid_cd_normal = np.array([i for i in invalid_indices if i not in invalid_cd_indices])
cd_values[invalid_cd_indices] = np.random.uniform(70, 85, size=len(invalid_cd_indices)).round(1)
cd_values[invalid_cd_normal] = np.random.uniform(40, 60, size=len(invalid_cd_normal)).round(1)
# Also add some normal-VRIN rows with high CD
n_extra_cd_invalid = max(int(n_rows * 0.03), 4)
extra_cd_indices = np.random.choice(normal_indices, size=n_extra_cd_invalid, replace=False)
cd_values[extra_cd_indices] = np.random.uniform(70, 85, size=len(extra_cd_indices)).round(1)
df['Val_CD'] = cd_values

# Verify
print(f"\nVal_VRIN >= 70: {(df['Val_VRIN'] >= 70).sum()} baris")
print(f"Val_CD >= 70: {(df['Val_CD'] >= 70).sum()} baris")
print(f"Val_VRIN >= 70 OR Val_CD >= 70: {((df['Val_VRIN'] >= 70) | (df['Val_CD'] >= 70)).sum()} baris")

# ============================================================
# 4. Tambahkan 7 Skala Faktor
# ============================================================
# Generate Factor Scale T-Scores dengan distribusi realistis
# Menggunakan distribusi normal yang di-clip ke 20-90
# Mean ~ 50, Std ~ 10 (typical T-Score distribution)

factor_scales = {
    'Sc_Agreeableness': {
        # Correlated positively with Warmth, Trustfulness, Tolerance
        'base_cols': ['Sc_Warmth', 'Sc_Trustfulness', 'Sc_Tolerance'],
        'noise_std': 5
    },
    'Sc_Conscientiousness': {
        # Correlated positively with Dutifulness, Orderliness, Ambition
        'base_cols': ['Sc_Dutifulness', 'Sc_Orderliness', 'Sc_Ambition'],
        'noise_std': 5
    },
    'Sc_Extraversion': {
        # Correlated positively with Sociability, Energy, Excitement
        'base_cols': ['Sc_Sociability', 'Sc_Energy', 'Sc_Excitement'],
        'noise_std': 5
    },
    'Sc_Narcissism': {
        # Correlated positively with Exhibitionism, Narcissistic, Assertiveness
        'base_cols': ['Sc_Exhibitionism', 'Sc_Narcissistic', 'Sc_Assertiveness'],
        'noise_std': 6
    },
    'Sc_Neuroticism': {
        # Correlated positively with Anxiety, Depression, Moodiness
        'base_cols': ['Sc_Anxiety', 'Sc_Depression', 'Sc_Moodiness'],
        'noise_std': 5
    },
    'Sc_Openness': {
        # Correlated positively with Aestheticism, Intellect, Flexibility
        'base_cols': ['Sc_Aestheticism', 'Sc_Intellect', 'Sc_Flexibility'],
        'noise_std': 5
    },
    'Sc_SensationSeeking': {
        # Correlated positively with Impulsiveness, Excitement, SelfIndulgence
        'base_cols': ['Sc_Impulsiveness', 'Sc_Excitement', 'Sc_SelfIndulgence'],
        'noise_std': 5
    },
}

for fc_name, fc_config in factor_scales.items():
    # Calculate weighted average of base columns + noise
    base_vals = df[fc_config['base_cols']].mean(axis=1)
    noise = np.random.normal(0, fc_config['noise_std'], size=n_rows)
    raw_values = (base_vals + noise).round(1)
    # Clip to valid T-Score range
    df[fc_name] = raw_values.clip(20.0, 90.0)

# Add some missing values to factor scales (~2-3% per column)
for fc_name in factor_scales.keys():
    n_missing = int(n_rows * np.random.uniform(0.01, 0.03))
    missing_idx = np.random.choice(n_rows, size=n_missing, replace=False)
    df.loc[missing_idx, fc_name] = np.nan

print(f"\n7 Skala Faktor ditambahkan:")
for fc_name in factor_scales.keys():
    n_valid = df[fc_name].notna().sum()
    n_miss = df[fc_name].isna().sum()
    print(f"  {fc_name}: mean={df[fc_name].mean():.1f}, "
          f"std={df[fc_name].std():.1f}, "
          f"valid={n_valid}, missing={n_miss}")

# ============================================================
# 5. Reorder kolom sesuai Bab 3
# ============================================================
demog_cols = ['Student_ID', 'Gender', 'Fakultas', 'Program_Studi', 'Angkatan']
validity_cols = ['Val_VRIN', 'Val_CD']
normal_cols = [
    'Sc_Aestheticism', 'Sc_Ambition', 'Sc_Anxiety', 'Sc_Assertiveness',
    'Sc_Conventionality', 'Sc_Depression', 'Sc_Dutifulness', 'Sc_Energy',
    'Sc_Excitement', 'Sc_Exhibitionism', 'Sc_Flexibility', 'Sc_Hostility',
    'Sc_Impulsiveness', 'Sc_Intellect', 'Sc_Irritability', 'Sc_Modesty',
    'Sc_Moodiness', 'Sc_Orderliness', 'Sc_SelfIndulgence', 'Sc_SelfReliance',
    'Sc_Sincerity', 'Sc_Sociability', 'Sc_Tolerance', 'Sc_Trustfulness',
    'Sc_Warmth'
]
pd_cols = [
    'Sc_Paranoid', 'Sc_Schizoid', 'Sc_Schizotypal', 'Sc_Antisocial',
    'Sc_Borderline', 'Sc_Histrionic', 'Sc_Narcissistic', 'Sc_Avoidant',
    'Sc_Dependent', 'Sc_ObsessiveCompulsive'
]
factor_cols = [
    'Sc_Agreeableness', 'Sc_Conscientiousness', 'Sc_Extraversion',
    'Sc_Narcissism', 'Sc_Neuroticism', 'Sc_Openness', 'Sc_SensationSeeking'
]

all_cols = demog_cols + validity_cols + normal_cols + pd_cols + factor_cols
df = df[all_cols]

print(f"\nDataset baru: {df.shape[0]} baris, {df.shape[1]} kolom")
print(f"Kolom: {list(df.columns)}")

# ============================================================
# 6. Save
# ============================================================
df.to_csv('dataset_omni_dummy.csv', index=False)
print(f"\n✅ Dataset berhasil disimpan: dataset_omni_dummy.csv")

# Verification summary
print("\n" + "="*60)
print("RINGKASAN VERIFIKASI")
print("="*60)
print(f"Total baris: {len(df)}")
print(f"Total kolom: {len(df.columns)}")
print(f"  - Demografis: {len(demog_cols)}")
print(f"  - Validitas: {len(validity_cols)}")
print(f"  - Kepribadian Normal: {len(normal_cols)}")
print(f"  - Gangguan Kepribadian: {len(pd_cols)}")
print(f"  - Faktor: {len(factor_cols)}")
print(f"\nVal_VRIN range: {df['Val_VRIN'].min():.1f} - {df['Val_VRIN'].max():.1f}")
print(f"Val_CD range: {df['Val_CD'].min():.1f} - {df['Val_CD'].max():.1f}")
print(f"Baris dengan Val_VRIN >= 70: {(df['Val_VRIN'] >= 70).sum()}")
print(f"Baris dengan Val_CD >= 70: {(df['Val_CD'] >= 70).sum()}")
print(f"Baris careless (VRIN>=70 OR CD>=70): {((df['Val_VRIN'] >= 70) | (df['Val_CD'] >= 70)).sum()}")
missing_total = df.isnull().sum().sum()
print(f"Total missing values: {missing_total}")
