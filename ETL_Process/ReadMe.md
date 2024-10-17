# ETL Process Documentation

## Overview
This project implements an ETL (Extract, Transform, Load) process that extracts data from various file sources, transforms it to fit the desired format, and loads it into a SQL Server database.

## ETL Process Breakdown

### 1. Extraction
The extraction phase reads data from several file sources located in different directories on your system, including:
- CSV Files:
  - dim_rooms.csv
  - dim_hotels.csv
- Excel Files:
  - dim_date.xlsx
  - fact_booking.xlsx
  - fact_aggregated_booking.xlsx

### 2. Transformation
During the transformation phase, the data undergoes several modifications, including:
- Renaming and adjusting columns in the DataFrames:
  - Renaming columns in the dim_date_data DataFrame:
    - 'week no' to 'week_num'
    - 'day type' to 'day_type'
- Converting date fields to proper datetime formats.
- Creating new columns such as date_id and check_in_date_id by formatting date columns into integers (YYYYMMDD format).
- Performing type conversions to ensure numerical and categorical data is in the correct format.

### 3. Loading
In the loading phase, the transformed data is inserted into a SQL Server database using the provided connection string (ELIJAH\\SQLEXPRESS01). The data is loaded into the following tables:
- dim_rooms
- dim_date
- dim_hotel
- fact_booking
- fact_properties_operations
