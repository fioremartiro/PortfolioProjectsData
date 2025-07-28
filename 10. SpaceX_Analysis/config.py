
"""Main functions and variables"""
import csv
import json
import pandas as pd

PATH = "files\\spacex_launch_data(original).csv"
JSON_PATH = "files\\spacex_launch_data(original).json"
NEW_FILE_PATH = "files\\spacex_launch_data(prep).csv"

class prepData:
    def csv_to_json():
        data = {}

        # create dictionary
        with open(PATH, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            # Convert each row into a dictionary
            # and add it to data
            for rows in csvReader:

                # Assuming a column named 'No' to
                # be the primary key
                key = rows['Flight Number']
                data[key] = rows

        # Open a json writer, and use the json.dumps()
        # function to dump data
        with open(JSON_PATH, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))


    def get_json():
        """returns dictionary from json file"""
        with open(JSON_PATH) as f:
            data = list(json.load(f).items())
            
        return data

    def get_df():
        return pd.read_csv(PATH)

    def save_csv(df: pd.DataFrame):
        """Save DataFrame to csv file"""
        df.to_csv(NEW_FILE_PATH)  
