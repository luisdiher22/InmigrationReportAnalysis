# Inmigration Report Analysis

## Project Summary

This project prepares immigration apprehension data for reporting and dashboard analysis. The pipeline cleans and enriches the dataset with time-based fields and standardized state names, then exports a final CSV used for analytics and visualization.

It is designed as a practical data-analysis portfolio project with a clear ETL flow:

1. Load source data (CSV or Excel)
2. Clean and normalize fields
3. Add analysis-ready columns
4. Export a reporting table for dashboards

## Repository Structure

- [datasets/InmigrationReview.py](datasets/InmigrationReview.py): Main data pipeline script
- [datasets/arrests-latest-cleaned.csv](datasets/arrests-latest-cleaned.csv): Cleaned output dataset used for reporting
- [Main Dashboard.pbix](Main%20Dashboard.pbix): Power BI dashboard file

## Data Pipeline Details

The script in [datasets/InmigrationReview.py](datasets/InmigrationReview.py) performs the following:

1. Source detection

- Prefers the cleaned CSV if available
- Falls back to the raw Excel file when needed

2. Cleaning

- Drops metadata columns not needed for reporting:
  departed_date, file_original, sheet_original, row_original

3. Feature engineering

- Converts apprehension_date to datetime
- Creates year, month, and year-month fields:
  Anio, Mes, AnioMes
- Standardizes apprehension state names into a cleaned State column

4. Export

- Saves the final table to [datasets/arrests-latest-cleaned.csv](datasets/arrests-latest-cleaned.csv)

## Technologies

- Python
- pandas
- Power BI

## How To Run

### Prerequisites

- Python 3.10+
- pandas installed

### Steps

1. Open a terminal in the project root.
2. Activate your virtual environment.
3. Run the pipeline script:

   python datasets/InmigrationReview.py
4. Confirm output messages in terminal:

- Source used
- Cleaned file path
- Final DataFrame shape

## Portfolio Highlights

- Real-world data cleaning and transformation workflow
- Reproducible ETL script with clear function boundaries
- Business-intelligence integration with Power BI
- Reporting-ready dataset enriched for trend analysis by year and month

## Possible Improvements

- Add data quality checks (nulls, duplicates, schema validation)
- Add unit tests for each transformation function
- Add automatic charts with matplotlib or seaborn for exploratory analysis
- Add notebook documentation for step-by-step EDA

## Author

Prepared as a data analytics portfolio project by Luis Diego Hernández Mora
