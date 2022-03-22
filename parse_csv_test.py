import pandas as pd
import numpy as np

import parse_csv_to_json as pc2j

def analyse_big_file(filename):
    with open(filename,'rb') as f:
        maxlen = 0
        maxrow = None
        for num,row in enumerate(pc2j.parse_csv_to_json(f)):
            linelen = sum([len(v) for k,v in row.items() if isinstance(v,str)])
            if linelen > maxlen:
                maxlen = linelen
                maxrow = row
        print(maxlen,maxrow)

if __name__ == '__main__':
    analyse_big_file('bigfile.csv')
