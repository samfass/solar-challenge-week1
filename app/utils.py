# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def load_country_data(country):
    """Safely load cleaned country data with encoding fallback"""
    filepath = f"../data/{country.lower()}_clean.csv"
    try:
        return pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(filepath, encoding='latin1')

def process_data(df):
    """Clean and process data"""
    # Convert timestamp if exists
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df.dropna()

def get_top_regions(df, n=5):
    """Calculate top performing regions"""
    return df.groupby('Region')['GHI'].mean().nlargest(n).reset_index()
