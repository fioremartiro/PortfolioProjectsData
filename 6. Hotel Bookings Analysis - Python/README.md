# Hotel Bookings Analysis - Python

This project involves performing data analysis on a hotel bookings dataset. Below is a step-by-step explanation of the analysis performed.

## Step 0: Imports and Reading Data

1. **Importing Libraries**:
   - Imported necessary libraries such as `pandas` and `matplotlib` for data manipulation and visualization.

2. **Reading the Dataset**:
   - Loaded the hotel bookings dataset using `pd.read_csv()`.

## Step 1: Data Understanding

1. **Dataframe Shape**:
   - Displayed the shape of the dataframe to understand the number of rows and columns.

2. **Head and Columns**:
   - Displayed the first 20 rows using `df.head(20)` to get an initial understanding of the data.
   - Listed all column names to ensure they match the original dataset.

## Step 2: Data Cleaning

1. **Handling Missing and Undefined Values**:
   - Replaced 'NA' values in the `children` column with 0.
   - Replaced 'Undefined' in the `meal`, `distribution_channel`, and `market_segment` columns with appropriate values.
   - Replaced 'Null' in the `agent` and `company` columns with 0.
   - Ensured no remaining null values in the `country` column.

## Step 3: Data Transformation

1. **Converting Data Types**:
   - Converted the `children` column to integer type.
   - Converted the `agent` and `company` columns to integer type using `pd.to_numeric()`.

## Step 4: Data Analysis and Visualization

1. **Canceled and Non-Canceled Reservations by Year**:
   - Grouped the data by `arrival_date_year` and `is_canceled`.
   - Counted the number of occurrences in each group and plotted a stacked bar chart to visualize the number of reservations canceled and not canceled per year.

2. **Children and Babies in Non-Canceled Reservations**:
   - Filtered the data to include only non-canceled reservations.
   - Summed the number of children and babies and plotted a bar chart to visualize the totals.

3. **Adults in Non-Canceled Reservations**:
   - Summed the number of adults in non-canceled reservations and printed the total count.

4. **Reservations by Market Segment (Non-Canceled)**:
   - Grouped the data by market segment and plotted a bar chart to visualize the number of non-canceled reservations by market segment.

## Step 5: Saving the Cleaned Data

1. **Saving to CSV**:
   - Saved the cleaned and processed DataFrame to a new CSV file.

## Conclusion

This project demonstrates the process of loading, cleaning, processing, and analyzing hotel booking data using Python. The visualizations provide insights into cancellation patterns, the number of children and babies in non-canceled reservations, and reservation trends by market segment.
