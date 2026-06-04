import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("🔍 Data Explorer")

df = pd.read_csv("data/50_Startups.csv")

# Dataset Overview
st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

st.divider()

# Raw Data
st.subheader("Dataset Preview")

st.dataframe(
    df,
    use_container_width=True,
    height=500
)

st.divider()

# Column Filter
st.subheader("Select Columns")

selected_cols = st.multiselect(
    "Choose Columns",
    df.columns.tolist(),
    default=df.columns.tolist()
)

st.dataframe(
    df[selected_cols],
    use_container_width=True
)

st.divider()

# Statistics
st.subheader("Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# Missing Values
st.subheader("Missing Value Analysis")

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

fig = px.bar(
    missing,
    x="Column",
    y="Missing Values",
    title="Missing Values Per Column"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Correlation Matrix
st.subheader("Correlation Matrix")

corr = df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Feature Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)
