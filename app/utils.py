# app/utils.py
import pandas as pd

def load_data():
    """Load data with encoding fallback"""
    countries = ['benin', 'sierra_leone', 'togo']
    dfs = []
    
    for country in countries:
        try:
            # Try multiple common encodings
            for encoding in ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']:
                try:
                    df = pd.read_csv(
                        f"data/{country}_clean.csv",
                        parse_dates=["Timestamp"],
                        encoding=encoding
                    )
                    df['Country'] = country.replace('_', ' ').title()
                    dfs.append(df)
                    break
                except UnicodeDecodeError:
                    continue
        except Exception as e:
            print(f"Error loading {country}: {str(e)}")
    
    return pd.concat(dfs) if dfs else pd.DataFrame()
