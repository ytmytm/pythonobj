import pandas as pd

class Deduplicator:
    def __init__(self,fields):
        self.fields = fields

    def transform(self,df):
        return df[self.fields].drop_duplicates()
