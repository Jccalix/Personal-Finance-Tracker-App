import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import json
import os

st.set_page_config(page_title="Personal Finance Tracker", page_icon="💰", layout="wide")

st.write(
    "Hello! This is a personal finance tracker app. Upload your CSV file to get started."
)
