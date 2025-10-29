import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Personal Finance Tracker", page_icon="💰", layout="wide")


def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")
        st.write(df)
        return df
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None


def main():
    st.title("💰 Personal Finance Tracker")

    uploaded_file = st.file_uploader("Upload your financial data (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)


main()
