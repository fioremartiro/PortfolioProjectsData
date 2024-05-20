# COVID-19 Data Exploration

## Project Overview
This project involves an in-depth analysis of COVID-19 data to extract insights on cases, deaths, and vaccination rates across different countries and continents. The SQL queries employ advanced data manipulation techniques including joins, CTEs, temporary tables, window functions, aggregate functions, and views.

## Data Source
The data for this project is sourced from the `PortfolioProject` database, specifically the `CovidDeaths` and `CovidVaccinations` tables.

## Key Features
- **Data Cleaning**: Filtered out entries where continent data is missing.
- **Analysis of Cases and Deaths**: Calculated the death percentage among confirmed cases and analyzed the total cases versus population to understand the infection rate.
- **Vaccination Analysis**: Tracked vaccination progress with cumulative totals using window functions.
- **Aggregated Global Insights**: Generated global totals for new cases and new deaths, and calculated death percentages over time.
- **Advanced SQL Techniques**: Used a combination of CTEs, temp tables, and views to organize and simplify data access for potential further analysis.

## Insights Derived
- Comparison of total cases vs. total deaths to explore the likelihood of dying from COVID-19 in various countries.
- Examination of infection rates as a percentage of the total population.
- Analysis of vaccination rates and how they progress over time across different regions.

## Setup and Usage
Ensure you have access to SQL Server with the necessary permissions to create views and manipulate data within the `PortfolioProject` database. Sequentially execute the provided SQL scripts to replicate the analysis environment and insights.

## Future Scope
This project can be extended by incorporating more granular data, such as age demographics and economic impacts, to provide deeper insights into the pandemic’s effects across different strata of society.

## Note
This README assumes a basic understanding of SQL and data analysis. It is intended to guide users in exploring and replicating the COVID-19 data analysis as performed in this project.
