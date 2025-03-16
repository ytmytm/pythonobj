import pandas as pd

class CsvExtractor:
    def extract(self,path):
        return pd.read_csv(path)
