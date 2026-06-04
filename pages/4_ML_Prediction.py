import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Profit Prediction",
    layout="wide"
)

st.title("🤖 Startup Profit Prediction")

# Load Model
model = joblib.load(
    "models/startup_profit_model.pkl"
)

st.subheader("Enter Startup Details")

col1, col2 = st.columns(2)

with col1:

    rd_spend = st.number_input(
        "R&D Spend",
        min_value=0.0,
        value=100000.0
    )

    admin = st.number_input(
        "Administration Cost",
        min_value=0.0,
        value=120000.0
    )

with col2:

    marketing = st.number_input(
        "Marketing Spend",
        min_value=0.0,
        value=200000.0
    )

    state = st.selectbox(
        "State",
        [
            "California",
            "Florida",
            "New York"
        ]
    )

st.divider()

if st.button(
    "Predict Profit",
    use_container_width=True
):

    input_data = pd.DataFrame({
        "R&D Spend": [rd_spend],
        "Administration": [admin],
        "Marketing Spend": [marketing],
        "State": [state]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Profit: ${prediction:,.2f}"
    )

    st.subheader("Prediction Summary")

    st.metric(
        "Expected Profit",
        f"${prediction:,.2f}"
    )

    if prediction > 150000:
        st.balloons()
        st.info(
            "Excellent growth potential detected."
        )

    elif prediction > 100000:
        st.info(
            "Good profitability expected."
        )

    else:
        st.warning(
            "Profit may be lower. Consider increasing R&D investment."
        )

st.divider()

st.subheader("📌 Model Information")

st.write("""
**Algorithm Used:** Random Forest Regressor

Features:
- R&D Spend
- Administration
- Marketing Spend
- State

Target:
- Profit
""")
