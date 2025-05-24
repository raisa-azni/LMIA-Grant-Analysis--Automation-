# LMIA ETL Automation Project

## Overview

This project automates the ETL (Extract, Transform, Load) process for the Temporary Foreign Worker Program (TFWP) Labour Market Impact Assessment (LMIA) data. It provides tools for data cleaning, database storage, analysis, and visualization of LMIA grants.

## Features

- **ETL Pipeline:** Loads raw LMIA CSV data, cleans it, and saves it to both a processed CSV and a SQLite database.
- **Analysis:** Fetches data from the database and generates basic analytical reports.
- **Visualization:** Plots the top occupations receiving LMIA grants.

## Project Structure

- `etl.py`: Handles data loading, cleaning, and saving to CSV/SQLite.
- `analysis.py`: Contains functions for data retrieval and reporting.
- `Visualization.py`: Generates visualizations from the processed data.
- `main.py`: Orchestrates the ETL, analysis, and visualization pipeline.
- `README.md`: Project documentation.
- `project_description.txt`: Detailed project explanation.

## Usage

1. Place your raw LMIA CSV file in the specified directory.
2. Run the pipeline:
   ```sh
   python main.py
   ```
3. The cleaned data will be saved, analyzed, and visualized automatically.

## Requirements

- Python 3.x
- pandas
- sqlite3
- matplotlib (for visualization)

Install dependencies with:
```sh
pip install pandas matplotlib
```

## Output

- Cleaned CSV file
- SQLite database with LMIA data
- Analytical report (console output)
- Occupation visualization plot

---

