from etl import load_data, clean_data, save_to_db, save_to_csv
from analysis import fetch_data, basic_report
from Visualization import plot_top_occupations

def run_pipeline():
    # ETL
    df = load_data(r'C:\Users\raisa\OneDrive\Desktop\Analyst Study\projects\TFWP\LMIA-Grant-Analysis\lmia_cleaned_2024q4.csv')
    df_clean = clean_data(df)
    save_to_db(df_clean, "lmia_analysis.db")
    save_to_csv(df_clean, r'C:\Users\raisa\OneDrive\Desktop\Analyst Study\projects\TFWP\LMIA-Grant-Analysis\lmia_cleaned_2024q4.csv')

    # Analysis
    df_db = fetch_data("lmia_analysis.db")
    basic_report(df_db)

    # Visualization
    plot_top_occupations(df_db)

if __name__ == "__main__":
    run_pipeline()
