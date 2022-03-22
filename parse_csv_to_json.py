import pandas as pd
import numpy as np

def parse_csv_to_json(data):
    for df in pd.read_csv(data, iterator=True, chunksize=1_000_000,low_memory=False):
        df.rename(columns = str.lower, inplace = True)
        df.replace({np.nan:None},inplace = True)
        for row in df.index:
            doc = dict(zip(df.columns.tolist(), df.loc[row].tolist() ))
            yield doc
