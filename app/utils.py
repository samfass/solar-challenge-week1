import pandas as pd

def load_data(filepath):
    try:
        return pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(filepath, encoding='latin1')

def clean_data(df):
    """Data cleaning pipeline"""
    # Add your cleaning logic here
    return df.dropna()
