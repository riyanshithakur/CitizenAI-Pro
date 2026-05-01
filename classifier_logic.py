import joblib
import numpy as np

# Load trained models
model = joblib.load('model.pkl')
tfidf = joblib.load('tfidf.pkl')

def get_prediction(text):
    dept_map = {
        "Road": "Public Works Department (PWD)",
        "Water": "Jal Vibhag (Water Board)",
        "Sanitary": "Nagar Nigam (Waste Management)",
        "Public Lighting": "Electricity Department"
    }
    
    vec = tfidf.transform([text])
    
    # 1. AI Confidence Score
    probs = model.predict_proba(vec)[0]
    max_prob = np.max(probs) * 100
    
    # 2. Predicted Category
    cat = model.predict(vec)[0]
    
    # 3. Emergency Logic (AI Override)
    priority = "Normal"
    is_emergency = False
    critical_words = ["burst", "manhole", "dead", "current", "accident", "emergency", "fire"]
    
    if any(word in text.lower() for word in critical_words):
        priority = "CRITICAL"
        is_emergency = True
        
    return {
        "Category": cat,
        "Department": dept_map.get(cat, "General Ward"),
        "Priority": priority,
        "Confidence": round(max_prob, 2),
        "Is_Emergency": is_emergency
    }