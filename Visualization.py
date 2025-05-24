import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data(db_path, table_name="lmia_grants"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

def plot_top_occupations(df):
    plt.figure(figsize=(10,6))
    top_occs = df['Occupation name'].value_counts().head(10)
    sns.barplot(y=top_occs.index, x=top_occs.values)
    plt.title('Top 10 Occupations')
    plt.xlabel('Number of Positions')
    plt.ylabel('Occupation')
    plt.tight_layout()
    plt.savefig('visualizations/top_occupations.png')
    plt.close()

if __name__ == "__main__":
    db_path = "lmia_analysis.db"
    df = fetch_data(db_path)
    plot_top_occupations(df)
    print("Visualization saved to visualizations/top_occupations.png")
