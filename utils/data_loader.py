import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """
    Load startup dataset.
    """

    df = pd.read_csv("data/50_Startups.csv")

    return df


@st.cache_data
def get_numeric_columns(df):

    return df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()


@st.cache_data
def get_categorical_columns(df):

    return df.select_dtypes(
        include=["object"]
    ).columns.tolist()
