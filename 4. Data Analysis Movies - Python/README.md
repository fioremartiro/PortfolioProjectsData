# Movie Data Exploration with Python, Pandas, and Numpy

This project focuses on exploring and analyzing a dataset of movies using Python, pandas, numpy, and seaborn. The following steps were undertaken to clean, transform, visualize, and analyze the data for better insights.

## Data Exploration Processes

### Installation
- **Objective**: Ensure all necessary libraries are installed and up-to-date.
- **Method**:
  - Installed pandas, numpy, matplotlib, and seaborn.
  - Upgraded seaborn to the latest version.

### Data Overview
- **Objective**: Load and preview the dataset.
- **Method**:
  - Read the movie data from a CSV file into a pandas DataFrame.
  - Displayed the first few rows of the DataFrame to understand its structure.

### Data Cleaning
- **Objective**: Identify and handle missing data and convert data types.
- **Method**:
  - Calculated the percentage of missing values in each column.
  - Converted the `budget` and `gross` columns to integer type after filling NaN values with 0.

### Data Transformation
- **Objective**: Extract and create new relevant columns.
- **Method**:
  - Extracted the year from the `released` column using a regular expression and created a new `yearcorrect` column.
  - Sorted the DataFrame by `gross` earnings in descending order.

### Visualization
- **Objective**: Visualize the relationships in the data using scatter plots and regression plots.
- **Method**:
  - Created a scatter plot to visualize the relationship between `budget` and `gross` earnings.
  - Used seaborn to create a regression plot with customized colors.

### Correlation Analysis
- **Objective**: Calculate and visualize the correlation between numeric features.
- **Method**:
  - Selected only numeric columns for correlation analysis.
  - Calculated the correlation matrix for numeric columns.
  - Visualized the correlation matrix using a heatmap with annotations for better readability.

### Factorized Correlation Analysis
- **Objective**: Analyze the correlation of factorized categorical values.
- **Method**:
  - Factorized categorical values to assign numeric values for each unique category.
  - Calculated and visualized the correlation matrix for these factorized values.

## Conclusion

This project effectively explores and analyzes the movie dataset, providing insights into the relationships between various features. The steps undertaken ensure the data is clean, well-transformed, and visually represented for easy understanding and further analysis.

## Notes

- The dataset used is a CSV file containing information about movies, including budgets, gross earnings, release dates, and more.
- All operations were performed within a Jupyter notebook environment, utilizing Python libraries tailored for data analysis and visualization.
