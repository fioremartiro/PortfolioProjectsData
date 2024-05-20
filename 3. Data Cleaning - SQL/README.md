# Nashville Housing Data Cleaning

This project focuses on cleaning and organizing the Nashville Housing data stored in the `PortfolioProject` database. The following steps were undertaken to ensure the data is standardized, duplicates are removed, and the data structure is optimized for further analysis.

## Data Cleaning Processes

### Standardize Date Format
- **Objective**: Standardize the date format across the dataset.
- **Method**:
  - Converted `SaleDate` to a standard date format using SQL `CONVERT` function.
  - Added a new column `SaleDateConverted` to store the standardized date values.

### Populate Missing Property Addresses
- **Objective**: Fill in missing `PropertyAddress` fields where possible.
- **Method**:
  - Identified records with null `PropertyAddress`.
  - Used data from related records (matched by `ParcelID` but different `UniqueID`) to populate missing addresses.

### Normalize 'Sold As Vacant' Field
- **Objective**: Convert shorthand 'Y' and 'N' in the `SoldAsVacant` field to 'Yes' and 'No' for clarity.
- **Method**:
  - Updated the `SoldAsVacant` column using a `CASE` statement to translate 'Y' to 'Yes' and 'N' to 'No'.

### Split Property and Owner Address into Components
- **Objective**: Break down the full addresses into more usable components such as Address, City, and State.
- **Method**:
  - Extracted parts of `PropertyAddress` and `OwnerAddress` using SQL string functions and stored them in new columns (`PropertySplitAddress`, `PropertySplitCity`, `OwnerSplitAddress`, `OwnerSplitCity`, `OwnerSplitState`).

### Remove Duplicates
- **Objective**: Identify and remove duplicate records based on certain key fields.
- **Method**:
  - Used a CTE with `ROW_NUMBER()` to assign a unique row number to each record partitioned by address and sale details. Duplicates identified by row numbers greater than 1 were flagged.

### Delete Unused Columns
- **Objective**: Streamline the dataset by removing columns that are no longer needed.
- **Method**:
  - Dropped columns like `OwnerAddress`, `TaxDistrict`, `PropertyAddress`, and `SaleDate` post-cleanup and extraction of necessary data.

### Error Handling
- **Objective**: Ensure that operations do not fail silently.
- **Method**:
  - Added `TRY...CATCH` blocks around updates to handle and report errors during execution.

### Final Review
- **Objective**: Verify all changes and ensure the integrity of the final dataset.
- **Method**:
  - Executed a final `SELECT *` query to view the updated data and confirm the effectiveness of the cleaning processes.

## Conclusion

This project effectively cleans and restructures the Nashville Housing dataset, making it more accessible and useful for future analyses. The data cleaning steps were carefully designed to handle various types of data inconsistencies and improve the overall quality of the dataset.

## Notes

- All operations were performed within the SQL environment, utilizing T-SQL commands tailored to Microsoft SQL Server.
- It is recommended to back up the database before performing operations that significantly modify the data structure.

