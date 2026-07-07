# Product Requirements Document (PRD)
# Customer Segmentation App menggunakan K-Means Clustering dan Gradio

## 1. Overview Produk

### Nama Aplikasi
**Customer Segmentation App**

### Deskripsi Singkat
Customer Segmentation App adalah aplikasi sederhana berbasis Machine Learning yang digunakan untuk melakukan segmentasi pelanggan berdasarkan karakteristik tertentu menggunakan algoritma K-Means Clustering.

Model clustering dilatih menggunakan **Mall Customer Dataset**. Setelah model berhasil dibuat, model disimpan dalam format `.pkl` dan digunakan kembali untuk melakukan prediksi cluster melalui sebuah interface sederhana menggunakan **Gradio**.

Aplikasi ini bertujuan untuk menunjukkan proses deployment model Machine Learning, khususnya untuk kasus **unsupervised learning**.

---

# 2. Tujuan Aplikasi

Tujuan pengembangan aplikasi:

- Menerapkan model clustering yang sudah dilatih ke dalam aplikasi sederhana.
- Memahami proses penyimpanan dan penggunaan kembali model Machine Learning.
- Membuat interface untuk melakukan prediksi cluster pelanggan baru.
- Memvisualisasikan hasil segmentasi pelanggan agar mudah dipahami.

---

# 3. Dataset

## Nama Dataset
Mall Customer Segmentation Dataset

## Deskripsi Dataset

Dataset berisi informasi pelanggan sebuah pusat perbelanjaan.

Fitur utama:

| Fitur | Deskripsi |
|---|---|
| CustomerID | ID unik pelanggan |
| Gender | Jenis kelamin pelanggan |
| Age | Usia pelanggan |
| Annual Income | Pendapatan tahunan pelanggan |
| Spending Score | Skor pengeluaran pelanggan |

---

# 4. Problem Statement

Perusahaan ingin memahami karakteristik pelanggan berdasarkan pola pendapatan dan kebiasaan belanja.

Dengan clustering, pelanggan dapat dikelompokkan menjadi beberapa segmen, misalnya:

- Pelanggan hemat
- Pelanggan potensial
- Pelanggan dengan pengeluaran tinggi
- Pelanggan dengan pendapatan tinggi tetapi pengeluaran rendah

Hasil segmentasi dapat membantu dalam strategi pemasaran.

---

# 5. Machine Learning Workflow

Alur pengembangan model:

```
Dataset
   |
   v
Data Preprocessing
   |
   v
Feature Selection
   |
   v
Feature Scaling
   |
   v
K-Means Training
   |
   v
Model Evaluation
   |
   v
Save Model (.pkl)
   |
   v
Gradio Deployment
```

---

# 6. Data Preprocessing

Tahapan preprocessing:

## 6.1 Feature Selection

Fitur yang digunakan:

```
Annual Income
Spending Score
```

atau dapat ditambahkan:

```
Age
Annual Income
Spending Score
```

---

## 6.2 Scaling Data

Karena K-Means menggunakan perhitungan jarak, fitur perlu dinormalisasi.

Metode:

- StandardScaler

Output:

```
scaler.pkl
```

---

# 7. Model Development

## Algorithm

Algoritma yang digunakan:

```
K-Means Clustering
```

Library:

```python
from sklearn.cluster import KMeans
```

---

## Parameter Model

Contoh konfigurasi:

```python
KMeans(
    n_clusters=5,
    random_state=42
)
```

Jumlah cluster dapat ditentukan menggunakan:

- Elbow Method
- Silhouette Score

---

# 8. Model Output

Model menghasilkan label cluster:

Contoh:

| Customer | Cluster |
|-|-|
| Customer A | Cluster 0 |
| Customer B | Cluster 3 |
| Customer C | Cluster 1 |

---

# 9. Model Saving

Model yang perlu disimpan:

## K-Means Model

Nama file:

```
kmeans_model.pkl
```

Berisi model clustering.

---

## Scaler

Nama file:

```
scaler.pkl
```

Digunakan untuk melakukan transformasi data baru.

---

Library penyimpanan:

```python
import pickle

pickle.dump(model, open("kmeans_model.pkl","wb"))
pickle.dump(scaler, open("scaler.pkl","wb"))
```

---

# 10. Prediction Pipeline

Alur prediksi pelanggan baru:

```
Input User
    |
    v
Load scaler.pkl
    |
    v
Transform Input
    |
    v
Load kmeans_model.pkl
    |
    v
Predict Cluster
    |
    v
Display Result
```

---

# 11. Gradio Interface Requirement

## Framework

Menggunakan:

```
Gradio
```

Library:

```python
import gradio as gr
```

---

# 12. User Input

Interface menerima input:

## Input 1

Nama:

```
Age
```

Tipe:

```
Number
```

---

## Input 2

Nama:

```
Annual Income
```

Tipe:

```
Number
```

---

## Input 3

Nama:

```
Spending Score
```

Tipe:

```
Slider (1-100)
```

---

# 13. Output Interface

Aplikasi menampilkan:

## Cluster Prediction

Contoh:

```
Customer termasuk Cluster 2
```

---

## Cluster Description

Tambahkan interpretasi:

Contoh:

```
Cluster 2:
High Income - High Spending Customer

Pelanggan potensial dengan kemampuan belanja tinggi.
```

---

# 14. Tampilan Interface

Struktur aplikasi:

```
=================================

 Customer Segmentation App

 Masukkan informasi pelanggan

 Age:
 [________]

 Annual Income:
 [________]

 Spending Score:
 [----slider----]

        Predict

 Result:

 Customer Segment:
 Cluster 2

 High Income - High Spending

=================================
```

---

# 15. File Structure Project

Struktur folder:

```
customer-segmentation-app/

│
├── app.py
│
├── kmeans_model.pkl
│
├── scaler.pkl
│
├── requirements.txt
│
└── README.md
```

---

# 16. Requirements.txt

Library:

```
gradio
pandas
numpy
scikit-learn
pickle
```

---

# 17. Deployment Target

Aplikasi dapat dijalankan pada:

- Local computer
- Hugging Face Spaces
- Cloud server

---

# 18. Success Criteria

Aplikasi dianggap berhasil apabila:

- Model K-Means berhasil dimuat.
- User dapat memasukkan data pelanggan baru.
- Sistem menghasilkan cluster pelanggan.
- Interface berjalan menggunakan Gradio.
- Model tidak perlu dilatih ulang saat aplikasi digunakan.

---

# 19. Future Improvement

Pengembangan berikutnya:

- Menambahkan visualisasi posisi cluster.
- Menampilkan grafik scatter plot.
- Menambahkan PCA untuk visualisasi.
- Membandingkan beberapa metode clustering.
- Menambahkan database pelanggan.

---

# End of PRD