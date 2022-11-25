#! /usr/bin/env python3

import pandas as pd

data = {'item': ('pants', 'pants', 'shirt', 'sweater', 'sweater', 'sweater'),
	'price': (40, 45, 15, 30, 25, 20)}

df = pd.DataFrame(data)

standardize = lambda series: (series - series.mean())/series.std()

df['zPrice'] = df.groupby('item').price.transform(standardize)

print(df)
