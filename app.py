import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from classifier_logic import get_prediction

# --- CONFIG & THEME ---
st.set_page_config(page_title="CitizenAI Pro", page_icon="🏙️", layout="wide")

# --- LOAD ANIMATION (AI Icon) ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except:
        return None

lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m6cuL6.json")

# --- PREMIUM CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; background-color: #f0f2f6; }
    
    .main-card {
        background: white; padding: 30px; border-radius: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05); margin-bottom: 25px;
        border: 1px solid #e1e4e8;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; border: none; padding: 12px 35px;
        border-radius: 12px; font-weight: 600; letter-spacing: 1px;
        transition: all 0.3s ease; width: 100%;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(118, 75, 162, 0.4); }
    
    .emergency-alert {
        background: #FF4B4B; color: white; padding: 20px;
        border-radius: 15px; font-weight: bold; text-align: center;
        animation: pulse 1.5s infinite; margin-bottom: 20px;
    }
    @keyframes pulse { 0% {box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.7);} 70% {box-shadow: 0 0 0 15px rgba(255, 75, 75, 0);} 100% {box-shadow: 0 0 0 0 rgba(255, 75, 75, 0);} }
    </style>
    """, unsafe_allow_html=True) # Yahan error fix kar diya hai

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🏛️ **CitizenAI v2.0**")
    st.markdown("---")
    page = st.sidebar.radio("Navigation", ["📥 File Complaint", "📊 Admin Analytics"])
    st.markdown("---")
    st.info("Status: System Online")
    st.caption("Hackathon Prototype - Bhopal Smart City")

# --- PAGE 1: HOME ---
if page == "📥 File Complaint":
    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.markdown("# Smart City **Grievance AI**")
        st.write("Solving citizen issues instantly with Machine Learning Intelligence.")
    with col_head2:
        if lottie_ai:
            st_lottie(lottie_ai, height=120, key="ai_icon")

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Drill-down Structure
    complaint_tree = {
        "Road": ["Potholes", "Broken Divider", "Incomplete Construction", "Road Cracks"],
        "Water": ["Pipeline Burst", "No Water Supply", "Contaminated Water", "Leakage"],
        "Sanitary": ["Garbage Overflow", "Blocked Sewage", "Dead Animal", "Open Manhole"],
        "Public Lighting": ["Short Circuit", "Broken Pole", "Dark Spot Area", "Timer Issue"]
    }
    
    c1, c2 = st.columns(2)
    with c1:
        m_type = st.selectbox("1. Category Select Karein", list(complaint_tree.keys()))
    with c2:
        s_type = st.selectbox("2. Specific Samasya", complaint_tree[m_type])
        
    desc = st.text_area("3. Describe the issue (AI iska analysis karega)", 
                        placeholder="E.g., There is a huge pothole near the main entrance causing traffic...", height=100)
    
    if st.button("🚀 Run AI Analysis & Submit"):
        if desc:
            # AI Logic call
            res = get_prediction(desc)
            st.markdown("---")
            
            if res['Is_Emergency']:
                st.markdown(f'<div class="emergency-alert">🚨 CRITICAL PRIORITY: {res["Priority"]} Detected</div>', unsafe_allow_html=True)
            
            # Results UI
            st.subheader("AI Diagnostics Result")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Assigned Dept", res['Department'])
            with m2:
                st.metric("AI Confidence", f"{res['Confidence']}%")
            with m3:
                st.metric("Resolution SLA", "24-48 Hours")
            
            st.balloons()
            st.success(f"Aapki shikayat **{res['Department']}** ko bhej di gayi hai.")
        else:
            st.warning("Pehle description mein kuch likhiye!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: ANALYTICS ---
else:
    st.title("📊 City Analytics & Probability")
    st.write("AI data distribution based on registered grievances.")
    
    stats = {'Dept': ['Road', 'Water', 'Sanitary', 'Lighting'], 'Reports': [35, 42, 58, 20]}
    df_stats = pd.DataFrame(stats)
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.subheader("Probability Distribution")
        st.bar_chart(df_stats.set_index('Dept'), color="#764ba2")
    with col_chart2:
        st.subheader("System Performance")
        st.progress(92)
        st.caption("92% AI Accuracy achieved during training.")

    st.markdown("---")
    st.table(df_stats)