import pandas as pd

def load_data():
    """Load and merge cleaned country datasets"""
    countries = ['benin', 'sierra_leone', 'togo']
    dfs = []
    
    for country in countries:
        try:
            df = pd.read_csv(
                f"data/{country}_clean.csv",
                parse_dates=["Timestamp"],
                encoding='utf-8'
            )
            df['Country'] = country.replace('_', ' ').title()
            dfs.append(df)
        except FileNotFoundError:
            continue
            
    return pd.concat(dfs) if dfs else pd.DataFrame()
