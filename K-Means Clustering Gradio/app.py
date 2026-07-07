import os
import pickle

import gradio as gr
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ─────────────────────────────────────────────────────────────
# Dataset
# ─────────────────────────────────────────────────────────────
_URL = (
    "https://gist.github.com/pravalliyaram/5c05f43d2351249927b8a3f3cc3e5ecf"
    "/raw/8bd6144a87988213693754baaa13fb204933282d/Mall_Customers.csv"
)
_FEATURES = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
_N_CLUSTERS = 5


# ─────────────────────────────────────────────────────────────
# Training
# ─────────────────────────────────────────────────────────────
def _train():
    data = pd.read_csv(_URL)
    X = data[_FEATURES].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=_N_CLUSTERS, random_state=42, n_init=10)
    kmeans.fit(X_scaled)

    pickle.dump(kmeans, open("kmeans_model.pkl", "wb"))
    pickle.dump(scaler, open("scaler.pkl", "wb"))

    return kmeans, scaler, data


# ─────────────────────────────────────────────────────────────
# Load or train
# ─────────────────────────────────────────────────────────────
if os.path.exists("kmeans_model.pkl") and os.path.exists("scaler.pkl"):
    _kmeans = pickle.load(open("kmeans_model.pkl", "rb"))
    _scaler = pickle.load(open("scaler.pkl", "rb"))
    _data = pd.read_csv(_URL)
else:
    _kmeans, _scaler, _data = _train()

# Assign cluster labels to the training data for description computation
_data["Cluster"] = _kmeans.predict(
    _scaler.transform(_data[_FEATURES].values)
)


# ─────────────────────────────────────────────────────────────
# Cluster descriptions (computed from training-data statistics)
# ─────────────────────────────────────────────────────────────
def _make_descriptions(data: pd.DataFrame) -> dict:
    descriptions = {}
    for c in range(_N_CLUSTERS):
        cd = data[data["Cluster"] == c]
        avg_income = cd["Annual Income (k$)"].mean()
        avg_spending = cd["Spending Score (1-100)"].mean()
        n = len(cd)
        pct = n / len(data) * 100

        if avg_income >= 70 and avg_spending >= 60:
            label = "High Income - High Spending"
            detail = "Pelanggan premium dengan daya beli tinggi. Cocok untuk produk eksklusif dan loyalty program."
        elif avg_income >= 70 and avg_spending < 40:
            label = "High Income - Low Spending"
            detail = "Pelanggan berpendapatan tinggi namun hemat. Cocok untuk strategi value proposition dan membership."
        elif avg_income < 50 and avg_spending >= 60:
            label = "Low Income - High Spending"
            detail = "Pelanggan fashion-conscious yang suka berbelanja. Cocok untuk cicilan, flash sale, dan diskon."
        elif avg_income < 50 and avg_spending < 40:
            label = "Low Income - Low Spending"
            detail = "Pelanggan budget-conscious yang sangat hemat. Cocok untuk produk budget-friendly dan promo hemat."
        else:
            label = "Middle Income - Medium Spending"
            detail = "Pelanggan menengah dengan pola belanja seimbang. Cocok untuk produk mid-range dan penawaran bundling."

        descriptions[c] = (label, detail, avg_income, avg_spending, n, pct)
    return descriptions


_cluster_desc = _make_descriptions(_data)


# ─────────────────────────────────────────────────────────────
# Prediction function
# ─────────────────────────────────────────────────────────────
def predict_cluster(age: float, annual_income: float, spending_score: float) -> str:
    X_new = np.array([[age, annual_income, spending_score]])
    X_scaled = _scaler.transform(X_new)
    cluster = int(_kmeans.predict(X_scaled)[0])

    label, detail, avg_income, avg_spending, n, pct = _cluster_desc[cluster]

    result = (
        f"Customer termasuk Cluster {cluster}\n"
        f"{'─' * 40}\n"
        f"Cluster {cluster}: {label}\n\n"
        f"{detail}\n\n"
        f"Statistik Cluster:\n"
        f"  Rata-rata Annual Income : ${avg_income:.1f}k\n"
        f"  Rata-rata Spending Score: {avg_spending:.1f}\n"
        f"  Jumlah pelanggan        : {n} ({pct:.1f}%)"
    )
    return result


# ─────────────────────────────────────────────────────────────
# Gradio Interface
# ─────────────────────────────────────────────────────────────
with gr.Blocks(title="Customer Segmentation App") as demo:
    gr.Markdown(
        """
        # Customer Segmentation App
        Segmentasi pelanggan menggunakan **K-Means Clustering** (5 cluster).
        Masukkan informasi pelanggan di bawah ini, lalu klik **Predict**.
        """
    )

    with gr.Row():
        age_input = gr.Number(
            label="Age",
            value=30,
            minimum=18,
            maximum=70,
            precision=0,
        )
        income_input = gr.Number(
            label="Annual Income (k$)",
            value=50,
            minimum=1,
            maximum=200,
            precision=0,
        )

    spending_input = gr.Slider(
        label="Spending Score (1–100)",
        minimum=1,
        maximum=100,
        value=50,
        step=1,
    )

    predict_btn = gr.Button("Predict", variant="primary")

    result_box = gr.Textbox(
        label="Customer Segment",
        lines=9,
        interactive=False,
    )

    predict_btn.click(
        fn=predict_cluster,
        inputs=[age_input, income_input, spending_input],
        outputs=result_box,
    )

    gr.Markdown(
        """
        ---
        **Cluster Reference:**

        | Cluster | Segmen | Karakteristik |
        |---------|--------|---------------|
        | 0–4 | Tergantung data | Dihitung otomatis dari Mall Customer Dataset |

        Model: K-Means · Scaler: StandardScaler · Dataset: Mall Customer Segmentation
        """
    )

if __name__ == "__main__":
    demo.launch()
