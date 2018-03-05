# encoding=utf-8
from collections import defaultdict

import pandas as pd

if __name__ == '__main__':
    input_file_path = '../nyt-ingredients-snapshot-2015_v1.csv'

    df = pd.read_csv(input_file_path)
    df = df.fillna("")

    units_dict = defaultdict(int)
    for index, row in df.iterrows():
        try:
            # extract the display name
            unit = row.get('unit')
            if unit:
                units_dict[unit] += 1

        # ToDo: deal with this
        except UnicodeDecodeError:
            pass

    print('{')
    for k in sorted(units_dict, key=units_dict.get, reverse=True):
        print('\t\'{}\': {},'.format(k, units_dict[k]))
    print('}')
