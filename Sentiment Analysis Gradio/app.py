import gradio as gr
import joblib

# Load the trained model from the pickle file
with open('sentiment_svm.pkl', 'rb') as f:
    model = joblib.load(f)

def predict_sentiment(text):
    if text.strip() == "":
        return "Ketik teks di sini..."
    
    prediction = model.predict([text])[0]

    if prediction == 'pos':
        return "Positif"
    else:
        return "Negatif"


# Create a Gradio interface
interface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Ketik teks di sini..."),
    outputs=gr.Textbox(label="Prediksi Sentimen"),
    title="Analisis Sentimen Bahasa Indonesia",
    description="Masukkan teks dalam Bahasa Indonesia untuk memprediksi sentimennya.",
    examples=[
        ["Saya sangat puas dengan layanan ini"],
        ["Jelek sekali pelayanannya"],  
    ]
)

if __name__ == "__main__":
    interface.launch()