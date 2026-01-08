import os
import pickle
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from nlp.preprocess import preprocess_text


# ================= CONFIG =================
CONFIDENCE_THRESHOLD = 0.12
MODEL_PATH = "nlp/intent_model.pkl"
VECTORIZER_PATH = "nlp/tfidf.pkl"
DATA_PATH = "data/intents.csv"


# ========== TRAINING FUNCTION ==========
def train_intent_classifier():
    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Preprocess text
    df["clean_text"] = df["text"].apply(
        lambda x: " ".join(preprocess_text(x))
    )

    # Vectorize
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["clean_text"])
    y = df["intent"]

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

    print("✅ Intent classifier trained & saved successfully!")


# ========== LOAD MODEL SAFELY ==========
MODEL = None
VECTORIZER = None

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    with open(MODEL_PATH, "rb") as f:
        MODEL = pickle.load(f)

    with open(VECTORIZER_PATH, "rb") as f:
        VECTORIZER = pickle.load(f)


# ========== PREDICTION FUNCTION ==========
def predict_intent(text):
    if MODEL is None or VECTORIZER is None:
        return "fallback"

    # Preprocess input
    clean = " ".join(preprocess_text(text))
    print("DEBUG CLEAN TEXT:", clean)
     

    # Vectorize
    X = VECTORIZER.transform([clean])

    # Predict probabilities
    probs = MODEL.predict_proba(X)[0]
    max_prob = np.max(probs)
    intent = MODEL.classes_[np.argmax(probs)]

    # Confidence guard
    if max_prob < CONFIDENCE_THRESHOLD:
        return "fallback"
    
    
          

    return intent


# ========== TRAIN ONLY WHEN RUN DIRECTLY ==========
if __name__ == "__main__":
    train_intent_classifier()
