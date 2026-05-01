import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

def train_system():
    df = pd.read_csv("dataset.csv")
    
    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(ngram_range=(1, 2))
    X = tfidf.fit_transform(df['Complaint_Text'])
    y = df['Category']

    # Random Forest Model (Probability enabled)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Saving objects for AI Logic
    joblib.dump(model, 'model.pkl')
    joblib.dump(tfidf, 'tfidf.pkl')
    print("✅ Step 2: AI Model and Vectorizer trained and saved!")

if __name__ == "__main__":
    train_system()