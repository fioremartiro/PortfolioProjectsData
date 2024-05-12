# Tableau Public COVID-19 Data Visualization Project

## Project Overview
This project uses SQL queries to prepare datasets for visualizing COVID-19 statistics on Tableau Public. The aim is to provide clear and impactful visual representations of COVID-19's impact, including case counts, death rates, infection rates, and vaccination progress worldwide.

## Data Source
The data is extracted from the `PortfolioProject` database, using the `CovidDeaths` and `CovidVaccinations` tables.

## Features and Queries
- **Global COVID-19 Overview**: Aggregated global data to show total cases, total deaths, and death percentages.
- **Non-Country Entities Analysis**: Data exclusions for non-country entities like 'World' and 'European Union' to maintain geographic consistency.
- **Infection and Mortality Rates**: Queries to calculate the highest infection counts and death rates per location, factoring in population sizes for accurate representation.
- **Vaccination Tracking**: Analysis of vaccination data to show rolling totals and percentages of populations vaccinated over time.
- **Temporal and Geographical Granularity**: Breakdowns by location and date to track COVID-19's spread and control measures' effectiveness over time.

## Insights
- **Death Rates vs. Cases**: Visualizations that explore the relationship between confirmed cases and resulting deaths, highlighting the deadliest outbreaks.
- **Population Infection Rates**: Maps and charts showing which regions have had the highest proportion of their populations infected.
- **Vaccination Progress**: Timelines and distribution maps of vaccination rollouts, providing insights into global and regional vaccination efforts.

## Usage
- **SQL Execution**: Run the provided SQL scripts to generate the necessary data extracts.
- **Tableau Setup**: Import the datasets into Tableau to create the visualizations.
- **Interactive Elements**: Utilize Tableau’s interactive capabilities, such as filters and drill-downs, to explore different dimensions of the data.

## View the Dashboard
Explore the interactive COVID-19 Dashboard created in Tableau Public [here](https://public.tableau.com/app/profile/fiorella.martinez/viz/COVIDDashboard_17153827476870/Dashboard1).

## Future Enhancements
This visualization project can be expanded by incorporating additional metrics such as age demographics, economic impacts, or more detailed vaccination data to provide deeper insights.

## Note
This README assumes familiarity with SQL and Tableau. It is designed to help users understand and replicate the data visualization process outlined in this project for COVID-19 data analysis.
