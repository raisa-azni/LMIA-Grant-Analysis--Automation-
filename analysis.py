import sqlite3
import pandas as pd

def fetch_data(db_path, table_name="lmia_grants"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

def basic_report(df):
    print("Shape:", df.shape)
    print("Top 5 Employers:\n", df['Employer'].value_counts().head())
    print("Top Occupations:\n", df['Occupation name'].value_counts().head())
    print("Null values:\n", df.isnull().sum())

if __name__ == "__main__":
    db_path = "lmia_analysis.db"
    df = fetch_data(db_path)
    basic_report(df)
