import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="Global Hunger Index Dashboard",
    page_icon="Ìºç",
    layout="wide"
)

# Title
st.title("ÔøΩÔøΩ Global Hunger Index Dashboard")
st.markdown("Explore Global Hunger Index (GHI) data across countries and regions")

# Sample data (in a real app, this would come from a CSV)
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Country': ['USA', 'India', 'China', 'Brazil', 'Germany', 'Nigeria', 'Ethiopia', 'Bangladesh'],
        'Region': ['North America', 'South Asia', 'East Asia', 'South America', 'Europe', 'Africa', 'Africa', 'South Asia'],
        'GHI': [5.2, 28.3, 9.5, 6.8, 2.5, 31.5, 29.7, 25.9],
        'Population (M)': [331, 1408, 1425, 213, 83, 206, 115, 165]
    })
    return data

# Load data
data = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect(
    "Select regions",
    options=data['Region'].unique(),
    default=data['Region'].unique()
)

selected_countries = st.sidebar.multiselect(
    "Select countries",
    options=data['Country'].unique(),
    default=data['Country'].unique()
)

# Filter data based on selections
filtered_data = data[
    (data['Region'].isin(selected_region)) & 
    (data['Country'].isin(selected_countries))
]

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("GHI Distribution by Country")
    if not filtered_data.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=filtered_data, x='Country', y='GHI', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No data available for selected filters")

with col2:
    st.subheader("Top Regions by GHI")
    if not filtered_data.empty:
        top_regions = filtered_data.groupby('Region')['GHI'].mean().sort_values(ascending=False)
        st.dataframe(top_regions, use_container_width=True)
    else:
        st.warning("No data available for selected filters")

# Additional visualizations
st.subheader("GHI vs Population")
if not filtered_data.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=filtered_data,
        x='Population (M)',
        y='GHI',
        hue='Region',
        size='GHI',
        sizes=(50, 300),
        ax=ax
    )
    ax.set_xlabel("Population (Millions)")
    ax.set_ylabel("Global Hunger Index")
    st.pyplot(fig)
else:
    st.warning("No data available for selected filters")

# Footer
st.markdown("---")
st.markdown("**Note:** This dashboard uses sample data. In a production environment, connect to your actual dataset.")
