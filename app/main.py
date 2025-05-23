# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_country_data, process_data, get_top_regions

# Configure page
st.set_page_config(
    page_title="West Africa Solar Potential",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main {padding: 2rem;}
    .sidebar .sidebar-content {padding: 1rem;}
    div[data-testid="stDataFrame"] {width: 100% !important;}
</style>
""", unsafe_allow_html=True)

# Sidebar controls
st.sidebar.title("Dashboard Controls")
country = st.sidebar.selectbox(
    "Select Country",
    ["Benin", "Sierra Leone", "Togo"],
    index=0
)

metric = st.sidebar.selectbox(
    "Select Metric",
    ["GHI", "DNI", "DHI", "Tamb"],
    index=0
)

# Main content
st.title(f"{country} Solar Analysis")
st.write(f"Analyzing {metric} (Global Horizontal Irradiance)")

try:
    # Load and process data
    df = load_country_data(country)
    df = process_data(df)
    
    # Visualization Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"{metric} Distribution")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(data=df, y=metric, ax=ax)
        st.pyplot(fig)
    
    with col2:
        st.subheader(f"Top 5 Regions by {metric}")
        top_regions = get_top_regions(df)
        st.dataframe(top_regions, hide_index=True)
    
    # Time Series Section
    if 'Timestamp' in df.columns:
        st.subheader(f"{metric} Over Time")
        time_df = df.set_index('Timestamp').resample('D')[metric].mean()
        st.line_chart(time_df)
    
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please ensure you have the cleaned data files in the data/ folder")
