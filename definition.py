import pandas as pd
import time


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("../data.csv")
        return tuple(df.loc[df['word'] == self.term]['definition'])


count = 1
d = Definition(term='sun')
result = d.get()
for i in result:
    print(f"{count}: {i}")
    count += 1
