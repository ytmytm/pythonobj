import pandas as pd

class ParquetLoader:
    def __init__(self):
        pass

    def load(self,df,path):
        return df.to_parquet(path)
