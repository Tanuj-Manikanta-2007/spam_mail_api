import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from app.model_loader import tfidf, svm, lr

# Ensure stopwords are available (important for Render)
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords', quiet=True)

ps = PorterStemmer()
stops_words = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    text = str(text)
    text = text.lower()
    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    text = " ".join(text.split())
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stops_words]
    
    return " ".join(words)

def predict_email(text: str):
    cleaned = clean_text(text)
    vector = tfidf.transform([cleaned])
    
    pred = svm.predict(vector)[0]
    prob = lr.predict_proba(vector)[0]

    return {
        "prediction": "Spam" if pred == 1 else "Ham",
        "confidence": float(max(prob)),
        "spam_probability": float(prob[1]),
        "ham_probability": float(prob[0])
    }