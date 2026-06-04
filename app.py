import streamlit as st
from utils.data_loader import load_data

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

df = load_data()

st.image(
    "assets/startup_banner.png",
    use_container_width=True
)

st.title("🚀 Startup Analytics Dashboard")

st.markdown("""
Analyze startup investments, profitability, and business growth using
Machine Learning and Interactive Analytics.
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Startups",
    len(df)
)

col2.metric(
    "Average Profit",
    f"${df['Profit'].mean():,.0f}"
)

col3.metric(
    "Highest Profit",
    f"${df['Profit'].max():,.0f}"
)

col4.metric(
    "Average R&D",
    f"${df['R&D Spend'].mean():,.0f}"
)

st.divider()

st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.success(
    "Navigate through the sidebar for Deep Analytics and ML Prediction."
)
