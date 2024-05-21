# Roller Coaster Data Analysis

This notebook performs data analysis on a roller coaster dataset. Below is a step-by-step explanation of the analysis performed.

## Step 0: Imports and Reading Data

1. **Importing Libraries**:
   - Imported necessary libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn` for data manipulation and visualization.
   - Set the plotting style to 'ggplot' for better visual aesthetics.
   - Configured pandas to display up to 200 columns.

2. **Reading the Dataset**:
   - Defined a variable `data_path` to store the file path to the dataset.
   - Read the roller coaster dataset using `pd.read_csv()`.

## Step 1: Data Understanding

1. **Dataframe Shape**:
   - Displayed the shape of the dataframe to understand the number of rows and columns.

2. **Head and Tail**:
   - Displayed the first 5 rows using `df.head(5)` and the last 5 rows using `df.tail(5)` to get an initial understanding of the data.

3. **Data Types (Dtypes)**:
   - Checked the data types of each column using `df.dtypes`.

4. **Statistical Summary (Describe)**:
   - Generated a statistical summary of the dataframe using `df.describe()`.

## Step 2: Data Preparation

1. **Dropping Irrelevant Columns and Rows**:
   - Selected relevant columns that are necessary for the analysis and created a copy of the dataframe.

2. **Date Conversion**:
   - Converted the `opening_date_clean` column to datetime format for accurate date manipulation.

3. **Renaming Columns**:
   - Renamed columns to more meaningful names for better readability.

4. **Handling Missing Values**:
   - Displayed the count of missing values in each column using `df.isna().sum()`.

5. **Handling Duplicate Values**:
   - Identified duplicate rows using `df.duplicated()` and displayed the first few duplicates.
   - Removed duplicates based on `Coaster_Name`, `Location`, and `Opening_Date` columns and reset the index.

## Step 3: Feature Understanding (Univariate Analysis)

1. **Plotting Feature Distributions**:
   - **Histogram**: Plotted a histogram of the `Speed_mph` column to understand the distribution of coaster speeds.
   - **KDE**: Plotted a Kernel Density Estimate (KDE) of the `Speed_mph` column for a smooth distribution curve.
   - **Bar Plot**: Displayed the top 10 years when coasters were introduced using a bar plot.

## Step 4: Feature Relationships

1. **Scatterplot**:
   - Plotted a scatter plot to visualize the relationship between `Speed_mph` and `Height_ft`.

2. **Heatmap Correlation**:
   - Created a correlation matrix of relevant numerical features and visualized it using a heatmap.

3. **Pairplot**:
   - Used Seaborn's `pairplot` to visualize pairwise relationships between numerical features colored by `Type_Main`.

4. **Groupby Comparisons**:
   - Analyzed the locations with the fastest roller coasters (minimum of 10) by grouping data by `Location`, calculating the mean speed, and visualizing it using a horizontal bar plot.

## Conclusion

This notebook provides a comprehensive analysis of the roller coaster dataset, covering data understanding, preparation, univariate analysis, and feature relationships. The visualizations help in gaining insights into the characteristics and distributions of roller coaster features.
