
import streamlit as st
import pandas as pd
import altair as alt

def health_dashboard():
    data = pd.DataFrame({
        "Date": pd.date_range(start="2025-06-01", periods=7),
        "Heart Rate": [72, 74, 70, 75, 71, 73, 72],
        "Blood Pressure": [120, 122, 119, 121, 123, 118, 120]
    })

    st.line_chart(data.set_index("Date"))
    st.write("AI Insight: Vitals appear stable. Maintain current routine and monitor weekly.")
