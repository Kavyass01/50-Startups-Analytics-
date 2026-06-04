import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📊 Deep Analytics Dashboard")

df = pd.read_csv("data/50_Startups.csv")

# KPI Section

avg_profit = df["Profit"].mean()
max_profit = df["Profit"].max()
avg_rd = df["R&D Spend"].mean()
avg_marketing = df["Marketing Spend"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Profit", f"${avg_profit:,.0f}")
col2.metric("Highest Profit", f"${max_profit:,.0f}")
col3.metric("Average R&D", f"${avg_rd:,.0f}")
col4.metric("Average Marketing", f"${avg_marketing:,.0f}")

st.divider()

# Profit Distribution

fig1 = px.histogram(
    df,
    x="Profit",
    nbins=20,
    title="Profit Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# Scatter Analysis

fig2 = px.scatter(
    df,
    x="R&D Spend",
    y="Profit",
    color="State",
    size="Marketing Spend",
    hover_data=["Administration"],
    title="R&D Spend vs Profit"
)

st.plotly_chart(fig2, use_container_width=True)

# State Wise Profit

state_profit = (
    df.groupby("State")["Profit"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    state_profit,
    x="State",
    y="Profit",
    color="State",
    title="Average Profit by State"
)

st.plotly_chart(fig3, use_container_width=True)

# Box Plot

fig4 = px.box(
    df,
    x="State",
    y="Profit",
    color="State",
    title="Profit Spread by State"
)

st.plotly_chart(fig4, use_container_width=True)

# Pair Analysis

fig5 = px.scatter_matrix(
    df,
    dimensions=[
        "R&D Spend",
        "Administration",
        "Marketing Spend",
        "Profit"
    ],
    color="State"
)

st.plotly_chart(fig5, use_container_width=True)

# Insights

st.subheader("📈 AI Business Insights")

best_state = (
    df.groupby("State")["Profit"]
    .mean()
    .idxmax()
)

st.success(
    f"""
    • Highest average profit state: {best_state}

    • R&D Spend has the strongest positive relationship with Profit.

    • Marketing Spend contributes moderately to Profit.

    • Administration spending shows weaker impact on Profit.
    """
)
