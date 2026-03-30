**PROPOSAL TUGAS AKHIR**

**PEMETAAN PROFIL KEPRIBADIAN MAHASISWA PADA DATA OMNI MELALUI *LATENT PROFILE ANALYSIS* (LPA) UNTUK REKOMENDASI INTERVENSI KESEHATAN MENTAL BERBASIS DATA**

**Oleh:**

**DHIFULLOH DHIYA ULHAQ**

**1202220139**

<img src="media/image1.jpg" style="width:1.5367in;height:2.22917in" alt="BP3SIEBCIAInFJY" />

**PROGRAM STUDI STRATA 1 SISTEM INFORMASI**

**FAKULTAS REKAYASA INDUSTRI**

**UNIVERSITAS TELKOM**

**2025**

# ABSTRAK

Eskalasi gangguan psikologis mahasiswa pasca-pandemi telah menjadi isu krusial yang sering kali terlambat dideteksi akibat kurangnya pemanfaatan data asesmen psikologis secara efektif. Meskipun institusi pendidikan memiliki data *OMNI Personality Inventory* (OMNI), pemanfaatannya belum optimal karena tingginya kompleksitas dimensi kepribadian multidimensional yang memerlukan analisis manual dan keahlian khusus, sehingga strategi intervensi cenderung lambat dan reaktif. Penelitian ini bertujuan mengembangkan sistem pendukung keputusan berbasis data yang menerapkan pendekatan *person-centered* untuk memetakan profil kepribadian mahasiswa secara otomatis dan massal guna mendukung perancangan intervensi kesehatan mental yang tepat sasaran. Mengacu pada kerangka kerja CRISP-DM, metode penelitian ini menggunakan *Latent Profile Analysis* (LPA) berbasis algoritma *Gaussian Mixture Model* (GMM). Tahapan penyelesaian masalah dimulai dari validasi kualitas data menggunakan indikator *Variable Response Inconsistency* (VRIN) dan *Current Distress* (CD), pra-pemrosesan skor skala, serta *measurement invariance testing* untuk memastikan kesetaraan pengukuran lintas kelompok demografis. Evaluasi model dilakukan menggunakan metrik statistik *Akaike Information Criterion* (AIC), *Bayesian Information Criterion* (BIC), *Entropy*, dan metrik tambahan *Silhouette Score* untuk memvalidasi struktur klaster profil yang terbentuk. Hasil utama yang ditargetkan adalah terbentuknya struktur profil kepribadian laten mahasiswa serta peta distribusi risiko lintas demografis yang disajikan dalam *dashboard* visual interaktif. Kontribusi ilmiah penelitian ini terletak pada transformasi analisis psikometrik yang subjektif menjadi wawasan objektif yang dapat ditindaklanjuti (*actionable insights*), sehingga memfasilitasi pemangku kepentingan dalam merumuskan rekomendasi program kesehatan mental dan akademik yang berbasis bukti serta responsif terhadap kebutuhan spesifik setiap kelompok mahasiswa.

Kata Kunci: Kesehatan Mental Mahasiswa, *Latent Profile Analysis*, *OMNI Personality Inventory*, *Gaussian Mixture Model*, Sistem Pendukung Keputusan.

# ABSTRACT

The post-pandemic escalation of psychological disorders among students has become a crucial issue that is often detected late due to the ineffective utilization of psychological assessment data. Although educational institutions possess OMNI Personality Inventory (OMNI) data, its utilization remains suboptimal due to the high complexity of multidimensional personality dimensions, which require manual analysis and specialized expertise, making intervention strategies slow and reactive. This study aims to develop a data-driven decision support system applying a person-centered approach to automatically map students' personality profiles on a large scale to support the design of targeted mental health interventions. Guided by the CRISP-DM framework, this research methodology employs Latent Profile Analysis (LPA) based on the Gaussian Mixture Model (GMM) algorithm. The problem-solving stages begin with data quality validation using Variable Response Inconsistency (VRIN) and Current Distress (CD) indicators, scale score preprocessing, and measurement invariance testing to ensure measurement equivalence across demographic groups. Model evaluation is conducted using statistical metrics such as Akaike Information Criterion (AIC), Bayesian Information Criterion (BIC), Entropy, and the supplementary Silhouette Score metric to validate the structural cohesion of the formed profile clusters. The primary expected outcome is the formation of students' latent personality profile structure and a cross-demographic risk distribution map presented in an interactive visual dashboard. The scientific contribution of this study lies in the transformation of subjective psychometric analysis into objective, actionable insights, thereby facilitating stakeholders in formulating evidence-based mental health and academic program recommendations that are responsive to the specific needs of each student group.

Keywords: Student Mental Health, Latent Profile Analysis, OMNI Personality Inventory, Gaussian Mixture Model, Decision Support System.

# DAFTAR ISI

[ABSTRAK ](#abstrak)

[ABSTRACT ](#abstract)

[DAFTAR ISI ](#daftar-isi)

[DAFTAR GAMBAR ](#daftar-gambar)

[DAFTAR TABEL ](#daftar-tabel)

[DAFTAR ISTILAH ](#daftar-istilah)

[DAFTAR SINGKATAN ](#daftar-singkatan)

[DAFTAR SIMBOL ](#daftar-simbol)

[Bab I PENDAHULUAN ](#pendahuluan)

[I.1 Latar Belakang ](#latar-belakang)

[I.2 Rumusan Masalah ](#rumusan-masalah)

[I.3 Tujuan Penelitian ](#tujuan-penelitian)

[I.4 Batasan Penelitian ](#batasan-penelitian)

[I.5 Manfaat Penelitian ](#manfaat-penelitian)

[I.6 Sistematika Penulisan ](#sistematika-penulisan)

[Bab II TINJAUAN PUSTAKA ](#tinjauan-pustaka)

[II.1 Dasar Teori ](#dasar-teori)

[II.1.1 Kesehatan Mental Mahasiswa ](#kesehatan-mental-mahasiswa)

[II.1.2 OMNI ](#omni)

[II.1.3 *Data Mining* ](#data-mining)

[II.1.4 *Machine Learning* ](#machine-learning)

[II.1.5 *Clustering* ](#clustering)

[II.1.6 *Latent Profile Analysis* (LPA) ](#latent-profile-analysis-lpa)

[II.1.7 *Measurement Invariance* ](#measurement-invariance)

[II.1.8 *Decision Support System* ](#decision-support-system)

[II.2 Penelitian Terdahulu *(State of the Art)* ](#penelitian-terdahulu-state-of-the-art)

[Bab III METODE PENYELESAIAN MASALAH ](#metode-penyelesaian-masalah)

[III.1 Metode Penelitian ](#metode-penelitian)

[III.2 Sistematika Penyelesaian Masalah ](#sistematika-penyelesaian-masalah)

[III.2.1 Tahap 1: *Business Understanding* ](#tahap-1-business-understanding)

[III.2.2 Tahap 2: *Data Understanding* ](#tahap-2-data-understanding)

[III.2.3 Tahap 3: *Data Preparation* ](#tahap-3-data-preparation)

[III.2.4 Tahap 4: *Modeling* ](#tahap-4-modeling)

[III.2.5 Tahap 5: *Evaluation* ](#tahap-5-evaluation)

[III.2.6 Tahap 6: *Deployment* ](#tahap-6-deployment)

[III.3 Metode Pengumpulan data dan Pengolahan Data ](#metode-pengumpulan-data-dan-pengolahan-data)

[III.4 Metode Evaluasi ](#metode-evaluasi)

[DAFTAR PUSTAKA ](#daftar-pustaka)

# DAFTAR GAMBAR

[Gambar II‑1 Siklus Kerangka Kerja CRISP-DM ](#_Toc225768968)

[Gambar II‑2 Perbandingan *Hard Clustering* (K-Means) dan *Soft Clustering* (LPA) ](#_Toc225768969)

[Gambar II‑3 *Flowchart* algoritma EM ](#_Toc225768970)

[Gambar II‑4 Contoh visualisasi *profile* *means* dari *Latent Profile Analysis* pada studi *mental health risk profiling* ](#_Toc225768971)

[Gambar II‑5 Contoh *Elbow Plot* untuk Pemilihan Jumlah Profil Optimal ](#_Toc225768972)

[Gambar II‑6 Hierarki Tingkat *Measurement Invariance* dalam CFA *Multi-Group* ](#_Toc225768973)

[Gambar III‑1 *Flowchart* Tahapan Penelitian ](#_Toc225768974)

# DAFTAR TABEL

[Tabel I‑1 Prevalensi Gangguan Mental Mahasiswa Tahun Pertama (Lintas 18 Negara) ](#_Toc225768977)

[Tabel II‑1 Prevalensi Masalah Kesehatan Mental Remaja (10-17 Tahun) Menurut Jenis Kelamin dan Usia (12 Bulan Terakhir) ](#_Toc225768978)

[Tabel II‑2 Struktur Komponen *OMNI Personality Inventory* ](#_Toc225768979)

[Tabel II‑3 Posisi Penelitian (*State of The Art)* ](#_Toc225768980)

[Tabel III‑1 Kamus Data Variabel OMNI ](#_Toc225768981)

# DAFTAR ISTILAH

| Istilah | Deskripsi | Halaman Pertama Kali Digunakan |
|:--:|----|:--:|
| *Careless Responding* | Pola jawaban responden yang tidak konsisten atau asal-asalan, yang dalam penelitian ini dideteksi menggunakan skala validitas VRIN dan CD. | 52 |
| *Clustering* | Teknik analisis data *machine learning* untuk mengelompokkan sekumpulan objek ke dalam klaster berdasarkan kesamaan karakteristik secara *unsupervised*. | 16 |
| *Data Mining* | Proses mengekstraksi pola, pengetahuan, dan *insight* bermakna dari kumpulan data besar menggunakan teknik statistik dan algoritma *machine learning*. | 13 |
| *Decision Support System* | Sistem pendukung keputusan interaktif yang dirancang untuk mentransformasi analisis data statistik kompleks menjadi wawasan praktis (*actionable insight*). | 28 |
| *Digital Natives* | Kelompok individu (seperti Gen Z) yang lahir di era digital dan tumbuh dengan karakteristik unik dalam pemanfaatan teknologi. | 1 |
| *Expectation-Maximization* (EM) | Algoritma dasar yang bekerja secara iteratif untuk menemukan estimasi kemungkinan maksimum parameter dalam model GMM. | 20 |
| *Hard Clustering* | Pendekatan pengelompokan (seperti *K-Means*) secara kaku di mana setiap individu di-*assign* ke satu klaster dengan probabilitas absolut. | 17 |
| *Healthcare Analytics* (Analitik Kesehatan) | Penerapan analitik untuk mengekstrak wawasan dari data kesehatan guna mendukung keputusan berbasis bukti. | 4 |
| *Latent Profile Analysis* (LPA) | Metode statistik *person-centered* untuk mengekstrak profil atau segmen laten dari data guna mengidentifikasi subgrup individu dengan pola karakteristik serupa. | 4 |
| *Machine Learning* | Cabang dari *artificial intelligence* yang memungkinkan sistem belajar dan mengidentifikasi pola dari pengalaman data tanpa diprogram secara eksplisit. | 13 |
| *Measurement Invariance* | Kondisi/asumsi fundamental statistik di mana instrumen pengukuran berfungsi secara setara dan tidak bias di berbagai kelompok demografis. | 5 |
| *New Normal* | Fase kehidupan transisi pasca-pandemi di mana gaya hidup digital dibaurkan dengan gaya hidup konvensional. | 1 |
| OMNI (*OMNI Personality Inventory*) | Instrumen asesmen kepribadian komprehensif yang terdiri dari 375 item untuk mengukur 25 skala normal, 10 skala gangguan kepribadian, dan 2 skala validitas. | 3 |
| *Person-Centered Approach* | Pendekatan analisis yang berfokus pada pengelompokan individu berdasarkan pola karakteristik keseluruhan mereka secara holistik. | 4 |
| *Responsible AI* | Pengembangan sistem AI yang transparan, adil (bebas bias demografis), memprioritaskan privasi, dan bertanggung jawab. | 42 |
| *Soft Clustering* | Pendekatan pengelompokan di mana setiap individu memiliki probabilitas keanggotaan di berbagai klaster (proporsional), bukan penugasan kaku,. | 18 |
| *Universal Prevention* | Strategi pencegahan atau intervensi kesehatan mental yang ditujukan untuk seluruh populasi (seperti seluruh mahasiswa) demi mempromosikan kesejahteraan umum. | 4 |
| *Unsupervised Learning* | Paradigma *machine learning* di mana sistem belajar menemukan struktur dari data tanpa adanya label (*ground truth*) sebelumnya. | 15 |
| *Variable-Centered Approach* | Pendekatan analisis kuantitatif (seperti regresi/korelasi) yang berfokus melihat hubungan antar-variabel satu sama lain. | 4 |

# DAFTAR SINGKATAN

| Singkatan | Deskripsi | Halaman Pertama Kali Digunakan |
|:--:|----|:--:|
| AIC | *Akaike Information Criterion* (Metrik statistik evaluasi model penyeimbang *goodness-of-fit*). | 5 |
| BIC | *Bayesian Information Criterion* (Metrik statistik yang memberi penalti ketat pada kompleksitas). | 5 |
| BLRT | *Bootstrapped Likelihood Ratio Test* (Uji statistik untuk membandingkan kecocokan jumlah profil). | 24 |
| CD | *Current Distress* (Skala validitas tekanan emosional pada OMNI). | 3 |
| CFA | *Confirmatory Factor Analysis* (Analisis faktor konfirmatori dalam uji invariansi). | 28 |
| CRISP-DM | *Cross-Industry Standard Process for Data Mining* (Kerangka kerja iteratif untuk proyek data). | 13 |
| DMHI | *Digital Mental Health Interventions* (Intervensi kesehatan mental berbasis digital). | 38 |
| DSM-IV | *Diagnostic and Statistical Manual of Mental Disorders, 4th Edition*. | 3 |
| DSS | *Decision Support System* (Sistem pendukung keputusan bagi pemangku kepentingan). | 28 |
| EM | *Expectation-Maximization* (Algoritma matematika estimasi log-likelihood model laten). | 20 |
| FFM | *Five Factor Model* (Teori dasar 5 sifat konseptual kepribadian). | 4 |
| GMM | *Gaussian Mixture Model* (Model distribusi probabilistik yang menjadi fondasi matematis LPA). | 19 |
| I-NAMHS | *Indonesia National Adolescent Mental Health Survey*. | 3 |
| LPA | *Latent Profile Analysis* (Teknik analitik person-centered identifikasi klaster/profil). | 4 |
| PAAI | *Psychological Assessment of AI-based Decision Support Systems* (Alat uji DSS). | 37 |
| PDP | Pelindungan Data Pribadi (*Catatan: Walau akronim PDP tidak tertulis langsung di teks, frasa "pelindungan data pribadi" diatur berdasarkan regulasi ada di Bab I*). | 7 |
| RCT | *Randomized Controlled Trial* (Metode studi eksperimental). | 33 |
| VRIN | *Variable Response Inconsistency* (Skala validitas pendeteksi inkonsistensi). | 3 |

# DAFTAR SIMBOL

| Simbol | Deskripsi | Halaman Pertama Kali Digunakan |
|:--:|----|:--:|
|$\mathcal{K}$| Jumlah kelas komponen atau klaster profil *Gaussian* dalam *mixture model*,. | 17 |
| $l$ atau $\mathcal{L}$ | Fungsi *Log-Likelihood* (Ukuran probabilitas kecocokan estimasi model terhadap observasi data). | 19 |
|$\mathcal{m}$| Jumlah total parameter yang diestimasi dalam penyeimbangan model (*AIC/BIC*). | 23 |
|$\mathcal{n}$| Jumlah keseluruhan ukuran observasi/sampel responden secara total dalam dataset. | 19 |
|$\mathcal{w}_{k}$| *Mixing weight* (Proporsi populasi atau probabilitas prior komponen/profil ke-). | 19 |
|$\mathcal{X}$| Kumpulan matriks atau fitur observasi data secara lengkap (dataset keseluruhan). | 19 |
|$\mathcal{x}_{\mathcal{i}}$| Vektor data nilai rekaman observasi per individu tunggal ke-. | 19 |
| *α* | Koefisien *Cronbach’s Alpha* (Indikator reliabilitas/kohesivitas internal sebuah alat ukur). | 12 |
|$\Upsilon(\mathcal{z}_{\mathcal{i}k})$| *Responsibilities* atau probabilitas ekspektasi posterior bahwa data observasi ke- berasal dari klaster/profil . | 20 |
|$\theta$| Kumpulan seluruh estimasi parameter turunan (*mean*, covarians, *weight*) dalam kalkulasi model. | 19 |
|$\mu_{k}$| Kumpulan vektor variabel *mean* (rata-rata lokasi atau sentroid per dimensi skalar normalisasi) dari komponen profil ke-. | 19 |
|$\Sigma_{k}$| Matriks dispersi *covariance* (rentang sebaran dari batas kurva komponen skalar kelompok) pada klaster profil ke-. | 19 |
|$\mathcal{N}$| Fungsi sebaran rentang kepadatan probabilitas normal/densitas untuk matriks *Gaussian* multivariat. | 19 |

# PENDAHULUAN

## Latar Belakang 

Eskalasi gangguan psikologis pasca-pandemi telah menempatkan isu kesehatan mental sebagai prioritas krusial dalam agenda kesehatan global, terutama setelah pandemi COVID-19 yang melanda seluruh dunia. Pandemi ini tidak hanya menimbulkan dampak fisik berupa tingginya angka kesakitan dan kematian, tetapi juga menyebabkan trauma psikologis yang mendalam pada berbagai kelompok populasi. Bersamaan itu, pandemi memicu akselerasi transformasi digital. Sebelum pandemi, transisi ke teknologi digital berlangsung secara bertahap, namun pandemi memaksa percepatan digitalisasi di hampir semua sektor kehidupan (Liu & Wu, 2024). Pasca pandemi, terbentuk fase *new normal* di mana gaya hidup digital yang terbentuk selama COVID-19 dibaurkan dengan gaya hidup konvensional, menciptakan dinamika baru dalam interaksi sosial (Selvam dkk., 2024). Dalam periode transisi ini, berbagai kelompok populasi mengalami kesulitan beradaptasi dengan perubahan yang sangat cepat.

Salah satu kelompok yang terdampak secara signifikan adalah remaja, khususnya Generasi Z (Gen Z). Gen Z adalah kelompok individu yang lahir antara pertengahan tahun 1990-an hingga awal 2010-an, yang tumbuh sebagai digital natives dengan karakteristik unik dalam pemanfaatan teknologi (Wajdi dkk., 2024). Kerentanan generasi ini meningkat khususnya bagi mahasiswa yang mengalami transisi ke perguruan tinggi bertepatan dengan pandemi COVID-19. Mereka harus menavigasi era *new normal* sekaligus menghadapi fase perkuliahan yang menurut Rahmadani & Mukti (2020) merupakan periode kritis penentuan masa depan, kemandirian, dan kesiapan karier. Akibatnya, Siddiqui & Siddiqui (2022) menilai dampak kesehatan mental pada angkatan ini jauh lebih buruk karena adanya tekanan ganda, di mana guncangan sosial akibat pandemi berimpitan langsung dengan tuntutan kematangan emosional dan akademik yang tinggi.

Kondisi ini sejalan dengan temuan global yang menunjukkan bahwa kesejahteraan mental mahasiswa menjadi perhatian serius karena proporsi gangguan mental di populasi kampus sangat tinggi dan berdampak pada fungsi harian serta capaian akademik. Survei lintas 18 negara yang melibatkan 72.288 mahasiswa tahun pertama menemukan bahwa *lifetime prevalence any mental disorder* mencapai 65,2% dan prevalensi 12 bulan sebesar 57,4%, dengan gangguan internalisasi seperti depresi dan kecemasan lebih dominan daripada gangguan eksternalisasi (Mason dkk., 2025). Temuan ini menegaskan kebutuhan mendesak akan skrining dan intervensi sistemik di lingkungan universitas untuk mencegah penurunan kesejahteraan mental yang lebih parah yang dapat dilihat pada tabel I.1-1 berikut.

<table>
<caption><p><span id="_Toc225768977" class="anchor"></span>Tabel I‑1 Prevalensi Gangguan Mental Mahasiswa Tahun Pertama (Lintas 18 Negara)</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 0%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th rowspan="2" style="text-align: left;"><strong>Types of Disorders</strong></th>
<th colspan="2" style="text-align: center;"><strong>Lifetime</strong></th>
<th colspan="3" style="text-align: center;"><strong>12-month</strong></th>
<th colspan="2" style="text-align: center;"><strong>12-month persistence</strong></th>
</tr>
<tr>
<th style="text-align: center;"><strong>%</strong></th>
<th style="text-align: center;"><strong>(SE)</strong></th>
<th colspan="2" style="text-align: center;"><strong>%</strong></th>
<th style="text-align: center;"><strong>(SE)</strong></th>
<th style="text-align: center;"><strong>%</strong></th>
<th style="text-align: center;"><strong>(SE)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8" style="text-align: left;"><strong>Internalizing disorders</strong></td>
</tr>
<tr>
<td style="text-align: left;">Any internalizing</td>
<td style="text-align: center;">54.7</td>
<td style="text-align: center;">(0.2)</td>
<td style="text-align: center;">43.9</td>
<td colspan="2" style="text-align: center;">(0.3)</td>
<td style="text-align: center;">80.8</td>
<td style="text-align: center;">(0.4)</td>
</tr>
<tr>
<td style="text-align: left;">Bipolar I/II disorder</td>
<td style="text-align: center;">4.9</td>
<td style="text-align: center;">(0.1)</td>
<td style="text-align: center;">4.3</td>
<td colspan="2" style="text-align: center;">(0.1)</td>
<td style="text-align: center;">85.9</td>
<td style="text-align: center;">(0.9)</td>
</tr>
<tr>
<td style="text-align: left;">Generalized anxiety disorder</td>
<td style="text-align: center;">12.8</td>
<td style="text-align: center;">(0.1)</td>
<td style="text-align: center;">11.5</td>
<td colspan="2" style="text-align: center;">(0.1)</td>
<td style="text-align: center;">89.0</td>
<td style="text-align: center;">(0.4)</td>
</tr>
<tr>
<td style="text-align: left;">Major depressive disorder</td>
<td style="text-align: center;">23.3</td>
<td style="text-align: center;">(0.2)</td>
<td style="text-align: center;">20.5</td>
<td colspan="2" style="text-align: center;">(0.2)</td>
<td style="text-align: center;">86.5</td>
<td style="text-align: center;">(0.3)</td>
</tr>
<tr>
<td style="text-align: left;">Panic disorder</td>
<td style="text-align: center;">9.1</td>
<td style="text-align: center;">(0.1)</td>
<td style="text-align: center;">7.2</td>
<td colspan="2" style="text-align: center;">(0.1)</td>
<td style="text-align: center;">78.2</td>
<td style="text-align: center;">(0.8)</td>
</tr>
<tr>
<td style="text-align: left;">Post-traumatic stress disorder</td>
<td style="text-align: center;">46.5</td>
<td style="text-align: center;">(0.2)</td>
<td style="text-align: center;">33.5</td>
<td colspan="2" style="text-align: center;">(0.3)</td>
<td style="text-align: center;">71.3</td>
<td style="text-align: center;">(0.5)</td>
</tr>
<tr>
<td colspan="8" style="text-align: left;"><strong>Externalizing disorders</strong></td>
</tr>
<tr>
<td style="text-align: left;">Any externalizing</td>
<td style="text-align: center;">44.1</td>
<td style="text-align: center;">(0.2)</td>
<td style="text-align: center;">30.7</td>
<td colspan="2" style="text-align: center;">(0.2)</td>
<td style="text-align: center;">94.4</td>
<td style="text-align: center;">(0.2)</td>
</tr>
<tr>
<td style="text-align: left;">Attention deficit/hyperactivity disorder</td>
<td style="text-align: center;">8.1</td>
<td style="text-align: center;">(0.1)</td>
<td style="text-align: center;">8.1</td>
<td colspan="2" style="text-align: center;">(0.1)</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Alcohol use disorder</td>
<td style="text-align: center;">23.6</td>
<td style="text-align: center;">(0.2)</td>
<td style="text-align: center;">23.6</td>
<td colspan="2" style="text-align: center;">(0.2)</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: left;">Drug use disorder</td>
<td style="text-align: center;">9.2</td>
<td style="text-align: center;">(0.1)</td>
<td style="text-align: center;">6.1</td>
<td colspan="2" style="text-align: center;">(0.1)</td>
<td style="text-align: center;">63.0</td>
<td style="text-align: center;">(0.7)</td>
</tr>
<tr>
<td style="text-align: left;">Any disorder</td>
<td style="text-align: center;">65.2</td>
<td style="text-align: center;">(0.2)</td>
<td style="text-align: center;">57.4</td>
<td colspan="2" style="text-align: center;">(0.3)</td>
<td style="text-align: center;">87.6</td>
<td style="text-align: center;">(0.2)</td>
</tr>
<tr>
<td style="text-align: center;">(n)</td>
<td colspan="2" style="text-align: center;">(72,288)</td>
<td colspan="3" style="text-align: center;">(72,288)</td>
<td colspan="2" style="text-align: center;">(40,803)</td>
</tr>
</tbody>
</table>

Sumber: Mason dkk. (2025)

Berdasarkan data global yang dijabarkan sebelumnya, menunjukkan urgensi permasalahan kesehatan mental di kalangan mahasiswa yang perlu ditangani secara komprehensif. Kondisi di Indonesia mencerminkan pola yang sama dengan tingkat permasalahan yang lebih mengkhawatirkan. Center for Reproductive Health (2022), melalui survei *Indonesia National Adolescent Mental Health Survey* (I-NAMHS) 2022, melaporkan bahwa 1 dari 3 remaja (34,9%) atau setara 15,5 juta jiwa mengalami masalah kesehatan mental dalam 12 bulan terakhir. Masalah tersebut didominasi oleh gangguan kecemasan (26,7%), kurang perhatian/hiperaktif (10,6%), dan depresi (5,3%). Secara demografis kerentanan tersebar cukup merata, namun prevalensinya sedikit lebih tinggi pada perempuan dibanding laki-laki, serta pada remaja awal 10-13 tahun dibanding usia 14-17 tahun.

Tingginya prevalensi gangguan mental tersebut menghadapkan institusi pendidikan pada tantangan besar, terutama karena identifikasi dan intervensi dini masih menghadapi hambatan metodologis. Instrumen *self-report* sering kali menunjukkan performa yang bervariasi pada populasi muda, menimbulkan risiko salah klasifikasi lintas kelompok demografis (Wang dkk., 2025). Keterbatasan identifikasi dini ini diperburuk oleh tindak lanjut yang cenderung reaktif. Hal ini terjadi karena data akademik dan kesejahteraan yang tersebar, sehingga analisis manual memerlukan waktu lama dan menyulitkan deteksi pola risiko secara dini (Keane, 2023). Di Indonesia, meski beberapa institusi melakukan skrining awal, hasilnya kebanyakan hanya menjadi data pasif tanpa tindak lanjut mendalam (Setyanto, 2023). Masalah utamanya bukan pada ketiadaan data, melainkan pada inefisiensi analisis manual terhadap data yang sebenarnya sudah tersedia dalam sistem.

Sebagai upaya pemetaan awal, beberapa institusi pendidikan tinggi telah memanfaatkan instrumen mendalam seperti OMNI Personality Inventory (OMNI) pada awal masa studi. Instrumen *self-report* komprehensif ini dirancang untuk usia 18-74 tahun dan terdiri dari 375 item yang mengukur 25 skala kepribadian normal, 10 skala gangguan kepribadian berdasarkan DSM-IV, serta dilengkapi dua *validity scales* yaitu *Variable Response Inconsistency* (VRIN) dan *Current Distress* (CD) (Guess, 2006). Dengan pendekatan yang mengintegrasikan karakteristik kepribadian "normal" dan "abnormal", OMNI menyediakan data terstruktur yang mendalam. Potensi inilah yang, jika dianalisis sistematis menggunakan komputasi cerdas, memungkinkan identifikasi profil mahasiswa secara komprehensif untuk mendukung intervensi yang lebih *targeted* dan proaktif.

Dalam ekosistem *healthcare analytics*, pemahaman profil kepribadian ini menjadi krusial karena bukan sekadar data klinis, melainkan faktor fundamental yang memengaruhi adaptasi dan resiliensi akademik. Studi literatur, khususnya pada *Five Factor Model* (FFM), mengonfirmasi adanya pola hubungan antara kepribadian dan disiplin ilmu, fenomena yang dikenal sebagai *selective entry* dan *socialization effects*. Misalnya, mahasiswa sains alam cenderung lebih introvert, sementara tingkat *openness* yang tinggi berkorelasi erat dengan jurusan seni dan humaniora (Kokkinos dkk., 2024). Mengacu pada dinamika tersebut, kekayaan data OMNI memiliki nilai strategis jika diolah dengan pendekatan analitik untuk memetakan karakteristik unik mahasiswa di setiap program studi.

Kendati demikian, optimalisasi data OMNI memerlukan pendekatan analitik yang tidak hanya komprehensif, tetapi juga mampu menyajikan hasil yang interpretatif bagi pemangku kepentingan. Tinjauan literatur memperlihatkan keterbatasan studi terdahulu. (Pan dkk., 2024) dan (Kokkinos dkk., 2024) menggunakan instrumen dengan dimensi terbatas (EPQ dan TIPI) sehingga kurang menangkap nuansa populasi lokal. Di sisi lain, penerapan *Latent Profile Analysis* (LPA) oleh (Guelmami dkk., 2022) masih terbatas pada prediksi risiko klinis tanpa disertai visualisasi yang mendukung advokasi praktis. Penelitian ini hadir mengisi celah tersebut dengan memanfaatkan dimensi OMNI sebagai basis pemetaan profil, serta menyajikan hasil secara visual dan *actionable* guna mendukung strategi pencegahan universal (*universal prevention*) di lingkungan kampus.

Penelitian ini beralih dari pendekatan tradisional yang hanya melihat hubungan antar-variabel (*variable-centered*) menuju pendekatan *person-centered* menggunakan *Latent Profile Analysis* (LPA). Berbeda dengan prediksi klinis yang kaku, LPA mengekstrak profil atau segmen laten dari data OMNI untuk mengidentifikasi subgrup mahasiswa dengan pola karakteristik serupa. Pendekatan ini memungkinkan pemahaman holistik terhadap heterogenitas mahasiswa, yang kemudian dapat dipetakan distribusinya lintas fakultas untuk merancang strategi intervensi yang spesifik (Pan dkk., 2024; Pecora dkk., 2025).

Pemilihan LPA didasarkan pada karakteristiknya yang sesuai untuk analisis data kepribadian. LPA menggunakan *soft classification* (probabilitas keanggotaan) yang lebih cocok untuk data kepribadian yang bersifat kontinyu dan beririsan, serta menyediakan indikator statistik objektif (AIC, BIC, Entropy) untuk menentukan jumlah profil optimal secara valid (Spurk dkk., 2020).  Selain itu, hasil LPA berupa profil deskriptif yang bermakna substantif dan lebih mudah diinterpretasi oleh pemangku kepentingan non-teknis seperti dosen wali dan psikolog, berbeda dengan sekadar pengelompokan matematis yang abstrak.

Secara keseluruhan, penelitian ini dirancang untuk mengoptimalkan pemanfaatan data OMNI melalui sistem *personality profiling* berbasis data yang menyajikan insight komprehensif dan *actionable* bagi pemangku kepentingan di kampus (seperti dosen wali dan psikolog). Melalui kombinasi analisis LPA dan uji invariansi pengukuran, sistem ini tidak hanya memetakan distribusi profil kepribadian lintas program studi dan fakultas, tetapi juga memastikan validitas hasil lintas kelompok demografis. Hasil akhirnya ditujukan untuk mendukung perancangan rekomendasi intervensi kesehatan mental yang berbasis bukti, sehingga proses pembinaan akademik dan layanan kesejahteraan mahasiswa dapat berjalan lebih terarah, adaptif, dan selaras dengan kebutuhan unik setiap kelompok studi.

## Rumusan Masalah 

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah:

1.  Bagaimana struktur profil kepribadian laten mahasiswa dari data OMNI dapat diidentifikasi menggunakan LPA, divalidasi melalui pengujian *measurement invariance* lintas kelompok demografis, dan dipetakan distribusinya untuk mengidentifikasi pola signifikan pada berbagai program studi, fakultas, dan angkatan?

2.  Bagaimana *insight* dari profil kepribadian mahasiswa dapat disajikan melalui *dashboard* visualisasi  yang *informatif* dan *actionable*, untuk mendukung pemangku kepentingan dalam merancang intervensi kesehatan mental yang berbasis data dan tepat sasaran?

## Tujuan Penelitian

Berdasarkan rumusan masalah yang ada, tujuan yang ingin dicapai dari penelitian ini adalah:

1.  Mengidentifikasi dan memvalidasi struktur profil kepribadian laten mahasiswa menggunakan LPA dengan pengujian *measurement invariance*, serta memetakan distribusi dan signifikansi perbedaan profil lintas kelompok demografis (program studi, fakultas, dan angkatan).

2.  Mengembangkan prototipe *dashboard* visualisasi yang menyajikan *insight* profil kepribadian mahasiswa secara informatif dan *actionable*, sehingga memfasilitasi pengambilan keputusan yang berbasis bukti oleh pemangku kepentingan (seperti dosen wali dan psikolog) dalam merancang rekomendasi intervensi kesehatan mental yang tepat sasaran.

## Batasan Penelitian

Untuk menjaga fokus dan kedalaman analisis, penelitian ini dibatasi pada aspek-aspek berikut:

1.  Sumber Data: Penelitian ini menggunakan data sekunder dari instrumen OMNI pada mahasiswa Universitas Telkom. Penelitian tidak mengintegrasikan data klinis dari sesi konseling, rekam medis, atau data hasil akademik (IPK).

2.  Fokus Analisis: Analisis difokuskan pada pemetaan profil kepribadian tingkat populasi (*population-level profiling*) menggunakan metode *Latent Profile Analysis* (LPA) untuk tujuan pencegahan dan promosi kesehatan mental pada level universal (universal prevention), bukan untuk diagnosis klinis individual atau prediksi langsung risiko gangguan jiwa.​

3.  Lingkup Populasi: Subjek penelitian terbatas pada populasi mahasiswa di lingkungan perguruan tinggi yang sama dengan sumber data OMNI. Generalisasi hasil ke institusi lain memerlukan uji validasi eksternal karena adanya potensi perbedaan karakteristik demografis, budaya kampus, dan konteks pembelajaran.

4.  Variabel Penelitian:

    - Variabel *input* profil menggunakan dimensi kepribadian dari instrumen OMNI.

    - Variabel komparasi demografis dibatasi pada atribut yang tersedia dalam data (program studi, fakultas, angkatan, dan gender).

5.  Etika & Privasi: Seluruh analisis dilakukan pada data yang telah dianonimkan (*de-identified*), sehingga tidak memuat identitas individu secara langsung. Pengolahan data dilakukan dengan memperhatikan prinsip pelindungan data pribadi dan tata kelola data yang baik sesuai regulasi yang berlaku.​

## Manfaat Penelitian

Penelitian ini diharapkan dapat memberikan manfaat baik secara praktis maupun teoritis sebagai berikut:

1.  Manfaat Praktis

    - Bagi Universitas Telkom (Unit Konseling & Program Studi): Memberikan peta profil kepribadian mahasiswa berbasis data (*data-driven*) yang dapat digunakan sebagai landasan strategis dalam merancang program dukungan akademik, layanan konseling, dan advokasi kesehatan mental yang lebih tepat sasaran sesuai karakteristik unik setiap program studi.

    - Bagi Mahasiswa: Mendukung terciptanya ekosistem kampus yang lebih inklusif dan responsif terhadap kebutuhan psikologis mahasiswa, sehingga memudahkan akses terhadap bentuk dukungan atau intervensi kesehatan mental yang relevan dengan profil kepribadian mereka.

2.  Manfaat Teoritis

    - Bagi Pengembangan Ilmu: Memberikan kontribusi literatur mengenai penerapan metode *Latent Profile Analysis* (LPA) dalam konteks psikologi pendidikan di Indonesia, khususnya dalam memetakan variasi kepribadian lintas disiplin ilmu dengan validasi *measurement invariance* yang ketat.

    - Bagi Peneliti Selanjutnya: Menjadi referensi metodologis dan kerangka kerja dasar (*baseline framework*) untuk penelitian lanjutan, seperti validasi eksternal di institusi lain, integrasi profil kepribadian dengan performa akademik, atau pengembangan sistem intervensi berbasis *machine learning* yang lebih kompleks.

## Sistematika Penulisan

Penelitian ini diuraikan dengan sistematika penulisan sebagai berikut:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th><strong>Bab I</strong></th>
<th><p><strong>Pendahuluan</strong></p>
<p>Bab ini memaparkan latar belakang masalah mengenai urgensi kesehatan mental mahasiswa, rumusan masalah, tujuan penelitian, batasan penelitian, manfaat penelitian bagi institusi dan mahasiswa, serta sistematika penulisan laporan tugas akhir ini.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bab II</strong></td>
<td><p><strong>KAJIAN PUSTAKA</strong></p>
<p>Bab ini menguraikan landasan teori secara sistematis, dimulai dari isu kesehatan mental mahasiswa dan instrumen TOMNI. Pembahasan berlanjut pada konsep <em>Data Mining</em>, <em>Machine Learning</em>, dan <em>Clustering</em> sebagai fondasi teknis, serta pendalaman metode <em>Latent Profile Analysis</em> (LPA) dan uji <em>Measurement Invariance</em>. Bab ini diakhiri dengan penjelasan <em>Decision Support System</em> serta pemetaan posisi penelitian melalui tinjauan studi terdahulu (<em>State of the Art</em>).</p></td>
</tr>
<tr>
<td><strong>Bab III</strong></td>
<td><p><strong>Metode Penyelesaian Masalah</strong></p>
<p>Bab ini menguraikan metode penelitian yang digunakan, langkah-langkah sistematis penyelesaian masalah, metode pengumpulan dan pengolahan data, serta metode evaluasi dan validasi hasil analisis yang dihasilkan.</p></td>
</tr>
</tbody>
</table>

# TINJAUAN PUSTAKA

## Dasar Teori

### Kesehatan Mental Mahasiswa

Kesehatan mental adalah kondisi kesejahteraan psikologis yang meliputi aspek emosional, kognitif, dan sosial dari seorang individu (WHO, 2022). Dalam konteks populasi mahasiswa, kesehatan mental mencakup kemampuan untuk beradaptasi dengan stres akademik, menjalin hubungan interpersonal yang sehat, dan mencapai keseimbangan antara kehidupan akademik dan personal. Isu ini telah menjadi prioritas global setelah pandemi COVID-19, dengan peningkatan signifikan dalam prevalensi gangguan mental di kalangan mahasiswa. Survei lintas 18 negara melibatkan 72.288 mahasiswa tahun pertama menemukan bahwa *lifetime prevalence* gangguan mental mencapai 65,2%, dengan prevalensi 12 bulan sebesar 57,4% (Mason dkk., 2025).

Kondisi di tingkat global tersebut sejalan dengan situasi di Indonesia. Data Indonesia *National Adolescent Mental Health Survey* (I-NAMHS) 2022 menunjukkan bahwa 34,9% remaja mengalami masalah kesehatan mental dalam 12 bulan terakhir, dengan kecemasan sebagai gangguan paling umum (26,7%), diikuti oleh gangguan perhatian/hiperaktif (10,6%), dan depresi (5,3%) (Center for Reproductive Health, 2022). Prevalensi masalah kesehatan mental di kalangan remaja ini dapat divisualisasikan lebih jelas melalui perbedaan demografis pada Tabel II.1-1 berikut.

<table>
<caption><p><span id="_Toc225768978" class="anchor"></span>Tabel II‑1 Prevalensi Masalah Kesehatan Mental Remaja (10-17 Tahun) Menurut Jenis Kelamin dan Usia (12 Bulan Terakhir)</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 8%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Karakteristik</strong></th>
<th colspan="2" style="text-align: center;"><strong>10-13 tahun</strong></th>
<th colspan="2" style="text-align: center;"><strong>14-17 tahun</strong></th>
<th colspan="2" style="text-align: center;"><strong>Total</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: center;"><strong>%</strong></td>
<td style="text-align: center;"><strong>(n/N)</strong></td>
<td style="text-align: center;"><strong>%</strong></td>
<td style="text-align: center;"><strong>(n/N)</strong></td>
<td style="text-align: center;"><strong>%</strong></td>
<td style="text-align: center;"><strong>(n/N)</strong></td>
</tr>
<tr>
<td style="text-align: left;">Laki-laki</td>
<td style="text-align: center;">36.1</td>
<td style="text-align: center;">(540/1.498)</td>
<td style="text-align: center;">33.0</td>
<td style="text-align: center;">(457/1.385)</td>
<td style="text-align: center;">34.6</td>
<td style="text-align: center;">(997/2.883)</td>
</tr>
<tr>
<td style="text-align: left;">Perempuan</td>
<td style="text-align: center;">34.2</td>
<td style="text-align: center;">(498/1.458)</td>
<td style="text-align: center;">36.2</td>
<td style="text-align: center;">(479/1.322)</td>
<td style="text-align: center;">35.1</td>
<td style="text-align: center;">(977/2.781)</td>
</tr>
<tr>
<td style="text-align: left;">Total</td>
<td style="text-align: center;">35.1</td>
<td style="text-align: center;">(1.038/2.956)</td>
<td style="text-align: center;">34.6</td>
<td style="text-align: center;">(936/2.708)</td>
<td style="text-align: center;">34.9</td>
<td style="text-align: center;">(1.974/5.664)</td>
</tr>
<tr>
<td colspan="7" style="text-align: left;">n=pembilang; N=penyebut</td>
</tr>
</tbody>
</table>

Sumber: Center for Reproductive Health (2022)

Tingginya prevalensi ini menghadapkan institusi pendidikan pada tantangan besar, terutama terkait kesenjangan antara kebutuhan layanan dengan kapasitas penanganan. Contohnya di Amerika Serikat, tercatat hanya 36% mahasiswa yang menerima layanan konseling dalam periode satu tahun terakhir (Eisenberg dkk., 2023). Tantangan ini diperberat oleh hambatan metodologis, di mana instrumen *self-report* sering menunjukkan performa yang bervariasi dan risiko salah klasifikasi pada populasi muda (Wang dkk., 2025).

Dalam perspektif sistem informasi dan pengelolaan data, kendala utama yang dihadapi bukan hanya pada ketiadaan data skrining, melainkan pada inefisiensi proses analisis. Di Indonesia, meskipun institusi pendidikan telah melakukan skrining awal, data yang dihasilkan sering kali berakhir sebagai data pasif (Keane, 2023). Hal ini disebabkan oleh proses analisis manual yang memakan waktu lama dan tidak terintegrasi, sehingga menghambat proses deteksi dini dan tindak lanjut intervensi yang seharusnya bersifat segera dan tepat sasaran (Setyanto, 2023). Oleh karena itu, diperlukan pendekatan berbasis data (*data-driven*) yang mampu mengolah hasil skrining kompleks menjadi wawasan yang dapat ditindaklanjuti secara efisien.

### OMNI

*OMNI Personality Inventory* (selanjutnya disebut OMNI) adalah instrumen asesmen kepribadian berbasis *self-report* yang komprehensif, dikembangkan oleh Armand W. Loranger untuk populasi dewasa berusia 18-74 tahun (Guess, 2006). Berbeda dengan instrumen kepribadian konvensional yang sering kali hanya berfokus pada satu sisi (normal atau patologis saja), OMNI menggunakan pendekatan *eclectic* yang mengintegrasikan perspektif kepribadian normal (akademik) dan kepribadian abnormal (klinis) dalam satu alat ukur yang padu.

Dalam ranah psikometri, disiplin ilmu yang berfokus pada teknik pengukuran psikologis dengan standar ketat untuk memastikan reliabilitas dan validitas (Kline, 2023), OMNI dirancang untuk mengukur konstruk laten kepribadian secara objektif melalui respons terhadap serangkaian item terstruktur. Secara struktur, OMNI terdiri dari 375 butir pernyataan (item) yang dinilai menggunakan skala *Likert*. Item-item tersebut dikelompokkan menjadi 7 faktor utama dan 25 skala kepribadian normal, serta dilengkapi dengan skala gangguan kepribadian dan validitas. Struktur komponen OMNI dapat dilihat pada Tabel II-2 berikut.

<table>
<caption><p><span id="_Toc225768979" class="anchor"></span>Tabel II‑2 Struktur Komponen <em>OMNI Personality Inventory</em></p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Normal Scales</strong></th>
<th style="text-align: left;"><strong>Personality Disorder Scales</strong></th>
<th style="text-align: left;"><strong>Factor Scales</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Aestheticism</td>
<td style="text-align: left;">Paranoid</td>
<td style="text-align: left;">Agreeableness</td>
</tr>
<tr>
<td style="text-align: left;">Ambition</td>
<td style="text-align: left;">Schizoid</td>
<td style="text-align: left;">Conscientiousness</td>
</tr>
<tr>
<td style="text-align: left;">Anxiety</td>
<td style="text-align: left;">Schizotypal</td>
<td style="text-align: left;">Extraversion</td>
</tr>
<tr>
<td style="text-align: left;">Assertiveness</td>
<td style="text-align: left;">Antisocial</td>
<td style="text-align: left;">Narcissism</td>
</tr>
<tr>
<td style="text-align: left;">Conventionality</td>
<td style="text-align: left;">Borderline</td>
<td style="text-align: left;">Neuroticism</td>
</tr>
<tr>
<td style="text-align: left;">Depression</td>
<td style="text-align: left;">Histrionic</td>
<td style="text-align: left;">Openness</td>
</tr>
<tr>
<td style="text-align: left;">Dutifulness</td>
<td style="text-align: left;">Narcissistic</td>
<td style="text-align: left;">Sensation Seeking</td>
</tr>
<tr>
<td style="text-align: left;">Excitement</td>
<td style="text-align: left;">Avoidant</td>
<td rowspan="17" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Exhibitionism</td>
<td style="text-align: left;">Dependent</td>
</tr>
<tr>
<td style="text-align: left;">Energy</td>
<td style="text-align: left;">Obsessive-Compulsive</td>
</tr>
<tr>
<td style="text-align: left;">Flexibility</td>
<td rowspan="14" style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Hostility</td>
</tr>
<tr>
<td style="text-align: left;">Impulsiveness</td>
</tr>
<tr>
<td style="text-align: left;">Intellect</td>
</tr>
<tr>
<td style="text-align: left;">Irritability</td>
</tr>
<tr>
<td style="text-align: left;">Modesty</td>
</tr>
<tr>
<td style="text-align: left;">Moodiness</td>
</tr>
<tr>
<td style="text-align: left;">Orderliness</td>
</tr>
<tr>
<td style="text-align: left;">Self-Indulgence</td>
</tr>
<tr>
<td style="text-align: left;">Sincerity</td>
</tr>
<tr>
<td style="text-align: left;">Sociability</td>
</tr>
<tr>
<td style="text-align: left;">Self-Reliance</td>
</tr>
<tr>
<td style="text-align: left;">Tolerance</td>
</tr>
<tr>
<td style="text-align: left;">Warmth</td>
</tr>
</tbody>
</table>

Sumber: (Guess, 2006)

Berdasarkan struktur tersebut, deskripsi fungsi dan cakupan pengukuran dari masing-masing kelompok skala dijabarkan sebagai berikut (Guess, 2006):

- 25 *Normal Personality Scales* (Skala Kepribadian Normal) yang mengukur karakteristik kepribadian adaptif dan fungsional dalam populasi umum, mencakup dimensi temperamen (*Negative & Positive Temperament*), gaya interpersonal (*Introversion, Extroversion, Aggression, Compliance*), serta orientasi nilai (*Sensation Seeking, Harm Avoidance*) untuk memberikan gambaran kekuatan dan gaya adaptasi individu.

- 10 *Personality Disorder Scales* (Skala Gangguan Kepribadian) yang dirancang untuk mengukur ciri-ciri terkait gangguan kepribadian menurut DSM-IV, meliputi *Paranoid, Schizoid, Schizotypal, Antisocial, Borderline, Histrionic, Narcissistic, Avoidant, Dependent,* dan *Obsessive-Compulsive features*, di mana skala ini berfungsi mengidentifikasi *trait* (sifat) yang memerlukan pemantauan lebih lanjut dan bukan sebagai diagnosis klinis formal.

- 2 *Validity Scales* (Skala Validitas) yang berfungsi sebagai kontrol kualitas data, terdiri dari *Variable Response Inconsistency* (VRIN) untuk mendeteksi inkonsistensi pola jawaban akibat kurangnya pemahaman atau jawaban acak, serta *Current Distress* (CD) yang mencerminkan tekanan emosional sesaat (*anxiety, sadness*) yang berpotensi memengaruhi akurasi jawaban responden.

- 7 *Broad Scales* (Skala Umum) yang mewakili integrasi dari *trait* normal dan abnormal yang dikelompokkan menjadi dimensi faktor yang lebih luas untuk memudahkan interpretasi profil kepribadian secara global.

Pemilihan instrumen OMNI dalam konteks asesmen mahasiswa didasarkan pada keunggulan komprehensivitasnya yang memuat 375 item dan 25 skala kepribadian normal, sehingga mampu menyediakan penilaian profil multidimensional yang mendalam dan *nuanced* (Guess, 2006). Instrumen ini memiliki keunikan integratif karena menggabungkan pengukuran kepribadian normal dan ciri gangguan kepribadian dalam satu spektrum, serta didukung oleh konsistensi internal yang moderat hingga tinggi, dengan koefisien *alpha* berkisar antara .53 hingga .86 untuk skala kepribadian normal, .62 hingga .84 untuk skala gangguan kepribadian, dan .79 hingga .94 untuk skala faktor (Guess, 2006). Selain dirancang relevan untuk populasi usia 18-74 tahun, OMNI juga dilengkapi indikator kualitas respons seperti VRIN dan CD yang memungkinkan deteksi reliabilitas data pada level individual, memastikan analisis hanya dilakukan pada data yang valid.

Dalam implementasinya di institusi pendidikan Indonesia, instrumen ini banyak digunakan sebagai alat skrining rutin pada masa orientasi mahasiswa baru (PKKMB) untuk memetakan profil kepribadian awal. Meskipun data yang dikumpulkan sangat kaya informasi, fakta di lapangan menunjukkan bahwa hasil asesmen ini sering kali hanya berakhir sebagai arsip atau patokan awal yang pasif. Pemanfaatan data tersebut untuk perencanaan program kesejahteraan mahasiswa yang berkelanjutan masih belum optimal, sehingga potensi OMNI sebagai landasan strategi preventif kesehatan mental belum tergali sepenuhnya (Setyanto, 2023).

### *Data Mining*

*Data mining* adalah proses mengekstraksi pola, pengetahuan, dan *insight* bermakna dari kumpulan data besar melalui kombinasi teknik statistik, komputasi, dan algoritma *machine learning* (Schröer dkk., 2021). Berbeda dengan statistik deskriptif atau inferensial tradisional yang fokus pada pengujian hipotesis spesifik, *data mining* lebih bersifat *exploratory* dan *discovery-driven*, mencari pola dan struktur yang mungkin sebelumnya tidak diketahui atau diharapkan (Sarker, 2021).

*Data mining* diaplikasikan dalam berbagai domain, termasuk bisnis (*customer segmentation*, *churn prediction*), kesehatan *(disease diagnosis*, *patient risk stratification*), dan sosial (*behavior analysis*, *recommendation systems*) (Schröer dkk., 2021). Dalam konteks kesehatan dan pendidikan, *data mining* dapat digunakan untuk mengidentifikasi pola dalam data asesmen psikologis guna mendukung pengambilan keputusan klinis atau administratif.

Salah satu kerangka kerja yang umum digunakan dalam proses *data mining* yaitu CRISP-DM. CRISP-DM (*Cross-Industry Standard Process for Data Mining*) adalah kerangka kerja standar industri yang telah diadopsi berbagai organisasi untuk memandu proses *data mining* dan *analytics* dari perencanaan hingga implementasi (Schröer dkk., 2021). Kerangka kerja ini terdiri dari enam tahap siklus yang saling terhubung dan iteratif, yang dapat dilihat pada Gambar II-1 berikut.

<figure>
<figcaption><p><span id="_Toc225768968" class="anchor"></span>Gambar II‑1 Siklus Kerangka Kerja CRISP-DM</p></figcaption>
</figure>

Sumber: Hanum dkk. (2023)

Keenam tahapan CRISP-DM adalah sebagai berikut (Schröer dkk., 2021):

1.  *Business Understanding*: Memahami objektif bisnis atau penelitian, mendefinisikan masalah, dan menetapkan target yang ingin dicapai. Tahap ini melibatkan identifikasi stakeholder, kebutuhan mereka, dan kendala-kendala yang ada.

2.  *Data Understanding*: Mengumpulkan, mengeksplorasi, dan menganalisis data awal untuk memahami kualitas, struktur, dan karakteristiknya. Tahap ini mencakup data *profiling*, identifikasi *missing values*, *outliers*, dan distribusi data.

3.  *Data Preparation*: Membersihkan, mentransformasi, dan mempersiapkan data untuk tahap *modeling*. Aktivitas ini mencakup *handling missing values*, *outlier treatment*, *feature engineering*, normalisasi/standardisasi, dan *feature selection*.

4.  *Modeling*: Memilih dan menerapkan algoritma atau teknik analitik yang sesuai untuk mengekstraksi pola dari data. Tahap ini mencakup eksperimen dengan berbagai model, *parameter tuning*, dan *cross-validation*.

5.  *Evaluation*: Mengevaluasi hasil model terhadap kriteria kesuksesan yang telah ditetapkan di tahap *Business Understanding*. Evaluasi mencakup *assessment* *goodness-of-fit*, validasi stabilitas model, dan *alignment* dengan objektif bisnis.

6.  *Deployment*: Mengimplementasikan model atau hasil analisis ke dalam lingkungan operasional, menciptakan visualisasi atau *dashboard* untuk *end-users*, dan menyiapkan dokumentasi serta *training* untuk pengguna.

Secara keseluruhan, kerangka kerja CRISP-DM menawarkan fleksibilitas tinggi dan sifat adaptif yang agnostik terhadap teknologi spesifik. Pendekatan iteratifnya memfasilitasi perbaikan berkelanjutan (*continuous refinement*) sepanjang siklus proyek, sekaligus menjembatani kesenjangan antara analisis teknis dan kebutuhan praktis bisnis. Dengan menekankan kolaborasi erat antara saintis data, ahli domain, dan pemangku kepentingan, CRISP-DM memastikan solusi yang dihasilkan tidak hanya akurat secara analitis, tetapi juga relevan dan dapat diimplementasikan (*implementable*) secara operasional (Schröer dkk., 2021).

### *Machine Learning*

*Machine Learning* adalah cabang dari *artificial intelligence* (AI) yang memungkinkan sistem komputer untuk belajar dan meningkatkan kinerjanya dari pengalaman data tanpa diprogram secara eksplisit untuk setiap tugas spesifik (Sarker, 2021). Berbeda dengan pemrograman tradisional di mana programmer menuliskan instruksi secara detail, *machine learning* memungkinkan sistem untuk mengidentifikasi pola dan membuat keputusan berdasarkan data.

*Machine learning* umumnya dibagi menjadi tiga paradigma utama (Janiesch dkk., 2021):

1.  *Supervised Learning*: Sistem belajar dari data berlabel (*labeled data*), di mana setiap sampel memiliki *input* dan *output* yang diketahui. Tujuannya adalah untuk memprediksi output berdasarkan *input* baru. Contoh: regresi (prediksi nilai kontinyu), klasifikasi (prediksi kategori diskrit).

2.  *Unsupervised Learning*: Sistem belajar dari data tanpa label (*unlabeled data*), dengan tujuan menemukan struktur atau pola tersembunyi dalam data. Contoh: *clustering* (pengelompokan), *dimensionality reduction* (reduksi dimensi).

3.  *Reinforcement Learning*: Sistem belajar melalui interaksi dengan lingkungan, menerima *reward* atau *penalty* berdasarkan aksi yang diambil. Paradigma ini sering digunakan dalam robotika dan game AI.

Alur umum dalam proyek machine learning mencakup: (1) pengumpulan dan eksplorasi data, (2) preprocessing dan feature engineering, (3) pemilihan model, (4) training model dengan hyperparameter tuning, (5) evaluasi model menggunakan metrik performa, dan (6) deployment dan monitoring model di lingkungan produksi (Janiesch dkk., 2021; Sarker, 2021).

Machine learning telah diaplikasikan luas dalam berbagai domain, seperti *computer vision* (pengenalan gambar), *natural language processing* (pemrosesan bahasa alami), *recommendation systems*, *fraud detection*, *medical diagnosis*, dan analisis perilaku pengguna(Janiesch dkk., 2021; Sarker, 2021). Dalam penelitian sosial dan psikologi, *machine learning* digunakan untuk mengidentifikasi pola dalam *data behavioral*, asesmen psikologis, atau data kuantitatif lainnya.

### *Clustering*

*Clustering* adalah teknik dalam *machine learning* yang mengelompokkan sekumpulan data ke dalam beberapa subgrup atau klaster berdasarkan kesamaan atau kedekatan karakteristik, tanpa memiliki label atau kategori yang telah ditentukan sebelumnya (*unsupervised learning*). Tujuan *clustering* adalah menemukan struktur alami dalam data, mengidentifikasi kelompok-kelompok yang homogen secara internal (*similar within groups*) dan heterogen antar kelompok (*dissimilar between groups*) (Khan dkk., 2025).

Dalam penelitian psikologi dan sosial, terdapat dua paradigma analisis yang berbeda yaitu *Variable-Centered Approach* dan *Person-Centered Approach*. *Variable-Centered Approach* berfokus pada hubungan antar variabel, misalnya korelasi antara *trait* kepribadian A dengan kondisi kesehatan mental B. Pendekatan ini menggunakan teknik seperti regresi, *structural equation modeling*, atau *factor analysis*. Sedangkan *Person-Centered Approach* berfokus pada pengelompokan individu berdasarkan pola karakteristik keseluruhan mereka. Pendekatan ini mengenali bahwa individu berbeda tidak hanya dalam "nilai rata-rata" pada variabel tertentu, melainkan dalam pola keseluruhan atau profil mereka. *Clustering* dan *latent profile analysis* adalah teknik utama dalam *person-centered approach* (Pan dkk., 2024).

Terdapat berbagai algoritma *clustering* yang tersedia, masing-masing dengan asumsi dan karakteristik berbeda (Khan dkk., 2025):

1.  *K-Means Clustering*: Algoritma partisional yang membagi data ke dalam *K* klaster dengan meminimalkan *within-cluster variance*. *K-means* menggunakan *hard assignment*, di mana setiap titik data di-*assign* ke satu klaster saja. Algoritma ini sederhana dan cepat, tetapi sensitif terhadap *outliers* dan memerlukan penentuan *K* secara apriori.

2.  *Hierarchical Clustering*: Membangun hirarki klaster melalui *agglomeration* (*bottom-up*) atau *division* (*top-down*). Hasil dapat divisualisasikan dalam dendogram. Metode ini tidak memerlukan penentuan jumlah klaster apriori, tetapi secara komputasi lebih mahal (*computationally expensive*).

3.  *Density-Based Clustering* (e.g., DBSCAN): Mengidentifikasi klaster berdasarkan kepadatan (*density*) titik data. Metode ini baik untuk menemukan klaster berbentuk *arbitrary* dan mendeteksi *outliers*, tetapi parameter *threshold* dapat sulit ditentukan.

4.  *Model-Based Clustering* (e.g., *Gaussian Mixture Model*): Mengasumsikan bahwa data berasal dari *mixture* distribusi probabilistik. Pendekatan ini lebih fleksibel dan menyediakan probabilitas keanggotaan (*soft assignment*) daripada *hard assignment*.

Perbedaan krusial dalam *clustering* adalah apakah setiap titik data di-*assign* secara kaku (*hard*) atau probabilistik (*soft*) (Khan dkk., 2025):

- *Hard Clustering*: Setiap individu di-*assign* ke satu klaster dengan probabilitas 1, dan ke klaster lain dengan probabilitas 0. Pendekatan ini cocok untuk data yang memiliki batas klaster yang jelas, tetapi kurang sesuai untuk data yang bersifat kontinyu atau beririsan.

- *Soft Clustering*: Setiap individu memiliki probabilitas keanggotaan di berbagai klaster ($\sum$ probabilitas = 1). Pendekatan ini lebih fleksibel dan sesuai untuk data kepribadian yang bersifat gradual dan *overlapping*.

<figure>
<figcaption><p><span id="_Toc225768969" class="anchor"></span>Gambar II‑2 Perbandingan <em>Hard Clustering</em> (K-Means) dan <em>Soft Clustering</em> (LPA)</p></figcaption>
</figure>

Sumber: Obiedat dkk. (2020)

Karena *clustering* adalah *unsupervised learning* (tanpa *ground truth label*), evaluasi dilakukan melalui beberapa pendekatan (Khan dkk., 2025):

- *Internal Validation*: Menggunakan ukuran seperti *Silhouette Coefficient*, *Davies-Bouldin Index*, dan *Calinski-Harabasz Index* untuk mengevaluasi kekompakan (*compactness*) dan pemisahan (*separation*) klaster.

- *External Validation* (jika tersedia *reference labels*): Menggunakan *Adjusted Rand Index* atau *Normalized Mutual Information* untuk membandingkan hasil *clustering* dengan *ground truth*.

- *Stability Assessment*: Mengevaluasi apakah klaster tetap stabil ketika data atau parameter sedikit berubah.

### *Latent Profile Analysis* (LPA)

*Latent Profile Analysis* (LPA) adalah teknik statistik yang menggunakan pendekatan *person-centered* dan probabilistik untuk mengidentifikasi subgrup atau profil laten dalam data multivariat (Ferguson dkk., 2020; Pan dkk., 2024). LPA mengasumsikan bahwa populasi yang diamati terdiri dari beberapa subgrup heterogen (*K* profil), masing-masing dengan distribusi karakteristik unik. Teknik ini mengekstraksi profil-profil tersebut dari data secara *data-driven*, tanpa pengetahuan apriori tentang berapa banyak profil atau seperti apa karakteristiknya (Spurk dkk., 2020).

Latent Profile Analysis (LPA) dibangun di atas fondasi *Gaussian Mixture Model* (GMM), sebuah model probabilistik yang merepresentasikan distribusi data sebagai kombinasi (*mixture*) dari *K* distribusi Gaussian multivariat. Dalam model ini, densitas probabilitas gabungan untuk sebuah observasi multivariat x didefinisikan sebagai berikut (lihat Persamaan II-1) (Yehoshua, 2023):

$p\left( x \middle| \theta \right) = \sum_{k = 1}^{K}{w_{k}\mathcal{N}\left( x;\mu_{k},\Sigma_{k} \right)}$ (II-1)

Keterangan:

> $K$ = jumlah komponen atau profil Gaussian
>
> $w_{k}$ = *mixing weight* atau probabilitas *prior* komponen ke-$k$, dengan syarat $w_{k} > 0$ dan $\sum_{k = 1}^{K}w_{k} = 1$
>
> $\mu_{k}$ = vektor *mean* dari komponen Gaussian ke-$k$
>
> $\Sigma_{k}$ = matriks *covariance* dari komponen Gaussian ke-$k$
>
> $\mathcal{N}\left( x;\mu_{k},\Sigma_{k} \right)$ = fungsi densitas normal multivariat untuk komponen ke-$k$

Karena perkalian probabilitas yang kecil dapat menyebabkan masalah komputasi (*numerical underflow*), estimasi parameter dilakukan dengan memaksimalkan fungsi *log-likelihood* sebagai berikut (lihat Persamaan II-2) (Yehoshua, 2023):

$l\left( \theta \middle| X \right) = \sum_{i = 1}^{n}{\log\left\lbrack \sum_{k = 1}^{K}{w_{k}\mathcal{N}\left( x_{i};\mu_{k},\Sigma_{k} \right)} \right\rbrack}$ (II-2)

Keterangan:

> $n$ = jumlah total observasi
>
> $X$ = dataset lengkap
>
> $K$ = jumlah profil
>
> $w_{k}$ = *mixing weight* komponen ke-$k$
>
> $\mathcal{N}\left( x_{i};\mu_{k},\Sigma_{k} \right)$ = fungsi densitas normal multivariat untuk komponen $k$

Karena adanya variabel laten (*latent variables*) yang tidak terobservasi, parameter model tidak dapat diestimasi secara langsung. Oleh karena itu, digunakan algoritma *Expectation-Maximization* (EM) yang bekerja secara iteratif dalam dua langkah (Yehoshua, 2023):

1\. E-Step (*Expectation*): Langkah ini menghitung responsibilities <img src="media/image4.png" title="gamma left parenthesis z subscript i k end subscript right parenthesis" style="width:0.48958in;height:0.19135in" alt="{&quot;mathml&quot;:&quot;&lt;math style=\&quot;font-family:stix;font-size:16px;\&quot; xmlns=\&quot;http://www.w3.org/1998/Math/MathML\&quot;&gt;&lt;mi&gt;&amp;#x3B3;&lt;/mi&gt;&lt;mo&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;z&lt;/mi&gt;&lt;mrow&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;)&lt;/mo&gt;&lt;/math&gt;&quot;,&quot;origin&quot;:&quot;MathType Legacy&quot;,&quot;version&quot;:&quot;v3.20.0&quot;}" />, yaitu probabilitas posterior bahwa data $\mathcal{x}_{i}$ berasal dari komponen atau profil *k*. Berdasarkan aturan Bayes, rumusnya didefinisikan sebagai berikut (lihat Persamaan II-3) (Yehoshua, 2023):

$\gamma\left( z_{ik} \right) = \frac{w_{k}\mathcal{N}\left( x_{i};\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}{w_{j}\mathcal{N}\left( x_{i};\mu_{j},\Sigma_{j} \right)}}$ (II-3)

Keterangan:

> $\gamma\left( z_{ik} \right)$ = probabilitas posterior (*responsibilities*) bahwa observasi $i$ berasal dari profil $k$

2\. M-Step (*Maximization*):

Langkah ini memperbarui parameter model untuk memaksimalkan *expected log-likelihood* menggunakan bobot responsibilities yang diperoleh dari E-step. Pembaruan parameter dilakukan sebagai berikut (Yehoshua, 2023):

- Update Means ($\mu_{k}$) berdasarkan Persamaan II-4 berikut:

$\mu_{k}^{new} = \frac{\sum_{i = 1}^{n}{\gamma\left( z_{ik} \right)x_{i}}}{\sum_{i = 1}^{n}{\gamma\left( z_{ik} \right)}}$ (II-4)

Keterangan:

> $\mu_{k}^{new}$ = nilai mean (rata-rata) yang diperbarui untuk profil k
>
> $\gamma\left( z_{ik} \right)$ = *responsibilities* dari E-step sebagai pembobot

- Update Covariances ($\sum_{k}$) berdasarkan Persamaan II-5 berikut:

$\Sigma_{k}^{new} = \frac{\sum_{i = 1}^{n}{\gamma\left( z_{ik} \right)\left( x_{i} - \mu_{k}^{new} \right)\left( x_{i} - \mu_{k}^{new} \right)^{T}}}{\sum_{i = 1}^{n}{\gamma\left( z_{ik} \right)}}$ (II-5)

Keterangan:

> $\Sigma_{k}^{new}$ = matriks *covariance* yang diperbarui untuk profil k
>
> $\left( x_{i} - \mu_{k}^{new} \right)\left( x_{i} - \mu_{k}^{new} \right)^{T}$ = matriks outer product dari deviasi data terhadap mean
>
> $\gamma\left( z_{ik} \right)$ = bobot dari *responsibilities*

- Update Mixing Weights ($w_{k}$) berdasarkan Persamaan II-6 berikut:

$w_{k}^{new} = \frac{\sum_{i = 1}^{n}{\gamma\left( z_{ik} \right)}}{n}$ (II-6)

Keterangan:

> $w_{k}^{new}$ = *mixing weight* yang diperbarui untuk profil $k$ (proporsi populasi dalam profil $k$)

Proses iteratif algoritma EM dapat dipahami melalui flowchart pada Gambar II-3 berikut:

<figure>
<img src="media/image5.jpeg" style="width:3.72917in;height:2.38635in" alt="Flowchart algoritma EM" />
<figcaption><p><span id="_Toc225768970" class="anchor"></span>Gambar II‑3 <em>Flowchart</em> algoritma EM</p></figcaption>
</figure>

Sumber: Adipraja dkk. (2022)

Algoritma EM ini diulang hingga mencapai konvergensi, yang biasanya ditentukan ketika perubahan *log-likelihood* berada di bawah *threshold* tertentu atau mencapai jumlah iterasi maksimum (Yehoshua, 2023).

Dari perspektif *machine learning* dan komputasi (Python), LPA secara matematis adalah Gaussian Mixture Model, model probabilistik yang merepresentasikan data sebagai *mixture* dari $K$ distribusi Gaussian multivariat (Yehoshua, 2023). Implementasi GMM dalam *library* scikit-learn menggunakan *class* GaussianMixture, yang menggunakan EM *algorithm* untuk *fitting* (Yehoshua, 2023).

Keunggulan LPA untuk data kepribadian (Ferguson dkk., 2020; Spurk dkk., 2020):

1.  *Soft Classification*: Menghasilkan probabilitas keanggotaan, bukan penugasan *hard*. Ini sesuai dengan nature kepribadian manusia yang kompleks dan *overlapping*.

2.  *Probabilistic Framework*: Berbasis teori distribusi probabilitas, memungkinkan *inference* statistik formal.

3.  Interpretabilitas: Output berupa profil deskriptif dengan *mean* dan *varians* per profil, mudah dikomunikasikan.

4.  *Fleksibilitas Covariance*: Dapat memodelkan *covariance* yang berbeda per profil (*tied vs. untied*), mencerminkan heteroskedastisitas alami.

Hasil profiling dari LPA dapat divisualisasikan dalam bentuk profile plot yang menunjukkan mean skor per profil, seperti contoh berikut (Gambar II-4):

<figure>
<figcaption><p><span id="_Toc225768971" class="anchor"></span>Gambar II‑4 Contoh visualisasi <em>profile</em> <em>means</em> dari <em>Latent Profile Analysis</em> pada studi <em>mental health risk profiling</em></p></figcaption>
</figure>

Sumber: Guelmami dkk. (2022)

Menentukan jumlah profil optimal (*k*) adalah tantangan utama dalam *Latent Profile Analysis* (LPA). Literatur merekomendasikan pendekatan *multi-criteria* yang melibatkan berbagai indeks evaluasi (Pan dkk., 2024). Berikut adalah metrik evaluasi yang biasa digunakan:

1\. Akaike *Information Criterion* (AIC)

AIC digunakan untuk menyeimbangkan *goodness of fit* model dengan kompleksitasnya. Nilai AIC yang lebih rendah mengindikasikan model yang lebih baik. Rumusnya didefinisikan sebagai berikut (lihat Persamaan II-7) (Yehoshua, 2023):

$AIC = 2m - 2\, l\left( \widehat{\theta} \right)$ (II-7)

Keterangan:

> $m$ = jumlah parameter yang diestimasi dalam model
>
> $l\left( \widehat{\theta} \right)$ = nilai *log-likelihood* maksimal

Di mana *m* adalah jumlah parameter yang diestimasi dalam model dan <img src="media/image7.png" title="l left parenthesis theta with hat on top right parenthesis" style="width:0.33019in;height:0.18379in" alt="{&quot;mathml&quot;:&quot;&lt;math style=\&quot;font-family:stix;font-size:16px;\&quot; xmlns=\&quot;http://www.w3.org/1998/Math/MathML\&quot;&gt;&lt;mi&gt;l&lt;/mi&gt;&lt;mo&gt;(&lt;/mo&gt;&lt;mover&gt;&lt;mi&gt;&amp;#x3B8;&lt;/mi&gt;&lt;mo&gt;^&lt;/mo&gt;&lt;/mover&gt;&lt;mo&gt;)&lt;/mo&gt;&lt;/math&gt;&quot;,&quot;origin&quot;:&quot;MathType Legacy&quot;,&quot;version&quot;:&quot;v3.20.0&quot;}" /> adalah nilai *log-likelihood* maksimal. AIC memberikan penalti moderat terhadap penambahan parameter untuk mencegah *overfitting*.

2\. Bayesian *Information Criterion* (BIC)

Serupa dengan AIC, BIC juga menyeimbangkan kesesuaian model dan kompleksitas, namun memberikan penalti yang lebih ketat terhadap jumlah parameter karena melibatkan ukuran sampel (*n*). Rumusnya adalah sebagai berikut (lihat Persamaan II-8) (Yehoshua, 2023):

$BIC = m\ln(n) - 2l\left( \widehat{\theta} \right)$ (II-8)

Keterangan:

> $m$ = jumlah parameter yang diestimasi dalam model
>
> $n$ = jumlah total observasi
>
> $l\left( \widehat{\theta} \right)$ = nilai *log-likelihood* maksimal

Karena faktor $In(n)$, BIC cenderung memilih model yang lebih sederhana (*parsimonious*) dibandingkan AIC. Dalam banyak kasus, BIC sering dijadikan kriteria utama dalam pemilihan *k* optimal karena penaltinya yang lebih kuat terhadap kompleksitas model.

3\. Entropy *Measure*

Entropy mengukur ketepatan klasifikasi individu ke dalam profil laten. Rumus entropy untuk *n* individu dan *k* profil adalah sebagai berikut (lihat Persamaan II-9):

$Entropy = - \frac{1}{n}\sum_{i = 1}^{n}{\sum_{k = 1}^{K}\left( \widehat{z_{ik}} \times \ln\left( \widehat{z_{ik}} \right) \right)}$ (II-9)

Keterangan:

> $n$ = jumlah observasi
>
> $K$ = jumlah profil
>
> $\widehat{z_{ik}}$ = probabilitas posterior (responsibilities) bahwa observasi i berasal dari profil $k$

Rentang nilai entropy berkisar antara 0 hingga 1. Nilai entropy mendekati 1 (khususnya \> 0.80) menunjukkan klasifikasi yang reliabel, yang berarti individu dapat diklasifikasi dengan tingkat kepercayaan (*confidence*) tinggi ke dalam profil masing-masing (Ferguson dkk., 2020).

4\. *Bootstrapped Likelihood Ratio Test* (BLRT)

BLRT digunakan untuk menguji apakah model dengan *k* profil secara statistik signifikan lebih baik daripada model dengan *k*-1 profil. Rumus *Likelihood Ratio Test* (LRT) dasar didefinisikan sebagai berikut (lihat Persamaan II-10):

$LRT = - 2\left\lbrack l\left( \widehat{\theta_{k - 1}} \right) - l\left( \widehat{\theta_{k}} \right) \right\rbrack$ (II-10)

Keterangan:

> $l\left( \widehat{\theta_{k - 1}} \right)$ = log-likelihood model dengan k-1 profil
>
> $l\left( \widehat{\theta_{k}} \right)$ = log-likelihood model dengan k profil
>
> Nilai LRT positif menunjukkan model dengan k profil lebih fit
>
> Pada BLRT, nilai p \< 0.05 menunjukkan signifikansi penambahan profil

Nilai p \< 0.05 pada BLRT menunjukkan bahwa penambahan profil memberikan peningkatan *fit* model yang signifikan, sehingga model yang lebih kompleks (dengan *k* profil) lebih didukung (Ferguson dkk., 2020).

5\. *Silhouette Score*

*Silhouette Score* merupakan metode yang digunakan untuk menilai kualitas pengelompokan (*clustering*) dengan mengukur seberapa baik suatu objek ditempatkan dalam klasternya sendiri dibandingkan dengan klaster lain (seberapa *well-defined* profil tersebut). Secara matematis, skor untuk setiap titik data $i$ dihitung berdasarkan perbandingan antara jarak rata-rata intra-klaster $c(i)$ dan jarak rata-rata inter-klaster minimum ke klaster terdekat $d(i)$, dengan rumus sebagai berikut (lihat Persamaan II-11) (Khan dkk., 2025):

$S(i) = \frac{d(i) - c(i)}{\max\left( c(i),d(i) \right)}$ (II-11)

Rentang nilainya berada pada interval $\lbrack - 1,1\rbrack$. Nilai yang mendekati 1 (umumnya $> \ 0.5$) menunjukkan bahwa titik data tersebut telah terklaster dengan baik dan terpisah tegas dari profil lain (*well-separated*). Sebaliknya, nilai 0 mengindikasikan bahwa titik data berada pada perbatasan antar klaster, sementara nilai mendekati $- 1$ menunjukkan kemungkinan kesalahan klasifikasi karena titik tersebut lebih dekat dengan klaster lain daripada klasternya sendiri (Khan dkk., 2025). Dalam konteks *Latent Profile Analysis* (LPA), metrik ini digunakan sebagai pembanding tambahan untuk memberikan konfirmasi terhadap ketegasan struktur profil, namun bukan merupakan kriteria utama dalam pengambilan keputusan.

Untuk prosedur pemilihan *k* optimal, model dengan *k* = 1, 2, 3, 4, 5 diestimasi secara berurutan. Untuk setiap *k*, dihitung nilai AIC, BIC, Entropy, dan BLRT. Prosedur *elbow informal* (mengamati titik penurunan tajam pada plot AIC/BIC) dikombinasikan dengan pemeriksaan Entropy dan BLRT untuk menentukan *k* optimal. Direkomendasikan agar memilih *k* dengan nilai AIC/BIC terendah (atau titik *elbow*), Entropy ≥ 0.80, BLRT signifikan (p \< 0.05), dan ukuran setiap profil (proporsi sampel) bernilai \> 5% dari total *n* untuk memastikan stabilitas profil (Pan dkk., 2024). Prosedur pemilihan *k* optimal dapat divisualisasikan melalui elbow plot pada gambar II-5 berikut, di mana penurunan nilai AIC/BIC mengindikasikan model yang lebih fit.

<figure>
<figcaption><p><span id="_Toc225768972" class="anchor"></span>Gambar II‑5 Contoh <em>Elbow Plot</em> untuk Pemilihan Jumlah Profil Optimal</p></figcaption>
</figure>

Sumber: (Zhong dkk., 2024)

### *Measurement Invariance*

*Measurement Invariance* (MI), atau sering disebut sebagai *factorial invariance*, adalah konsep fundamental dalam psikometri yang menjamin bahwa instrumen pengukuran berfungsi secara setara di berbagai subkelompok populasi yang berbeda (Freilich dkk., 2023). Dalam studi komparatif, validitas perbandingan skor antar kelompok (seperti gender, budaya, atau usia) sangat bergantung pada asumsi bahwa konstruksi psikologis yang diukur memiliki makna dan struktur yang sama bagi seluruh responden. Tanpa terbuktinya invariansi, perbedaan skor yang ditemukan mungkin bukan mencerminkan perbedaan sifat asli (*true trait differences*), melainkan akibat bias pengukuran atau perbedaan interpretasi item antar kelompok (Kline, 2023).

Secara teoritis, pengujian *measurement invariance* dilakukan melalui pendekatan analisis faktor konfirmatori multi-grup (*Multi-Group Confirmatory Factor Analysis*) yang mengikuti tahapan hierarkis ketat secara sekuensial, di mana setiap tingkatan memberlakukan konstrain statistik yang semakin restriktif **(**Fischer & Karl, 2019). Tingkatan invariansi tersebut dijabarkan sebagai berikut:

1.  *Configural Invariance*: Merupakan tahap dasar untuk memastikan bahwa struktur faktor (pola *loading* butir instrumen laten) berlaku konseptual sama lintas kelompok. Pada tahap ini, *magnitude loading* dan *intercept* dibiarkan bebas bervariasi. Jika model ini mencapai *fit* yang baik, maka populasi yang berbeda mengonseptualisasikan konstruk kepribadian dengan cara yang sama.

2.  *Metric (Weak) Invariance*: Menguji kesetaraan metrik dengan membatasi (*constraining*) nilai *factor loading* agar bernilai sama lintas kelompok, di luar struktur pola yang sudah ada. Tahap ini memastikan bahwa setiap butir instrumen mengukur dimensi laten dengan sensitivitas (*scaling*) yang setara di semua kelompok demografis.

3.  *Scalar (Strong) Invariance*: Tahap krusial di mana *factor loading* beserta titik potong respons (*item intercept*) dikonstrain agar bernilai sama lintas kelompok. Pemenuhan invariansi skalar membuktikan bahwa tidak ada bias sistematis dalam merespons instrumen, sehingga perbedaan nilai rata-rata observasi (*observed means*) yang muncul antar kelompok demografis benar-benar merefleksikan perbedaan sifat asli (*true trait differences*), bukan akibat bias instrumen.

Ketiga tingkat invariansi ini dapat direpresentasikan dalam bentuk hierarki sebagai berikut (Gambar II-6):

<figure>
<figcaption><p><span id="_Toc225768973" class="anchor"></span>Gambar II‑6 Hierarki Tingkat <em>Measurement Invariance</em> dalam CFA <em>Multi-Group</em></p></figcaption>
</figure>

Sumber: Fischer & Karl (2019)

Evaluasi terhadap pemenuhan asumsi invariansi pada setiap tingkatan tersebut didasarkan pada kriteria statistik *goodness-of-fit*. Literatur terkini menegaskan kembali penggunaan ambang batas standar untuk menerima hipotesis invariansi pada sampel besar (Kline, 2023). Model yang lebih ketat (*constrained*) dapat dianggap invarian jika penurunan kualitas model masih berada dalam batas toleransi, yang ditandai dengan perubahan nilai *Comparative Fit Index* (ΔCFI) tidak melebihi -0.010 dan perubahan *Root Mean Square Error of Approximation* (ΔRMSEA) tidak melebihi 0.015 dibandingkan model tahapan sebelumnya (Kline, 2023; Sterner dkk., 2025).

### *Decision Support System*

Penerapan hasil analisis profil psikologis memerlukan jembatan komunikasi yang efektif agar dapat dipahami oleh pemangku kepentingan non-teknis. Dalam konteks ini, Sistem Pendukung Keputusan (*Decision Support System*/DSS) berperan krusial sebagai instrumen yang mentransformasi data statistik kompleks menjadi wawasan praktis yang mendukung pengambilan kebijakan strategis (San Cornelio dkk., 2025).

Salah satu bentuk implementasi DSS modern adalah melalui antarmuka *dashboard* interaktif. Agar DSS dapat berfungsi optimal dalam menyampaikan informasi, desain visualisasinya harus mematuhi prinsip pengurangan beban kognitif (*cognitive load reduction*) dan hierarki informasi yang jelas. Prinsip ini diterapkan melalui pemilihan enkoding visual yang tepat sasaran, seperti penggunaan grafik distribusi untuk perbandingan lintas kelompok, *radar chart* untuk pemetaan profil multidimensi, serta tabel kontingensi untuk rincian demografis. Visualisasi yang terstruktur membantu pengguna mengidentifikasi pola dan anomali secara *real-time* tanpa terbebani oleh kompleksitas matematis di balik model (San Cornelio dkk., 2025).

Dari sisi teknologi pengembangan, implementasi DSS kini didukung oleh kerangka kerja berbasis web (*web-based frameworks*) seperti *Streamlit*. Teknologi ini memfasilitasi pembuatan aplikasi data yang cepat (*rapid prototyping*) dengan menyediakan komponen interaktif (*widgets*) seperti *slider* dan *dropdown*. Fitur-fitur ini memungkinkan mekanisme *filtering* data dinamis dan *live replotting*, sehingga pengguna akhir dapat melakukan eksplorasi data secara mandiri dan memperoleh rekomendasi tindakan (*actionable insights*) yang presisi (Akkem dkk., 2023).

## Penelitian Terdahulu *(State of the Art)*

Penelitian mengenai *personality profiling* di kalangan mahasiswa menggunakan berbagai pendekatan metode. Berikut adalah tinjauan sistematis penelitian-penelitian terkait:

<table>
<caption><p><span id="_Toc225768980" class="anchor"></span>Tabel II‑3 Posisi Penelitian (<em>State of The Art)</em></p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>No</strong></th>
<th style="text-align: center;"><em><strong>Author</strong></em></th>
<th style="text-align: center;"><strong>Metode</strong></th>
<th style="text-align: center;"><strong>Fokus Penelitian</strong></th>
<th style="text-align: center;"><strong>Hasil</strong></th>
<th style="text-align: center;"><strong>Kekuatan</strong></th>
<th style="text-align: center;"><strong>Kekurangan</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Pan et dkk. (2024)</td>
<td style="text-align: left;">Latent Profile Analysis (LPA) pada instrumen EPQ</td>
<td style="text-align: left;">Mengidentifikasi profil kepribadian dan hubungannya dengan resiliensi psikologis pada mahasiswa.</td>
<td style="text-align: left;">• Ditemukan 3 profil kepribadian dengan pola berbeda pada resiliensi psikologis dan dukungan sosial.<br />
• Pendekatan berpusat pada orang untuk pengelompokan kepribadian.</td>
<td style="text-align: left;">• Metodologi LPA yang kuat untuk pembuatan profil kepribadian.<br />
• Menggunakan pendekatan berpusat pada individu.<br />
• Mengidentifikasi profil yang berbeda.</td>
<td style="text-align: left;">• Menggunakan EPQ (4 dimensi) dan bukan inventori komprehensif seperti OMNI.<br />
• Tidak fokus pada luaran kesehatan mental.</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Kokkinos dkk. (2024)</td>
<td style="text-align: left;">• Latent Profile Analysis pada Big Five Model<br />
• ANOVA lintas kelompok</td>
<td style="text-align: left;">Mengidentifikasi profil kepribadian lintas program studi dan hubungannya dengan penyesuaian psikologis mahasiswa.</td>
<td style="text-align: left;">• 4 profil kepribadian teridentifikasi dengan perbedaan signifikan lintas program studi berdasarkan efek <em>selective entry.</em><br />
• Profil kepribadian berhubungan dengan konstruk psikologis yang berbeda.</td>
<td style="text-align: left;">• LPA untuk mengidentifikasi profil kepribadian berbeda.<br />
• Analisis berpusat pada individu.<br />
• Memeriksa efek <em>selective entry</em> lintas disiplin ilmu.<br />
• Relevan untuk konteks universitas.</td>
<td style="text-align: left;">• Menggunakan hanya 5 dimensi Big Five bukan inventaris kepribadian komprehensif.<br />
• Tidak spesifik untuk desain intervensi kesehatan mental.</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Guelmami dkk. (2022)</td>
<td style="text-align: left;">Latent Class Analysis (LCA) dengan model <em>dual-factor</em> kesehatan mental</td>
<td style="text-align: left;">Mengidentifikasi profil kesehatan mental berdasarkan integrasi psikopatologi dan kesejahteraan pada mahasiswa Tunisia.</td>
<td style="text-align: left;">• 3 kelas kesehatan mental yang berbeda teridentifikasi yaitu <em>flourishing, moderate,</em> dan <em>at-risk.</em><br />
• Profil berpusat pada individu lebih efektif daripada pendekatan berpusat pada variabel untuk skrining kesehatan mental.</td>
<td style="text-align: left;">• Pendekatan berpusat pada individu untuk profil kesehatan mental.<br />
• Mengintegrasikan psikopatologi dan kesejahteraan (<em>dual-factor model</em>).<br />
• Karakterisasi profil yang bermakna.</td>
<td style="text-align: left;">• Tidak menggunakan inventaris kepribadian sebagai masukan.<br />
• Fokus pada hasil kesehatan mental saja bukan <em>antecedents</em> kepribadian sebagai prediktor.</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Chen dkk. (2025)</td>
<td style="text-align: left;">Latent Profile Analysis (LPA) ditambah regresi logistik multinomial dengan model <em>dual-factor</em></td>
<td style="text-align: left;">Mengidentifikasi profil kesehatan mental pada mahasiswa <em>fresh generation</em> dan memeriksa kepribadian proaktif serta lingkungan universitas sebagai prediktor.</td>
<td style="text-align: left;">• 4 profil kesehatan mental teridentifikasi yaitu <em>flourishing, moderate, content-dominated</em> dengan <em>symptoms</em>, dan <em>symptoms-dominated</em> dengan <em>content.</em><br />
• Kepribadian proaktif dan lingkungan universitas ditemukan sebagai prediktor signifikan.</td>
<td style="text-align: left;">• Profil kesehatan mental <em>dual-factor</em> berpusat pada individu.<br />
• Metodologi LPA.<br />
• Memeriksa ciri kepribadian dan faktor lingkungan sebagai prediktor.<br />
• Penelitian terbaru.</td>
<td style="text-align: left;">• Fokus pada kepribadian proaktif (hanya 1 ciri) bukan penilaian kepribadian komprehensif seperti OMNI.<br />
• Hanya mahasiswa generasi pertama bukan seluruh populasi.</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Xiao dkk. (2021)</td>
<td style="text-align: left;"><em>Structural Equation Modeling</em> ditambah pengelompokan kategorikal dengan validasi model <em>dual-factor</em></td>
<td style="text-align: left;">Memvalidasi model <em>dual-factor</em> untuk skrining kesehatan mental mahasiswa perguruan tinggi dengan mengintegrasikan kesejahteraan dan psikopatologi .untuk mengidentifikasi kebutuhan intervensi</td>
<td style="text-align: left;">• 4 sampai 6 kategori kesehatan mental berbeda teridentifikasi.<br />
• Model <em>dual-factor</em> valid dan lebih efektif dibanding pendekatan psikopatologi saja untuk skrining dan stratifikasi.</td>
<td style="text-align: left;">• Kerangka kerja foundational untuk model <em>dual-factor.</em><br />
• Validasi pada sampel besar (N=2065).<br />
• Menyediakan kerangka skrining berbasis bukti.</td>
<td style="text-align: left;">• Tidak menggunakan inventaris kepribadian.<br />
• Tidak menggunakan pengelompokan berpusat pada individu.<br />
• Pendekatan berpusat pada variabel.</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Pecora dkk. (2025)</td>
<td style="text-align: left;">Latent Profile Analysis (LPA) dengan memeriksa hubungan antara profil dan faktor risiko</td>
<td style="text-align: left;">Mengidentifikasi profil fungsi psikologis selama pandemi dan konfigurasi kerentanan pada remaja dan dewasa muda.</td>
<td style="text-align: left;">• 3 profil risiko teridentifikasi <em>(low-risk, mild-risk, high-risk</em>) dengan pola berbeda pada psikopatologi, kesejahteraan, dan mekanisme <em>coping.</em><br />
• LPA efektif untuk stratifikasi risiko.</td>
<td style="text-align: left;">• LPA untuk profil fungsi psikologis.<br />
• Stratifikasi risiko berpusat pada individu.<br />
• Mengidentifikasi pola kerentanan yang berbeda.<br />
• Menggunakan <em>multiple</em> indikator psikologis.</td>
<td style="text-align: left;">• Populasi remaja bukan mahasiswa perguruan tinggi.<br />
• Tidak fokus pada <em>antecedents</em> kepribadian.<br />
• Tidak ditujukan untuk desain program pencegahan.</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Newton dkk. (2022)</td>
<td style="text-align: left;">• Cluster Randomized Controlled Trial (cRCT) dengan intervensi kepribadian yang ditargetkan<br />
• <em>Longitudinal follow-up</em> 7 tahun</td>
<td style="text-align: left;">Program PreVenture yaitu 2-<em>session brief</em> intervensi pencegahan selektif berbasis kepribadian yang menargetkan 4 ciri risiko kepribadian yaitu <em>anxiety sensitivity, negative thinking, impulsivity, sensation seeking</em> untuk pencegahan penggunaan alcohol.</td>
<td style="text-align: left;">• Data <em>follow-up</em> 7 tahun menunjukkan efek berkelanjutan intervensi pada pengurangan pertumbuhan penggunaan alkohol berisiko.<br />
• Pencegahan selektif berbasis kepribadian layak dan efektif.</td>
<td style="text-align: left;">• Desain pencegahan selektif target kepribadian berbasis bukti.<br />
• Menargetkan profil kepribadian spesifik dengan pelatihan <em>coping</em> <em>skills.</em><br />
• Data longitudinal 7 tahun untuk <em>sustainability.</em><br />
• Menunjukkan <em>feasibility</em> intervensi berbasis kepribadian.</td>
<td style="text-align: left;">• Fokus pencegahan alkohol bukan promosi kesehatan mental umum.<br />
• Populasi remaja bukan mahasiswa.<br />
• Menargetkan hanya 4 ciri spesifik bukan penilaian komprehensif.</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">Choi dkk. (2024)</td>
<td style="text-align: left;">• Desain <em>personalized feedback</em> berdasarkan profil kepribadian<br />
• <em>Pilot testing</em></td>
<td style="text-align: left;">Program <em>Personalized Feedback</em> Program menargetkan jalur risiko kepribadian yang dipengaruhi secara genetik yaitu <em>Sensation Seeking, Impulsivity, Extraversion, Neuroticism</em> dengan <em>online personalized feedback</em> dan integrasi <em>resources</em> kampus.</td>
<td style="text-align: left;">• Program layak dan dapat diterima (<em>feasible and acceptable</em>)<br />
• Indikasi awal pengurangan perilaku penggunaan zat berisiko.<br />
• Stratifikasi berbasis kepribadian dapat diintegrasikan dengan sumber daya kampus.</td>
<td style="text-align: left;">• Desain umpan balik target kepribadian.<br />
• Menargetkan ciri kepribadian dimensional (mirip dimensi OMNI).<br />
• Integrasi dengan sumber daya kampus.<br />
• Rekomendasi terpersonalisasi.</td>
<td style="text-align: left;">• Hasil masih tahap awal.<br />
• Fokus pencegahan penggunaan zat bukan promosi kesehatan mental secara umum.<br />
• Data efektivitas masih awal (<em>preliminary</em>).</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: center;">Magalhães (2024)</td>
<td style="text-align: left;"><em>Systematic review</em> ditambah synthesis dan analisis kerangka kerja teoritis</td>
<td style="text-align: left;">Tinjauan komprehensif model kesehatan mental <em>dual-factor</em> dalam penelitian dan praktik serta identifikasi pendekatan kategorisasi optimal.</td>
<td style="text-align: left;">• Sintesis dari 50 lebih studi.<br />
• Mengidentifikasi superioritas <em>dual-factor</em> dibanding model tradisional hanya psikopatologi.<br />
• Menyediakan kerangka berbasis bukti untuk profil kesehatan mental.</td>
<td style="text-align: left;">• Kerangka kerja teoretis dasar<br />
• Tinjauan komprehensif model <em>dual-factor.</em><br />
• Mengidentifikasi pendekatan optimal untuk kategorisasi.<br />
• Memvalidasi superioritas pendekatan <em>dual-factor.</em></td>
<td style="text-align: left;">• Merupakan makalah tinjauan (<em>review paper</em>) bukan penelitian empiris<br />
• Tidak fokus pada <em>antecedents</em> kepribadian.<br />
• Sintesis dari konteks yang beragam.</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;">Moggia dkk. (2024)</td>
<td style="text-align: left;"><em>Narrative review</em> ditambah synthesis meta-analitik dari <em>literature</em> dan <em>clinical examples</em></td>
<td style="text-align: left;"><em>Treatment Personalization and Precision Mental Health Care</em>: Gambaran komprehensif pendekatan pencocokan profil pasien dengan perawatan terpersonalisasi.</td>
<td style="text-align: left;">• Konseptualisasi kesehatan mental presisi sebagai pencocokan profil pasien dengan perawatan.<br />
• Pendekatan perawatan berbasis pengukuran.<br />
• Contoh sistem pendukung keputusan (DSS) dan algoritma personalisasi.</td>
<td style="text-align: left;">• Kerangka kritis untuk intervensi berbasis data.<br />
• Perspektif perawatan berbasis pengukuran.<br />
• Contoh implementasi DSS.<br />
• Landasan teoretis untuk rekomendasi terpersonalisasi.</td>
<td style="text-align: left;">• Makalah tinjauan bukan penelitian empiris.<br />
• Belum ada implementasi spesifik dengan profil kepribadian di konteks universitas.</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;">Gholami dkk. (2025)</td>
<td style="text-align: left;">• <em>Mixed methods</em> (kuantitatif &amp; kualitatif <em>co-design</em>)<br />
• <em>Pilot testing</em> dengan <em>human-centered design</em></td>
<td style="text-align: left;">Pengembangan dan pengujian aplikasi kesehatan mental mahasiswa terpersonalisasi yang mengintegrasikan data HER untuk intervensi <em>personalized</em> di universitas.</td>
<td style="text-align: left;">• Kerangka kerja desain aplikasi selesai dengan perbaikan iteratif.<br />
• <em>Co-design</em> dengan mahasiswa menghasilkan 7 fitur personalisasi inti.<br />
• Partisipasi &gt;600 mahasiswa baru/pindahan/medis.</td>
<td style="text-align: left;">• Desain aplikasi berpusat pada mahasiswa dengan personalisasi.<br />
• Integrasi dengan sumber daya kampus dan EHR.<br />
• Perbaikan iteratif dengan masukan pengguna.<br />
• Protokol terbaru (2025).</td>
<td style="text-align: left;">• Masih tahap pengembangan (belum ada analisis lengkap).<br />
• Tidak spesifik berbasis kepribadian.<br />
• Pendekatan personalisasi umum.</td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td style="text-align: center;">Buschmeyer dkk. (2023)</td>
<td style="text-align: left;">• Pengembangan skala (kuesioner PAAI)<br />
• Validasi <em>Confirmatory Factor Analysis</em> (CFA)</td>
<td style="text-align: left;"><em>Psychological Assessment of AI-based Decision Support Systems</em> yaitu <em>development</em> dan <em>validation</em> PAAI <em>questionnaire</em> untuk mengevaluasi DSS dari perspektif <em>psychological user.</em></td>
<td style="text-align: left;">• Kuesioner PAAI dengan 5 faktor (kualitas keputusan, transparansi, kepercayaan, kegunaan, otonomi) menunjukkan properti psikometrik baik.<br />
• Dapat diterapkan untuk beragam DSS.</td>
<td style="text-align: left;">• Kerangka evaluasi pengalaman pengguna dan dampak psikologis DSS.<br />
• Validasi desain berpusat pada manusia.<br />
• Alat ukur tervalidasi CFA.<br />
• Relevan untuk konteks psikologi/kesehatan mental.</td>
<td style="text-align: left;">• Alat ukur masih relatif baru.<br />
• Belum diuji ekstensif dalam konteks psikologi/kesehatan mental khusus.</td>
</tr>
<tr>
<td style="text-align: center;">13</td>
<td style="text-align: center;">Madrid-Cagigal dkk. (2025)</td>
<td style="text-align: left;"><em>Systematic review</em> ditambah <em>meta-analysis</em> dari <em>randomized controlled trials</em> (RCT)</td>
<td style="text-align: left;"><em>Digital Mental Health Interventions</em> untuk <em>University Students</em> yaitu <em>systematic review</em> ditambah <em>meta-analysis effectiveness</em> dari DMHIs untuk <em>anxiety</em> dan <em>depression.</em></td>
<td style="text-align: left;">• Meta-analisis dari lebih dari 30 RCTs (ribuan mahasiswa).<br />
• Bukti kuat efektivitas intervensi digital (SMD -0.45 kecemasan, -0.52 depresi).<br />
• Intervensi terpandu lebih efektif dibanding otomatis.</td>
<td style="text-align: left;">• Basis bukti kuat penyampaian intervensi digital pada mahasiswa.<br />
• Mengidentifikasi moderator (terpandu vs otomatis).<br />
• Rekomendasi implementasi.</td>
<td style="text-align: left;">• Meta-analisis umum bukan spesifik kepribadian.<br />
• Jenis intervensi beragam (tidak khusus target kepribadian).</td>
</tr>
<tr>
<td style="text-align: center;">14</td>
<td style="text-align: center;">Nosè dkk. (2025)</td>
<td style="text-align: left;">• <em>Randomized Controlled Trial</em> (RCT)<br />
• Uji efektivitas (akseptabilitas, kesesuaian, kelayakan)</td>
<td style="text-align: left;">Efektivitas intervensi WHO "Doing What Matters in Times of Stress" untuk promosi kesehatan mental universal pada mahasiswa.</td>
<td style="text-align: left;">• Akseptabilitas dan kesesuaian kuat di populasi universitas beragam.<br />
• Pengurangan signifikan distres psikologis (Cohen's d=0.45).<br />
• Pendekatan universal bermanfaat bagi semua mahasiswa.</td>
<td style="text-align: left;">• Bukti intervensi kesehatan mental universal.<br />
• Pendekatan terskala (<em>scalable</em>).<br />
• Menunjukkan manfaat pencegahan universal.<br />
• Konteks Italia.</td>
<td style="text-align: left;">• Belum terstratifikasi kepribadian.<br />
• Pendekatan pencegahan universal (bukan target).<br />
• Tidak ada stratifikasi berbasis kepribadian.</td>
</tr>
<tr>
<td style="text-align: center;">15</td>
<td style="text-align: center;">Webster dkk. (2025)</td>
<td style="text-align: left;"><em>Person-centered clustering approach</em> dengan <em>cross-demographic comparison</em></td>
<td style="text-align: left;">Profil Kesehatan Mental Mahasiswa dan Hubungannya dengan perilaku kesehatan (mengidentifikasi pengelompokan dan pola lintas demografi).</td>
<td style="text-align: left;">• Profil kesehatan mental teridentifikasi dengan perbedaan signifikan lintas demografi.<br />
• Pola jelas antara profil kesehatan mental, perilaku kesehatan, dan performa akademik.</td>
<td style="text-align: left;">• Profil berpusat pada individu untuk kesehatan mental.<br />
• Memeriksa variasi demografi.<br />
• Mengidentifikasi pola perilaku kesehatan yang bermakna.<br />
• Studi terbaru.</td>
<td style="text-align: left;">• Hasil publikasi masih terbatas.<br />
• Belum spesifik detail lengkap.<br />
• Lebih ke kesehatan mental umum bukan berbasis kepribadian.</td>
</tr>
<tr>
<td style="text-align: center;">16</td>
<td style="text-align: center;">Penelitian Ini</td>
<td style="text-align: left;">• Latent Profile Analysis (LPA)<br />
• <em>Measurement Invariance Testing</em><br />
• <em>Dual-Factor Mental Health Model</em><br />
• <em>Interactive Dashboard DSS</em></td>
<td style="text-align: left;">Pemetaan Profil Kepribadian Mahasiswa Berbasis OMNI melalui Latent Profile Analysis Sebagai Dasar Strategi Promosi Kesehatan Mental di Universitas.</td>
<td style="text-align: left;">• Diharapkan menghasilkan identifikasi 3 sampai 5 profil kepribadian berdasarkan 25 normal ditambah 10 <em>personality disorder scales</em> OMNI.<br />
• Validasi <em>Measurement Invariance</em> lintas gender, prodi, angkatan.<br />
• Pemetaan distribusi profil dan hubungan dengan kesehatan mental <em>dual-factor.</em><br />
• Rekomendasi strategi promosi terpersonalisasi.<br />
• Visualisasi DSS interaktif.</td>
<td style="text-align: left;">Sintesis &amp; Integrasi:<br />
• Studi pertama yang mengintegrasikan OMNI dengan pengujian <em>Measurement Invariance</em> ketat (konfigural, metrik, skalar) untuk AI yang bertanggung jawab.<br />
• Integrasi profil kepribadian dengan model <em>dual-factor.</em><br />
• Profil berpusat pada individu dengan rekomendasi yang dapat ditindaklanjuti.<br />
• Implementasi praktis via dasbor DSS.<br />
• Konteks institusi Indonesia.</td>
<td style="text-align: left;">Kontribusi Mengisi Celah:<br />
• Penilaian kepribadian komprehensif (mengintegrasikan spektrum normal dan patologis) dibanding EPQ/Big Five sebelumnya.<br />
• Pengujian invarian pengukuran untuk perbandingan lintas kelompok yang adil.<br />
• Menggali anteseden kepribadian untuk kesehatan mental yang belum ada.<br />
• Implementasi praktis DSS.<br />
• Konteks universitas lokal di Indonesia.</td>
</tr>
</tbody>
</table>

Berdasarkan tabel perbandingan di atas, penelitian ini menunjukkan beberapa *positioning* yang unik:

- Menggunakan instrumen OMNI yang lebih komprehensif (375 item; 25 skala normal; 10 skala abnormal) dibanding EPQ, TIPI, atau Big Five untuk mengidentifikasi profil kepribadian multidimensional yang lebih detail (Guess, 2006).

- Mengombinasikan LPA dan GMM serta menambahkan *measurement invariance testing* lintas kelompok demografis untuk memastikan perbedaan profil merefleksikan perbedaan sejati, bukan bias pengukuran (Guelmami dkk., 2022; Pan dkk., 2024).

- Berfokus pada *universal prevention* dan perancangan program (program design) yang terdiferensiasi berdasarkan profil, bukan semata *job matching* atau *risk prediction* klinis (Keane, 2023).

- Mengangkat konteks Indonesia dan pendidikan tinggi, mengingat studi *personality profiling* berbasis LPA di universitas Indonesia masih terbatas dan membutuhkan data lokal yang relevan (Mason dkk., 2025).

- Mengintegrasikan prinsip *Responsible AI* melalui transparansi algoritma, *measurement invariance testing* untuk aspek keadilan, perlindungan privasi data, dan *human oversight* (Keane, 2023).

- Melakukan analisis multi-level: (a) *population-level profiling*, (b) analisis terstratifikasi lintas kelompok demografis, (c) *measurement invariance testing*, dan (d) rekomendasi program, untuk menghasilkan pemahaman yang lebih komprehensif dibanding studi sebelumnya (Ferguson dkk., 2020).**\**

# METODE PENYELESAIAN MASALAH

## Metode Penelitian

Penelitian ini menggunakan pendekatan kuantitatif dengan desain non-eksperimental. Kerangka kerja metodologis yang digunakan mengacu pada standar industri CRISP-DM (*Cross-Industry Standard Process for Data Mining*). Pendekatan ini dipilih karena menyediakan siklus hidup analitik yang iteratif, dimulai dari pemahaman kebutuhan institusi hingga implementasi solusi nyata berupa strategi intervensi.

Berbeda dengan pendekatan pengembangan sistem konvensional, penelitian ini berfokus pada ekstraksi pola data laten. Oleh karena itu, metode analisis inti yang digunakan adalah *Latent Profile Analysis* (LPA) dengan algoritma *Gaussian Mixture Model* (GMM). Algoritma ini diimplementasikan untuk melakukan pengelompokan probabilistik (*soft clustering*) yang mampu menangkap karakteristik data kepribadian yang bersifat multidimensional dan beririsan (*overlapping*). Sistem akhir diposisikan sebagai Sistem Pendukung Keputusan (*Decision Support System*) yang memberikan rekomendasi berbasis data bagi pemangku kepentingan di kampus (seperti dosen wali dan psikolog).

## Sistematika Penyelesaian Masalah

Untuk memperjelas langkah-langkah penelitian, alur penyelesaian masalah digambarkan dalam bentuk diagram alir (*flowchart*) yang mengacu pada siklus CRISP-DM dengan penyesuaian konteks data OMNI. Tahapan ini memastikan proses dari data mentah hingga menjadi strategi intervensi berjalan sistematis yang diilustrasikan secara detail pada Gambar III-1 berikut.

<figure>
<img src="media/image10.png" style="width:5.50591in;height:7.34653in" />
<figcaption><p><span id="_Toc225768974" class="anchor"></span>Gambar III‑1 <em>Flowchart</em> Tahapan Penelitian</p></figcaption>
</figure>

### Tahap 1: *Business Understanding*

Tahap ini bertujuan menyelaraskan tujuan analitik dengan kebutuhan strategis institusi serta pengumpulan data yang diperlukan. Langkah-langkah yang dilakukan meliputi:

1.  Identifikasi Masalah: Memetakan kendala saat ini di mana data asesmen psikologi mahasiswa yaitu OMNI belum dimanfaatkan secara optimal untuk intervensi proaktif, serta proses analisis manual yang tidak efisien.

2.  Perumusan Masalah: Merumuskan pertanyaan penelitian spesifik mengenai bagaimana mengelompokkan profil kepribadian mahasiswa menggunakan pendekatan berbasis data (*data-driven*) untuk kepentingan intervensi kesehatan mental.

3.  Penetapan Tujuan Penelitian: Menetapkan target luaran berupa model profil dan *dashboard* interaktif. Pada tahap ini juga ditetapkan kriteria keberhasilan, yaitu tercapainya nilai *Entropy* ≥ 0.80 (validitas statistik) dan profil yang dapat diinterpretasikan secara klinis oleh psikolog (validitas substantif).

4.  Pengumpulan Data: Mengambil data sekunder dari repositori Unit Layanan Psikologi hasil OMNI berupa respons jawaban mahasiswa (anonim).

### Tahap 2: *Data Understanding*

Tahap ini berfokus pada pemahaman struktur variabel, dan pemeriksaan karakteristik data untuk mengidentifikasi pola awal.

1.  Definisi Variabel: Didefinisikan terlebih dahulu seluruh variabel dasar yang terdapat pada data mentah (*raw data*) instrumen OMNI. Variabel tersebut mencakup indikator validitas respons, skala kepribadian normal, skala gangguan kepribadian, serta dimensi skala faktor, yang seluruhnya dirangkum dalam Tabel III-1 berikut.

| **No** | **Nama Variabel** | **Tipe Data** | **Deskripsi** |
|:--:|:--:|:--:|:---|
| 1 | Val_VRIN | Float | (Indikator Validitas Respons) Variable Response Inconsistency: Mengukur konsistensi pola jawaban responden untuk mendeteksi respons acak atau ketidakseriusan pengisian. |
| 2 | Val_CD | Float | (Indikator Validitas Respons) Current Distress: Mengukur tingkat tekanan emosional, kecemasan, atau stres yang dialami responden saat pengisian tes. |
| 3 | Sc_Aestheticism | Float | (Skala Kepribadian Normal) Mengukur apresiasi terhadap seni, keindahan, dan pengalaman estetis. |
| 4 | Sc_Ambition | Float | (Skala Kepribadian Normal) Mengukur dorongan untuk berprestasi, kompetitif, dan mencapai tujuan tinggi. |
| 5 | Sc_Anxiety | Float | (Skala Kepribadian Normal) Mengukur kecenderungan mengalami kekhawatiran, ketegangan, atau rasa takut. |
| 6 | Sc_Assertiveness | Float | (Skala Kepribadian Normal) Mengukur kemampuan mengekspresikan pendapat, memimpin, dan bersikap tegas. |
| 7 | Sc_Conventionality | Float | (Skala Kepribadian Normal) Mengukur kepatuhan terhadap norma sosial, tradisi, dan aturan yang berlaku. |
| 8 | Sc_Depression | Float | (Skala Kepribadian Normal) Mengukur kecenderungan perasaan sedih, pesimis, atau putus asa (dalam rentang normal). |
| 9 | Sc_Dutifulness | Float | (Skala Kepribadian Normal) Mengukur rasa tanggung jawab, keandalan, dan komitmen terhadap kewajiban. |
| 10 | Sc_Energy | Float | (Skala Kepribadian Normal) Mengukur tingkat vitalitas, antusiasme, dan aktivitas fisik. |
| 11 | Sc_Excitement | Float | (Skala Kepribadian Normal) Mengukur kebutuhan akan stimulasi, sensasi, dan kegembiraan. |
| 12 | Sc_Exhibitionism | Float | (Skala Kepribadian Normal) Mengukur keinginan untuk menjadi pusat perhatian dan tampil di depan orang lain. |
| 13 | Sc_Flexibility | Float | (Skala Kepribadian Normal) Mengukur kemampuan beradaptasi dan keterbukaan terhadap perubahan situasi. |
| 14 | Sc_Hostility | Float | (Skala Kepribadian Normal) Mengukur kecenderungan merasakan kemarahan atau sinisme terhadap orang lain. |
| 15 | Sc_Impulsiveness | Float | (Skala Kepribadian Normal) Mengukur kecenderungan bertindak spontan tanpa perencanaan matang. |
| 16 | Sc_Intellect | Float | (Skala Kepribadian Normal) Mengukur ketertarikan pada ide-ide abstrak, diskusi intelektual, dan pemikiran logis. |
| 17 | Sc_Irritability | Float | (Skala Kepribadian Normal) Mengukur ambang batas toleransi terhadap frustrasi atau gangguan. |
| 18 | Sc_Modesty | Float | (Skala Kepribadian Normal) Mengukur kerendahan hati dan ketidakinginan untuk menonjolkan diri sendiri. |
| 19 | Sc_Moodiness | Float | (Skala Kepribadian Normal) Mengukur fluktuasi suasana hati dan stabilitas emosional. |
| 20 | Sc_Orderliness | Float | (Skala Kepribadian Normal) Mengukur preferensi terhadap kerapian, struktur, dan organisasi. |
| 21 | Sc_SelfIndulgence | Float | (Skala Kepribadian Normal) Mengukur kecenderungan untuk memanjakan diri dan mencari kepuasan segera. |
| 22 | Sc_SelfReliance | Float | (Skala Kepribadian Normal) Mengukur kemandirian dan kepercayaan pada kemampuan diri sendiri. |
| 23 | Sc_Sincerity | Float | (Skala Kepribadian Normal) Mengukur kejujuran, ketulusan, dan keterusterangan dalam berinteraksi. |
| 24 | Sc_Sociability | Float | (Skala Kepribadian Normal) Mengukur keinginan untuk berinteraksi sosial dan berada di sekitar orang lain. |
| 25 | Sc_Tolerance | Float | (Skala Kepribadian Normal) Mengukur penerimaan terhadap perbedaan nilai, pendapat, atau perilaku orang lain. |
| 26 | Sc_Trustfulness | Float | (Skala Kepribadian Normal) Mengukur kecenderungan mempercayai niat baik orang lain (tidak curiga). |
| 27 | Sc_Warmth | Float | (Skala Kepribadian Normal) Mengukur kasih sayang, keramahan, dan kedekatan emosional dengan orang lain. |
| 28 | Sc_Paranoid | Float | (Skala Gangguan Kepribadian) Mengukur kecenderungan ketidakpercayaan dan kecurigaan berlebih terhadap motif orang lain. |
| 29 | Sc_Schizoid | Float | (Skala Gangguan Kepribadian) Mengukur pelepasan diri dari hubungan sosial dan rentang ekspresi emosional yang terbatas. |
| 30 | Sc_Schizotypal | Float | (Skala Gangguan Kepribadian) Mengukur ketidaknyamanan akut dalam hubungan dekat, distorsi kognitif, dan perilaku eksentrik. |
| 31 | Sc_Antisocial | Float | (Skala Gangguan Kepribadian) Mengukur pengabaian dan pelanggaran terhadap hak-hak orang lain serta norma sosial. |
| 32 | Sc_Borderline | Float | (Skala Gangguan Kepribadian) Mengukur ketidakstabilan dalam hubungan antarpribadi, citra diri, emosi, serta impulsivitas. |
| 33 | Sc_Histrionic | Float | (Skala Gangguan Kepribadian) Mengukur tingkat emosionalitas yang berlebihan dan perilaku mencari perhatian. |
| 34 | Sc_Narcissistic | Float | (Skala Gangguan Kepribadian) Mengukur tingkat kebesaran diri (fantasi/perilaku), kebutuhan akan kekaguman, dan kurangnya empati. |
| 35 | Sc_Avoidant | Float | (Skala Gangguan Kepribadian) Mengukur hambatan sosial, perasaan tidak mampu, dan hipersensitivitas terhadap evaluasi negatif. |
| 36 | Sc_Dependent | Float | (Skala Gangguan Kepribadian) Mengukur kebutuhan berlebih untuk diurus yang memicu perilaku tunduk dan ketakutan akan perpisahan. |
| 37 | Sc_ObsessiveCompulsive | Float | (Skala Gangguan Kepribadian) Mengukur keasyikan dengan keteraturan, perfeksionisme, serta kontrol mental dan antarpribadi. |
| 38 | Sc_Agreeableness | Float | (Skala Faktor) Mengukur kecenderungan untuk bersikap baik, kooperatif, dan dapat dipercaya oleh orang lain. |
| 39 | Sc_Conscientiousness | Float | (Skala Faktor) Mengukur tingkat keandalan, kedisiplinan, keteraturan, dan ambisi dalam mencapai tujuan. |
| 40 | Sc_Extraversion | Float | (Skala Faktor) Mengukur intensitas interaksi sosial, tingkat energi, dan kebutuhan akan stimulasi. |
| 41 | Sc_Narcissism | Float | (Skala Faktor) Mengukur kecenderungan dominasi, memamerkan diri, dan kekakuan (infleksibilitas). |
| 42 | Sc_Neuroticism | Float | (Skala Faktor) Mengukur tingkat kecemasan, kemurungan (depresi), dan kerentanan terhadap stres emosional. |
| 43 | Sc_Openness | Float | (Skala Faktor) Mengukur ketertarikan pada seni, toleransi, dan keterbukaan terhadap pengalaman atau ide baru. |
| 44 | Sc_SensationSeeking | Float | (Skala Faktor) Mengukur dorongan pencarian sensasi, impulsivitas, pemanjaan diri, dan perilaku berisiko. |

<span id="_Toc225768981" class="anchor"></span>Tabel III‑1 Kamus Data Variabel OMNI

2.  Eksplorasi Data (*Exploratory Data Analysis*): Eksplorasi dilakukan untuk memahami karakteristik dan pola intrinsik data sebelum pemodelan. Aktivitas teknis yang dilakukan meliputi:

- Analisis Statistik Deskriptif: Menghitung nilai *mean*, median, standar deviasi, dan rentang data pada setiap atribut untuk melihat gambaran umum distribusi data.

- Pemeriksaan Kualitas Data: Mengidentifikasi keberadaan nilai yang hilang (*missing values*), duplikasi data, dan anomali (*outliers*) yang dapat memengaruhi kinerja model.

- Visualisasi Distribusi: Menggunakan histogram dan *boxplot* untuk menganalisis sebaran data, mendeteksi kemiringan (*skewness*), serta melihat pola normalitas data pada setiap dimensi skala.

- Analisis Korelasi: Memeriksa hubungan antar variabel untuk melihat pola keterkaitan awal antar dimensi kepribadian.

### Tahap 3: *Data Preparation*

Tahap ini merupakan fase konstruksi data untuk mengubah data mentah menjadi format yang siap dimodelkan (*model-ready*). Langkah-langkahnya mencakup:

1.  *Data Cleaning*: Melakukan penyaringan data responden berdasarkan kriteria kualitas. Baris data yang memiliki indikasi *missing values* signifikan atau terdeteksi invalid berdasarkan batas ambang skor VRIN dan CD (indikasi *careless responding*) akan dieliminasi dari dataset.

2.  *Feature Selection*: Meskipun dataset mentah memiliki 35 skala kepribadian dasar dan 7 skala faktor (seperti pada Tabel III-1), pada tahap pemrosesan ini dilakukan penyaringan fitur (*drop column*). Variabel yang akan dimasukkan ke dalam algoritma GMM dibatasi hanya pada 7 Skala Faktor Utama (Broad Scales). 35 skala pembentuk dasar (25 normal dan 10 abnormal) beserta skala validitas dibuang dari *dataframe* untuk mencegah multikolinearitas yang ekstrem dan menghindari *Curse of Dimensionality* (kutukan dimensi) yang dapat mengaburkan jarak perhitungan metrik pada algoritma *clustering*.

3.  Standardisasi: Melakukan penskalaan fitur (*feature scaling*) menggunakan metode Z-score pada variabel skala kepribadian yang terbentuk. Langkah ini bertujuan menyetarakan rentang nilai antar variabel agar perhitungan jarak dalam algoritma GMM menjadi optimal dan tidak bias.

### Tahap 4: *Modeling*

Tahap ini adalah fase eksekusi analitik menggunakan algoritma pembelajaran mesin untuk membentuk profil.

1.  Uji Invariansi: Melakukan pengujian statistik untuk memverifikasi bahwa struktur instrumen pengukuran bersifat setara (*invarian*) lintas kelompok demografis (Gender dan Program Studi). Tahap ini krusial untuk menjamin bahwa perbedaan profil yang ditemukan benar-benar mencerminkan perbedaan kepribadian, bukan bias alat ukur pada kelompok tertentu.

2.  Pemodelan GMM (*Gaussian Mixture Model*): Menerapkan algoritma *Gaussian Mixture Model* (GMM) untuk mengeksekusi *Latent Profile Analysis* (LPA). Algoritma ini digunakan untuk mengelompokkan mahasiswa ke dalam subgrup laten (klaster) berdasarkan densitas distribusi probabilitas dari pola skor kepribadian.

3.  Iterasi Model: Melakukan eksperimen model secara berulang (*looping*) dengan memvariasikan jumlah profil ($k$) mulai dari $k = 2$ hingga $k = 5$. Proses iterasi ini bertujuan untuk menghasilkan berbagai kandidat model yang nantinya akan dibandingkan melalui metrik evaluasi statistik.

4.  Estimasi Parameter: Melakukan estimasi parameter model melalui algoritma *Expectation-Maximization* (EM) untuk menentukan nilai rata-rata (*means*), kovarians (*covariances*), dan bobot pencampuran (*mixing weights*) untuk setiap profil. Parameter inilah yang merepresentasikan karakteristik unik dari setiap kelompok kepribadian mahasiswa yang terbentuk.

### Tahap 5: *Evaluation*

Evaluasi dilakukan secara komprehensif untuk memastikan model yang dihasilkan valid secara statistik dan bermakna secara keilmuan.

1.  Evaluasi *Goodness-of-Fit* Model: Menganalisis dan membandingkan kinerja model pada berbagai skenario jumlah profil (k). Penentuan profil optimal *Latent Profile Analysis* dilakukan secara holistik dengan membandingkan nilai *Akaike Information Criterion* (AIC) dan *Bayesian Information Criterion* (BIC) paling rendah (titik *elbow*). Selanjutnya, ditambahkan evaluasi menggunakan uji signifikan *Bootstrapped Likelihood Ratio Test* (BLRT) secara paralel.

2.  Evaluasi Akurasi Pemisahan Klaster: Mengukur tingkat kejelasan batas pemisahan antar profil menggunakan nilai *Entropy* ≥0.80, yang kemudian dikonfirmasi menggunakan dukungan skor tambahan *Silhouette Score* (\>0.5) untuk membuktikan bahwa profil kohesif secara internal namun tetap terpisah tegas dari profil sebelahnya.

3.  Interpretasi Substantif & Kalibrasi Ahli: Melakukan interpretasi karakteristik profil berdasarkan nilai rata-rata (*centroid)* setiap klaster. Pemeliharaan akurasi dan pelabelan profil divalidasi oleh ekspertis psikologi guna memastikan rekomendasi intervensi kelak tidak melenceng. Uji statistik tambahan seperti evaluasi invariansi proporsi sampel per profil dipastikan melebihi 5% agar analisis relevan dan stabil serta bukan bersifat penemuan yang tumpang tindih secara kebetulan semata.

### Tahap 6: *Deployment*

Tahap ini menerjemahkan hasil analisis menjadi sistem pendukung keputusan yang dapat digunakan pengguna akhir.

1.  *Prototyping Dashboard*: Mengembangkan antarmuka sistem interaktif menggunakan pustaka *Streamlit* (Python).

2.  Visualisasi Insight: Menyajikan peta sebaran profil risiko per angkatan, fakultas, dan program studi dalam bentuk grafik visual yang intuitif.

3.  Penyusunan Strategi Intervensi: Mengintegrasikan basis aturan (*rule-base*) ke dalam sistem untuk menampilkan rekomendasi program kesehatan mental yang spesifik sesuai dengan karakteristik profil yang terdeteksi pada suatu kelompok.

## Metode Pengumpulan data dan Pengolahan Data

1.  Spesifikasi Sumber Data: Penelitian ini menggunakan data sekunder (*archival data*) yang bersifat privat dan sensitif. Data diperoleh melalui prosedur perizinan resmi dari Unit Layanan Psikologi Universitas Telkom. Mengingat data memuat informasi psikologis mahasiswa, dataset disimpan dalam repositori internal dengan akses terbatas yang diatur dalam protokol kerahasiaan (*Non-Disclosure Agreement*).

- Jenis Data: Data Kuantitatif Terstruktur (*Structured Data*).

- Format Data: *Tabular dataset* (.csv/.xlsx) yang memuat matriks respons mahasiswa terhadap instrumen *OMNI Personality Inventory*.

- Struktur Atribut: Dataset terdiri dari serangkaian atribut numerik yang merepresentasikan indikator psikometrik. Struktur data ini dapat berupa respons tingkat item (*item-level responses*) atau skor skala agregat (*aggregated scale scores*), yang akan divalidasi lebih lanjut pada tahap eksplorasi data.

2.  Spesifikasi Lingkungan Pengolahan Data: Penelitian ini menerapkan pendekatan *Computational Psychiatry* menggunakan ekosistem *data science* berbasis Python (versi 3.10 atau lebih baru). Spesifikasi teknis perangkat lunak dan pustaka yang digunakan meliputi:

- Platform Pengembangan: *Jupyter Notebook* atau *Google Colab* untuk dokumentasi kode yang interaktif dan transparan.

- *Library* Manipulasi Data: Pandas dan NumPy digunakan untuk manajemen *dataframe*, pembersihan data (*data cleaning*), dan operasi vektorisasi pada atribut multidimensional.

- *Library* Pemodelan: Scikit-learn (modul mixture) digunakan untuk implementasi algoritma *Gaussian Mixture Model* (GMM) dan estimasi parameter berbasis *Expectation-Maximization* (EM).

- *Library* Visualisasi & Deployment: Seaborn dan Matplotlib untuk analisis distribusi data statistik, serta kerangka kerja Streamlit untuk pengembangan antarmuka *dashboard* interaktif bagi pengguna akhir.

## Metode Evaluasi

Evaluasi penelitian ini dirancang untuk mengukur validitas model pengelompokan (*clustering validity*) dari dua perspektif utama, ketepatan statistik dan kebermaknaan interpretasi.

1.  Evaluasi Kualitas Model (*Statistical Fit Metrics*) Untuk menentukan jumlah profil ($k$) yang paling optimal secara objektif, digunakan parameter kriteria informasi sebagai berikut:

- *Akaike Information Criterion* (AIC) & *Bayesian Information Criterion* (BIC): Metrik ini digunakan untuk mengukur efisiensi model dengan menyeimbangkan *goodness-of-fit* dan kompleksitas model. Model dengan nilai AIC dan BIC yang lebih rendah diindikasikan sebagai model yang lebih baik (*parsimonious model*).

- *Entropy*: Metrik ini digunakan untuk mengukur ketidakpastian klasifikasi posterior. Nilai *entropy* mendekati 1 (target≥0.80) menunjukkan bahwa model berhasil memisahkan profil-profil kepribadian secara tegas (*well-separated clusters*) dengan tingkat ambiguitas yang minimal.

2.  Evaluasi Evaluasi Stabilitas Model

- *Likelihood Ratio Test* (LMR-LRT / BLRT): Pengujian statistik untuk memverifikasi signifikansi penambahan jumlah profil. Nilai p \< 0.05 digunakan sebagai standar untuk menyatakan bahwa model dengan $k$ profil memberikan peningkatan kecocokan yang signifikan dibandingkan model dengan $k - 1$ profil.

- *Silhouette Score*: Metrik dukungan struktural (*structural support metric*) untuk mengevaluasi apakah profil terdefinisi secara baik dan padat (kohesif secara internal dan menyebar). Nilai valid ditandai pada parameter ≥0.5.

3.  Evaluasi Substantif (*Interpretability Check*): Evaluasi kualitatif dilakukan untuk memvalidasi relevansi hasil analisis dengan teori psikologi. Kriteria keberhasilan meliputi:

- Ukuran Profil: Setiap profil yang terbentuk harus mencakup proporsi sampel yang substansial (umumnya \>5% dari total populasi) untuk menghindari terbentuknya profil *spurious* (palsu) yang hanya berisi *outliers*.

- Makna Klinis: Pola karakteristik (*centroid*) dari setiap profil harus dapat dijelaskan secara logis dan diberi label yang bermakna (misalnya: "Profil Resilien" atau "Profil Rentan") sebagai dasar penentuan strategi intervensi.

# DAFTAR PUSTAKA

Adipraja, P. F. E. (2022). *Mengenal Konsep Algoritma Ekspektasi-Maksimisasi (EM)*. https://www.indowhiz.com/articles/id/mengenal-konsep-algoritma-expectation-maximization-em/

Akkem, Y., Kumar, B. S., & Varanasi, A. (2023). Streamlit Application for Advanced Ensemble Learning Methods in Crop Recommendation Systems – A Review and Implementation. *Indian Journal Of Science And Technology*, *16*(48), 4688–4702. https://doi.org/10.17485/IJST/v16i48.2850

Buschmeyer, K., Hatfield, S., & Zenner, J. (2023). Psychological assessment of AI-based decision support systems: tool development and expected benefits. *Frontiers in Artificial Intelligence*, *6*. https://doi.org/10.3389/frai.2023.1249322

Center for Reproductive Health, U. of Q. & J. H. B. S. of P. H. (2022). *I-NAMHS: Indonesia-National Adolescent Mental Health Survey*. https://qcmhr.org/outputs/reports/12-i-namhs-report-bahasa-indonesia

Chen, R., Gao, X., Zhang, Z., Hong, M., & Zhang, L. (2025). What predicts mental health profiles in first-generation college freshmen?: the role of proactive personality and university environment. *BMC Psychology*, *13*(1). https://doi.org/10.1186/s40359-025-02498-2

Choi, M., Driver, M. N., Balcke, E., Saunders, T., Langberg, J. M., & Dick, D. M. (2024). Initial Results from a New College Substance Use Prevention Program Targeting Externalizing and Internalizing Traits. *Substance Use and Misuse*, *59*(3), 421–424. https://doi.org/10.1080/10826084.2023.2275565

Eisenberg, D., Lipson, S. K., Heinze, J., Zhou, S., Study, M., Vyletel, B., Henry, H., Fucinari, J., Murphy, M., Voichoski, E., & Bell, J. (2023). *THE HEALTHY MINDS STUDY 2022-2023 Data Report*. https://healthymindsnetwork.org/wp-content/uploads/2019/04/HMS_national.pdf

Ferguson, S. L., G. Moore, E. W., & Hull, D. M. (2020). Finding latent groups in observed data: A primer on latent profile analysis in Mplus for applied researchers. *International Journal of Behavioral Development*, *44*(5), 458–468. https://doi.org/10.1177/0165025419881721

Fischer, R., & Karl, J. A. (2019). A primer to (cross-cultural) multi-group invariance testing possibilities in R. *Frontiers in Psychology*, *10*(JULY). https://doi.org/10.3389/fpsyg.2019.01507

Freilich, C. D., Palumbo, I. M., Latzman, R. D., & Krueger, R. F. (2023). Assessing the Measurement Invariance of the Personality Inventory for DSM-5 Across Black and White Americans. *Psychological Assessment*, *35*(9), 721–728. https://doi.org/10.1037/pas0001255

Gholami, M., Wing, D., Bedmutha, M. S., Godino, J., Ibarra, A., Fergerson, B., May, N., Longhurst, C. A., Weibel, N., Duffy, A., Rataj, H., Singh, K., & Patrick, K. (2025). A Human-Centered Approach for a Student Mental Health and Well-Being Mobile App: Protocol for Development, Implementation, and Evaluation. *JMIR Research Protocols*, *14*, e68368. https://doi.org/10.2196/68368

Guelmami, N., Tannoubi, A., Chalghaf, N., Saidane, M., Kong, J., Puce, L., Fairouz, A., Bragazzi, N. L., & Alroobaea, R. (2022). Latent Profile Analysis to Survey Positive Mental Health and Well-Being: A Pilot Investigation Insight Tunisian Facebook Users. *Frontiers in Psychiatry*, *13*. https://doi.org/10.3389/fpsyt.2022.824134

Guess, P. (2006). Test Reviews: OMNI Personality Inventory. Dalam *Journal of Psychoeducational Assessment* (Vol. 24, Nomor 2, hlm. 160–166). https://doi.org/10.1177/0734282905285789

Hanum, N., Prianto, C., Rahayu, W. I., & Kishendrian, H. D. (2023). Penerapan Metode Clustering Dalam Segmentasi Pelanggan Perusahaan Logistik. *SINTECH Journal*. https://doi.org/10.31598

Janiesch, C., Zschech, P., & Heinrich, K. (2021). Machine learning and deep learning. *Electronic Markets*, *31*(3), 685–695. https://doi.org/10.1007/s12525-021-00475-2

Keane, J. (2023). *The Office for Students (OfS) mental health analytics project: an evaluation*. https://www.jisc.ac.uk/reports/the-office-for-students-mental-health-analytics-project

Khan, I. K., Daud, H., Zainuddin, N., & Sokkalingam, R. (2025). Standardizing reference data in gap statistic for selection optimal number of cluster in K-means algorithm. *Alexandria Engineering Journal*, *118*, 246–260. https://doi.org/10.1016/j.aej.2025.01.034

Kline, R. B. (2023). Principles and Practice of Structural Equation Modeling. Dalam *The Guilford Press* (FIFTH EDITION). The Guilford Press. https://bit.ly/Principles_and_Practice_of_Structural_Equation_Modeling

Kokkinos, C. M., Antoniadou, N., & Voulgaridou, I. (2024). Majors unleashed: unravelling students’ personality profiles across academic disciplines. *Current Psychology*, *43*(19), 17635–17645. https://doi.org/10.1007/s12144-024-05721-2

Liu, J., & Wu, Y. (2024). The Development and Transformation of Digital Economy Before and After the Pandemic Era. *EWA Publishing*. https://doi.org/10.54254/2754-1169/143/2024.GA18933

Madrid-Cagigal, A., Kealy, C., Potts, C., Mulvenna, M. D., Byrne, M., Barry, M. M., & Donohoe, G. (2025). Digital Mental Health Interventions for University Students With Mental Health Difficulties: A Systematic Review and Meta-Analysis. *Early Intervention in Psychiatry*, *19*(3). https://doi.org/10.1111/eip.70017

Magalhães, E. (2024). Dual-factor Models of Mental Health: A Systematic Review of Empirical Evidence. *Psychosocial Intervention*, *33*(2), 89–102. https://doi.org/10.5093/pi2024a6

Mason, A., Rapsey, C., Sampson, N., Lee, S., Albor, Y., Al-Hadi, A. N., Alonso, J., Al-Saud, N., Altwaijri, Y., Andersson, C., Atwoli, L., Auerbach, R. P., Ayuya, C., Báez-Mansur, P. M., Ballester, L., Bantjes, J., Baumeister, H., Bendtsen, M., Benjet, C., … van der Heijde, C. (2025). Prevalence, age-of-onset, and course of mental disorders among 72,288 first-year university students from 18 countries in the World Mental Health International College Student (WMH-ICS) initiative. *Journal of Psychiatric Research*, *183*, 225–236. https://doi.org/10.1016/j.jpsychires.2025.02.016

Moggia, D., Lutz, W., Brakemeier, E. L., & Bickman, L. (2024). Treatment Personalization and Precision Mental Health Care: Where are we and where do we want to go? Dalam *Administration and Policy in Mental Health and Mental Health Services Research* (Vol. 51, Nomor 5, hlm. 611–616). Springer. https://doi.org/10.1007/s10488-024-01407-w

Newton, N. C., Debenham, J., Slade, T., Smout, A., Grummitt, L., Sunderland, M., Barrett, E. L., Champion, K. E., Chapman, C., Kelly, E., Lawler, S., Castellanos-Ryan, N., Teesson, M., Conrod, P. J., & Stapinski, L. (2022). Effect of Selective Personality-Targeted Alcohol Use Prevention on 7-Year Alcohol-Related Outcomes among High-risk Adolescents: A Secondary Analysis of a Cluster Randomized Clinical Trial. *JAMA Network Open*, *5*(11), E2242544. https://doi.org/10.1001/jamanetworkopen.2022.42544

Nosè, M., Muriago, G., Turrini, G., Tedeschi, F., Forlani, O., Sartori, R., Badino, M., & Barbui, C. (2025). Effectiveness of a Self-Guided Digital Intervention for Mental Health and Psychological Well-Being in University Students: Pre- and Postintervention Study. *Journal of Medical Internet Research*, *27*(1). https://doi.org/10.2196/69031

Obiedat, M., Al-Yousef, A., Khasawneh, A., Hamadneh, N., & Aljammal, A. (2020). Using Fuzzy c-Means for Weighting Different Fuzzy Cognitive Maps. Dalam *IJACSA) International Journal of Advanced Computer Science and Applications* (Vol. 11, Nomor 5). www.ijacsa.thesai.org

Pan, L. L., Zhou, S. R., Chen, G. Z., Ke, Y. D., Huang, Z. Y., Wu, Y. W., & Yan, W. J. (2024). Latent profile analysis of Eysenck’s personality dimensions and psychological constructs in university students. *Frontiers in Psychology*, *15*. https://doi.org/10.3389/fpsyg.2024.1379705

Pecora, G., Laghi, F., Baiocco, R., Baumgartner, E., & Sette, S. (2025). A Latent Profile Analysis of Psychological Functioning During the COVID-19 Pandemic: Adolescents’ Perceived Social Support and Lifestyle Behaviours. *International Journal of Psychology*, *60*(2). https://doi.org/10.1002/ijop.70025

Rahmadani, A., & Mukti, Y. R. (2020). Adaptasi akademik, sosial, personal, dan institusional : studi college adjustment terhadap mahasiswa tingkat pertama. *Jurnal Konseling dan Pendidikan*, *8*(3), 159. https://doi.org/10.29210/145700

San Cornelio, G., Elisabeth Fäßler, V., Pires, F., Kai-Ho Chan, H., Neri, G., Marshall, S., Yaghi, A., Tabor, D., Sinha, R., & Mazumdar, S. (2025). Data visualization in AI-assisted decision-making: a systematic review. *Frontiers in Communication*. https://doi.org/10.3389/fcomm.2025.1605655

Sarker, I. H. (2021). Machine Learning: Algorithms, Real-World Applications and Research Directions. *SN Computer Science*, *2*(3). https://doi.org/10.1007/s42979-021-00592-x

Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. *Procedia Computer Science*, *181*, 526–534. https://doi.org/10.1016/j.procs.2021.01.199

Selvam, K. P., Kosalram, K., & Chinnaiyan, S. (2024). Post-COVID pandemic: The new normal and aftermath. *Journal of Family Medicine and Primary Care*, *13*(10), 4308–4314. https://doi.org/10.4103/jfmpc.jfmpc_313_24

Setyanto, A. T. (2023). Deteksi Dini Prevalensi Gangguan Kesehatan Mental Mahasiswa di Perguruan Tinggi. *Wacana*, *15*(1), 66. https://doi.org/10.20961/wacana.v15i1.69548

Siddiqui, M. M., & Siddiqui, M. J. (2022). How has the COVID-19 Pandemic Affected Student Mental Health? *EAS Journal of Psychology and Behavioural Sciences*, *4*(5), 117–123. https://doi.org/10.36349/easjpbs.2022.v04i05.001

Spurk, D., Hirschi, A., Wang, M., Valero, D., & Kauffeld, S. (2020). Latent profile analysis: A review and “how to” guide of its application within vocational behavior research. *Journal of Vocational Behavior*, *120*. https://doi.org/10.1016/j.jvb.2020.103445

Sterner, P., De Roover, K., & Goretzko, D. (2025). New Developments in Measurement Invariance Testing: An Overview and Comparison of EFA-Based Approaches. *Structural Equation Modeling*, *32*(1), 117–135. https://doi.org/10.1080/10705511.2024.2393647

Wajdi, M., Susanto, B., Made Sumartana, I., Agus Sutiarso, M., Hadi, W., & Negeri Bali, P. (2024). Profile of generation Z characteristics: Implications for contemporary educational approaches. *Kajian Pendidikan, Seni, Budaya, Sosial dan Lingkungan*, *1*(1), 33–44. https://ojs.ympn2.or.id/index.php/KPSBSL

Wang, S., Lu, J., Zheng, G., He, Y., Liu, S., Xiang, Y., Liu, X., Wang, X., & Xiao, Y. (2025). Poor performance of PHQ-9 and GAD-7 in screening clinical depression and anxiety among a large sample of Chinese children and adolescents. *BMC Psychiatry*, *25*(1). https://doi.org/10.1186/s12888-025-06754-y

Webster, C. A., Mîndrila, D., Murphy, A. D., Banićević, I., Perić, D., Stankić, D., & Banićević, Ž. (2025). Students’ Mental Health Profiles and Their Association With Health Behaviors and School Satisfaction in Dubai-Based British Curriculum Schools. *Psychology in the Schools*, *62*(10), 4023–4040. https://doi.org/10.1002/pits.23592

WHO. (2022). *World mental health report: transforming mental health for all*. https://www.who.int/publications/i/item/9789240049338

Xiao, R., Zhang, C., Lai, Q., Hou, Y., & Zhang, X. (2021). Applicability of the Dual-Factor Model of Mental Health in the Mental Health Screening of Chinese College Students. *Frontiers in Psychology*, *11*. https://doi.org/10.3389/fpsyg.2020.549036

Yehoshua, R. (2023). *Gaussian Mixture Models (GMMs): from Theory to Implementation*. https://towardsdatascience.com/

Zhong, B., Yan, J., Sun, H., Chen, H., Tao, B., Jiang, Y., Chen, H., Lu, T., & Ding, Z. (2024). Relationship between personality portraits of university students and interpersonal conflict resolution strategies: a latent profile analysis. *Scientific Reports*, *14*(1). https://doi.org/10.1038/s41598-024-83491-4

 
