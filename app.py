import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Dropout System", layout="wide")

# ---------- DARK MODE UI ----------
st.markdown("""
<style>

/* background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* labels */
label {
    color: white !important;
    font-weight: 600;
}

/* inputs */
input {
    background-color: #1E1E1E !important;
    color: white !important;
}

/* select box */
div[data-baseweb="select"] {
    background-color: #1E1E1E !important;
    color: white !important;
}

/* sliders text */
.stSlider {
    color: white !important;
}

/* button */
.stButton>button {
    background: linear-gradient(90deg, #00ADB5, #007BFF);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.5rem 1rem;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #007BFF, #00ADB5);
    color: white;
}

/* titles */
h1, h2, h3 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ---------- TITLE ----------
st.title("🎓 Student Dropout Risk Prediction System")
st.write("AI-powered analysis for student performance & dropout risk")

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Academic Features")

    jee_main_score = st.slider("JEE Main Score", 0, 100, 50)
    jee_adv_score = st.slider("JEE Advanced Score", 0, 100, 50)
    mock_test_score_avg = st.slider("Mock Test Average", 0, 100, 50)
    class_12_percent = st.slider("Class 12 Percentage", 0, 100, 60)
    attempt_count = st.slider("Attempt Count", 0, 10, 1)
    daily_study_hours = st.slider("Daily Study Hours", 0, 12, 4)

with col2:
    st.subheader("🌍 Personal & Environment")

    family_income = st.slider("Family Income", 0, 200000, 50000)
    peer_pressure_level = st.slider("Peer Pressure Level", 0, 10, 5)

    school_board = st.selectbox("School Board", ["CBSE", "ICSE", "State"])
    coaching_institute = st.selectbox("Coaching Institute", ["Yes", "No"])
    parent_education = st.selectbox("Parent Education", ["High School", "Graduate", "Postgraduate"])
    location_type = st.selectbox("Location Type", ["Urban", "Rural"])
    mental_health_issues = st.selectbox("Mental Health Issues", ["Yes", "No"])
    admission_taken = st.selectbox("Admission Taken", ["Yes", "No"])

# ---------- PREDICTION ----------
if st.button("🚀 Predict Risk"):

    input_data = {
        "jee_main_score": jee_main_score,
        "jee_advanced_score": jee_adv_score,
        "mock_test_score_avg": mock_test_score_avg,
        "class_12_percent": class_12_percent,
        "attempt_count": attempt_count,
        "daily_study_hours": daily_study_hours,
        "family_income": family_income,
        "peer_pressure_level": peer_pressure_level,

        "school_board": school_board,
        "coaching_institute": coaching_institute,
        "parent_education": parent_education,
        "location_type": location_type,
        "mental_health_issues": mental_health_issues,
        "admission_taken": admission_taken
    }

    df = pd.DataFrame([input_data])

    # encoding
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    # prediction
    prediction = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    # ---------- RISK LEVEL ----------
    if prob < 0.3:
        risk = "Low Risk ✅"
        color = "green"
    elif prob < 0.7:
        risk = "Medium Risk ⚠️"
        color = "orange"
    else:
        risk = "High Risk 🚨"
        color = "red"

    st.markdown(f"## 🎯 Prediction: {risk}")
    st.progress(int(prob * 100))

    # ---------- CHART ----------
    fig = px.pie(
        names=["Risk", "Safe"],
        values=[prob, 1-prob],
        title="Risk Probability"
    )
    st.plotly_chart(fig, use_container_width=True)