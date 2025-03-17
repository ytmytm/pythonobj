import pandas as pd

class JsonLoader:
    def __init__(self,orient,index,lines):
        self.orient = orient
        self.index = index
        self.lines = lines

    def load(self,df,path):
        return df.to_json(path, orient=self.orient, index=self.index, lines=self.lines)
