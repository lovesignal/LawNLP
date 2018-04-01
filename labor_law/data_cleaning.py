import pandas as pd
import numpy as np

import csv
law_double_list = []
law_single_list = []
with open('law.csv', 'r') as raw:
    cooked = csv.reader(raw)
    for record in cooked:
        print(record)
        law_double_list.append(record)
        start = len(law_single_list)
        law_single_list[start:start] = record

print(law_single_list)