import joblib
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

DATA_XLSX = Path("data/dataset.xlsx")
DATA_CSV = Path("data/sentiment_id.csv")

# Load dataset
# Expected columns: text, label
if DATA_XLSX.exists():
    df = pd.read_excel(DATA_XLSX)
else:
    df = pd.read_csv(DATA_CSV)
df = df.dropna(subset=["text", "label"])

texts = df["text"].astype(str).tolist()
labels = df["label"].astype(str).tolist()

X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels,
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("svm", LinearSVC()),
])

model.fit(X_train, y_train)

# Evaluate on the test split
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))

# Save trained model after evaluation
joblib.dump(model, "sentiment_svm.pkl")
print("Model saved to sentiment_svm.pkl")
