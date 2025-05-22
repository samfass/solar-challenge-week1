import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

# Configure page
st.set_page_config(
    page_title="Solar Potential Dashboard",
    page_icon="‚òÄÔ∏è",
    layout="wide"
)

# Title and description
st.title("Ìºç West Africa Solar Potential Dashboard")
st.markdown("""
Interactive visualization of solar irradiation metrics across countries
""")

# Load data
@st.cache_data
def get_data():
    return load_data()

df = get_data()

# Sidebar controls
with st.sidebar:
    st.header("Filters")
    selected_countries = st.multiselect(
        "Select Countries",
        df['Country'].unique(),
        default=df['Country'].unique()
    )
    metric = st.selectbox(
        "Primary Metric",
        ["GHI", "DNI", "DHI"],
        index=0
    )
    show_table = st.checkbox("Show Top Regions", True)

# Filter data
filtered_df = df[df['Country'].isin(selected_countries)]

# Main content
tab1, tab2 = st.tabs(["Distribution Analysis", "Regional Insights"])

with tab1:
    st.header(f"{metric} Distribution")
    
    # Boxplot
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
    ax.set_title(f"{metric} Distribution by Country")
    ax.set_ylabel(f"{metric} (W/m¬≤)")
    st.pyplot(fig)

with tab2:
    st.header("Regional Performance")
    
    if show_table:
        # Top regions table
        st.subheader(f"Top 5 Regions by {metric}")
        top_regions = (filtered_df.groupby(['Country', 'Region'])[metric]
                      .mean()
                      .sort_values(ascending=False)
                      .head(5))
        st.dataframe(top_regions.reset_index())
    
    # Time series plot
    st.subheader("Temporal Trends")
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(12, 6))
        for country in filtered_df['Country'].unique():
            country_df = filtered_df[filtered_df['Country'] == country]
            country_df.set_index('Timestamp')[metric].plot(ax=ax, label=country)
        ax.legend()
        st.pyplot(fig)

# Footer
st.divider()
st.markdown
("""
**Data Sources**: Cleaned solar irradiation datasets  
**Metrics**:  
- GHI: Global Horizontal Irradiance  
- DNI: Direct Normal Irradiance  
- DHI: Diffuse Horizontal Irradiance
""")
