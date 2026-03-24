import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Term Frequency – Inverse Document Frequency
#It converts text → numbers
tfidf = pickle.load(open(os.path.join(BASE_DIR, "models", "tfidf.pkl"), "rb"))
svm = pickle.load(open(os.path.join(BASE_DIR, "models", "svm_model.pkl"), "rb"))
lr = pickle.load(open(os.path.join(BASE_DIR, "models", "lr_model.pkl"), "rb"))