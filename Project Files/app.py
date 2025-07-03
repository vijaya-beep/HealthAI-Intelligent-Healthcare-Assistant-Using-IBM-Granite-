
import streamlit as st
from modules.patient_chat import patient_chat_response
from modules.disease_prediction import predict_disease
from modules.treatment_plan import generate_treatment_plan
from modules.health_analytics import health_dashboard

st.set_page_config(page_title="HealthAI", layout="wide")

st.title("🤖 HealthAI: Intelligent Healthcare Assistant")

menu = ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
choice = st.sidebar.selectbox("Choose a Module", menu)

if choice == "Patient Chat":
    st.header("💬 Patient Chat")
    query = st.text_input("Ask a health-related question:")
    if query:
        response = patient_chat_response(query)
        st.write("**Response:**", response)

elif choice == "Disease Prediction":
    st.header("🩺 Disease Prediction")
    symptoms = st.text_area("Enter your symptoms (comma-separated):")
    if symptoms:
        result = predict_disease(symptoms)
        st.json(result)

elif choice == "Treatment Plans":
    st.header("📋 Treatment Plans")
    condition = st.text_input("Enter your diagnosed condition:")
    if condition:
        plan = generate_treatment_plan(condition)
        st.write(plan)

elif choice == "Health Analytics":
    st.header("📊 Health Analytics")
    health_dashboard()
