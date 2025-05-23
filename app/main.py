# -*- coding: utf-8 -*-
"""
Streamlit dashboard for solar data analysis
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

# Configure page
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Add UTF-8 encoding when reading files
@st.cache_data
def safe_load_data(filepath):
    try:
        return pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(filepath, encoding='latin1')

# Load data
st.sidebar.title("Configuration")
countries = ["Benin", "Sierra Leone", "Togo"]
selected_country = st.sidebar.selectbox("Select Country", countries)

# Main content
st.title(f"Solar Potential Analysis: {selected_country}")

try:
    df = safe_load_data(f"../data/{selected_country.lower()}_clean.csv")
    
    # Visualization section
    st.header("Solar Irradiance Distribution")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y="GHI")
    st.pyplot(fig)
    
    # Top regions table
    st.header("Top Performing Regions")
    top_regions = df.groupby("Region")["GHI"].mean().nlargest(5).reset_index()
    st.dataframe(top_regions)
    
except FileNotFoundError:
    st.error("Data file not found. Please ensure cleaned data exists.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
