"""Get data from a csv file"""
import pandas as pd

class GetDf:
    def __init__(self, path):
        """Init class"""
        self.path = path


    def get_df(self):
        """Return a df from csv file"""
        return pd.read_csv(self.path)
