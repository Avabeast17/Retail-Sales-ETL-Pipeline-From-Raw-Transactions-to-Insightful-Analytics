# Retail Sales ETL Pipeline

This project is a simple and practical example of an ETL (Extract, Transform, Load) data pipeline. It focuses on processing and analyzing retail grocery sales data using Python and pandas.

The goal is to take raw data from two different sources, clean and filter it, perform a basic analysis, and save the results for reporting or further use.


## Project Overview

This pipeline will:
- Read and merge two datasets (sales and additional store data)
- Clean the combined data
- Calculate average weekly sales per month
- Save the cleaned and aggregated data to CSV files
- Check that the output files were saved successfully



## Project Structure

```
retail-etl-pipeline/
├── data/
│   ├── grocery_sales.csv           # Simulated sales data
│   └── extra_data.parquet          # Additional store metadata
│
├── etl_pipeline.py                # Main ETL functions
├── run_pipeline.py                # Script to run the pipeline
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── output/
    ├── clean_data.csv             # Cleaned dataset
    └── agg_data.csv               # Aggregated sales data
```



## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/retail-etl-pipeline.git
cd retail-etl-pipeline
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the ETL pipeline:

```bash
python run_pipeline.py
```

4. Check the `output/` folder for the resulting CSV files.



## What's Inside the Code

- **extract()**: Combines sales data with additional data by shared index.
- **transform()**: Cleans missing values, filters by sales amount, and adds a month column.
- **avg_weekly_sales_per_month()**: Calculates the average sales for each month.
- **load()**: Saves both cleaned and aggregated data to CSV.
- **validation()**: Checks if the files were saved correctly.



## Why This Matters

ETL pipelines are essential in real-world data processing. They turn raw, messy inputs into structured, usable data that can support reporting, machine learning, or business decisions.

This example mirrors what you might find in a retail or operations analytics role, especially in companies that deal with time-series sales data.

