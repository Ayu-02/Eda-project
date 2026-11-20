
# Enterprise E-Commerce Data Engineering Pipeline

## Project Overview

This project implements an end-to-end Enterprise E-Commerce
Data Engineering Pipeline using Python, Pandas, SQL, and SQLite.

The objective is to transform raw e-commerce datasets into
clean, structured, and analytics-ready data.

The pipeline follows a Medallion Architecture:

- Bronze Layer: Raw data ingestion
- Silver Layer: Data cleaning and validation
- Gold Layer: Business-level aggregations
- Feature Store: Customer and product features
- Data Warehouse: SQLite analytical database

## Architecture

Raw Data
   |
   v
Bronze Layer
   |
   v
Silver Layer
   |
   v
Gold Layer
   |
   v
Feature Store
   |
   v
SQLite Data Warehouse
   |
   v
Business Analytics

## Technologies Used

- Python
- Pandas
- NumPy
- SQL
- SQLite
- CSV
- Git
- GitHub
- Unittest

## Project Structure

enterprise-ecommerce-data-engineering/

├── data/
├── src/
├── outputs/
├── warehouse/
├── tests/
├── docs/
├── main.py
├── config.py
├── requirements.txt
└── README.md

## Key Features

- Automated CSV data ingestion
- Customer and product data cleaning
- Order validation
- Data transformation
- Gold layer aggregations
- Customer and product feature engineering
- SQLite data warehouse
- SQL analytical queries
- Automated unit testing

## Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate into the project:

cd enterprise-ecommerce-data-engineering

Create virtual environment:

python -m venv .venv

Activate environment:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run Project

python main.py

## Run Tests

python -m unittest discover -s tests -v

## Data Warehouse

Database location:

warehouse/ecommerce.db

Tables:

- dim_customer
- dim_product
- dim_date
- fact_daily_sales
- fact_customer_sales
- fact_product_sales

## Future Improvements

- Apache Airflow orchestration
- PostgreSQL integration
- Docker containerization
- AWS S3 integration
- CI/CD using GitHub Actions
- Pipeline monitoring
- Incremental data loading

## Author

Ayush Vishnoi

## License

MIT License
