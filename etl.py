import pandas as pd
import sqlite3

def load_data(csv_path):
    """Load CSV data into DataFrame."""
    df = pd.read_csv(csv_path)
    return df

def clean_data(df):
    """Example cleaning: remove duplicates, handle nulls."""
    df = df.drop_duplicates()
    df = df.fillna({'Incorporate Status': 'Unknown'})
    return df

def save_to_db(df, db_path, table_name="lmia_grants"):
    """Save DataFrame to SQLite database."""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def save_to_csv(df, path):
    """Optional: Save processed data as CSV."""
    df.to_csv(path, index=False)

if __name__ == "__main__":
    csv_path = r'C:\Users\raisa\OneDrive\Desktop\Analyst Study\projects\TFWP\LMIA-Grant-Analysis\lmia_cleaned_2024q4.csv'
    db_path = "lmia_analysis.db"
    processed_csv_path = r'C:\Users\raisa\OneDrive\Desktop\Analyst Study\projects\TFWP\LMIA-Grant-Analysis\lmia_processed_2024q4.csv'

    df = load_data(csv_path)
    df_clean = clean_data(df)
    save_to_db(df_clean, db_path)
    save_to_csv(df_clean, processed_csv_path)
    print("ETL pipeline complete!")
