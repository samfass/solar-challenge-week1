# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data
import sys
import traceback

# Configure page
st.set_page_config(
    page_title="Solar Potential Dashboard",
    page_icon="‚òÄÔ∏è",
    layout="wide"
)

def safe_load_data():
    """Handle data loading with error fallback"""
    try:
        df = load_data()
        if df.empty:
            st.error("No data loaded - check CSV files")
            st.stop()
        return df
    except Exception as e:
        st.error(f"Critical error: {str(e)}")
        st.error(traceback.format_exc())
        st.stop()

# Title and description
st.title("Ìºç West Africa Solar Potential Dashboard")
st.markdown("""
Interactive visualization of solar irradiation metrics  
*Data Sources: Benin, Sierra Leone, Togo*  
""")

# Load data with error handling
df = safe_load_data()

# Sidebar controls
with st.sidebar:
    st.header("Filters")
    selected_countries = st.multiselect(
        "Countries",
        sorted(df['Country'].unique()),
        default=sorted(df['Country'].unique())
    )
    metric = st.selectbox(
        "Metric",
        ["GHI", "DNI", "DHI"],
        index=0
    )

# Filter data
filtered_df = df[df['Country'].isin(selected_countries)]

# Main visualization
tab1, tab2 = st.tabs(["Distribution", "Trends"])

with tab1:
    st.header(f"{metric} Distribution")
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(
            data=filtered_df,
            x='Country',
            y=metric,
            hue='Country',
            palette="viridis",
            legend=False,
            ax=ax
        )
        ax.set_xlabel("")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Plotting error: {str(e)}")

with tab2:
    st.header("Temporal Trends")
    if not filtered_df.empty:
        try:
            fig, ax = plt.subplots(figsize=(12, 6))
            for country in filtered_df['Country'].unique():
                country_df = filtered_df[filtered_df['Country'] == country]
                country_df.set_index('Timestamp')[metric].plot(ax=ax, label=country)
            ax.legend()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Time series error: {str(e)}")

# Footer
st.divider()
st.markdown("""
**Metrics**:  
- GHI: Global Horizontal Irradiance  
- DNI: Direct Normal Irradiance  
- DHI: Diffuse Horizontal Irradiance  
""")
