# app/main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, plot_comparison

# Configure page
st.set_page_config(
    page_title="Solar Potential Dashboard",
    page_icon="‚òÄÔ∏è",
    layout="wide"
)

# Title and description
st.title("Ìºç West Africa Solar Potential Analysis")
st.markdown("""
Compare solar irradiation metrics across Benin, Sierra Leone, and Togo
""")

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    countries = st.multiselect(
        "Select Countries",
        ["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )
    metrics = st.selectbox(
        "Primary Metric",
        ["GHI", "DNI", "DHI"]
    )
    show_stats = st.checkbox("Show Summary Statistics", True)

# Main content
@st.cache_data
def get_clean_data():
    """Load and merge cleaned country data"""
    return load_data()

df = get_clean_data()
filtered_df = df[df['Country'].isin(countries)]

# Visualization tabs
tab1, tab2 = st.tabs(["Comparison", "Trends"])

with tab1:
    st.header(f"{metrics} Distribution")
    fig = plot_comparison(filtered_df, metric=metrics)
    st.pyplot(fig)
    
    if show_stats:
        st.subheader("Summary Statistics")
        st.dataframe(
            filtered_df.groupby('Country')[metrics].agg(['mean', 'median', 'std']).style.background_gradient()
        )

with tab2:
    st.header("Temporal Trends")
    time_res = st.radio(
        "Time Resolution",
        ["Daily", "Monthly"],
        horizontal=True
    )
    
    # Example time series plot
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(12, 6))
        for country in filtered_df['Country'].unique():
            country_df = filtered_df[filtered_df['Country'] == country]
            if time_res == "Monthly":
                resampled = country_df.set_index('Timestamp').resample('M')[metrics].mean()
            else:
                resampled = country_df.set_index('Timestamp')[metrics]
            resampled.plot(ax=ax, label=country)
        
        ax.set_ylabel(f"{metrics} (W/m¬≤)")
        ax.legend()
        st.pyplot(fig)

# Footer
st.divider()
st.markdown("""
**Data Sources**: Cleaned solar irradiation datasets  
**Metrics**:  
- GHI: Global Horizontal Irradiance  
- DNI: Direct Normal Irradiance  
- DHI: Diffuse Horizontal Irradiance
""")
