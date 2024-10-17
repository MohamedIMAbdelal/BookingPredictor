# Project Overview

This project leverages **Azure Cloud Services** for managing and processing data, integrating data flows into **Azure Machine Learning** for model building and analytics. Key components of the project include:

1. **ETL Process using SSIS**:
   - The **Extract, Transform, and Load (ETL)** process was carried out using **SQL Server Integration Services (SSIS)**. We extracted data from various sources, transformed it as per the requirements, and loaded it into a database for further processing.

2. **Uploading Data to Azure**:
   - After completing the ETL process on SSIS, we uploaded the transformed data to **Azure**. The data was then structured into **Data Assets** in **Azure Machine Learning Studio**, where it could be utilized for machine learning model training and analytics.

3. **Azure Machine Learning Studio**:
   - **Data Assets** were created in Azure ML Studio for machine learning purposes. For example, the **`JOSEPH_fact_booking`** dataset was created to manage hotel booking data, which could be queried and analyzed for building predictive models.
   
4. **Azure Data Factory for Data Transfer**:
   - We used **Azure Data Factory** to transfer data from the database to Azure Data Storage for subsequent access and processing in other services like Azure ML.
   - The Data Factory pipeline was responsible for automating the data movement from the **Azure SQL Database** to **Azure Data Storage**, ensuring that the transformed data is securely stored and ready for further use.
     - **Lookup Activity**: Retrieves table information from the source database.
     - **ForEach Activity**: Iterates over the results from the lookup and transfers data for each table using the **Copy Data Activity**.

## Key Components

### 1. Azure Machine Learning Studio
   - Dataset: **JOSEPH_fact_booking**
     - A tabular dataset created from the transformed data after the ETL process.
     - Used for querying, analytics, and machine learning modeling.

### 2. Azure Data Factory
   - Pipeline: **pipeline1**
     - Transfers data from the Azure SQL database to Azure Data Storage.
     - **Lookup1** fetches table names from the source database.
     - **ForEach1** iterates over tables and performs the data transfer using the **Copy Data Activity**.

## SQL Query Example in Azure ML Studio
```sql
SELECT * FROM fact_booking;
```

This query retrieves all data from the **fact_booking** dataset in Azure ML Studio for further analysis.
