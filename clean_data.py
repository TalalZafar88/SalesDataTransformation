# Collaborator 1: clean_data.py

import pandas as pd

def clean_data(df):
    # Add your data cleaning code here
    cleaned_df = df.dropna()
    return cleaned_df

if __name__ == "__main__":
    data = pd.read_csv("sales_data.csv")
    cleaned_data = clean_data(data)
    cleaned_data.to_csv("cleaned_data.csv", index=False)
