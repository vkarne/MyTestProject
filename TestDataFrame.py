import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,6), ['A', 'B', 'C', 'D', 'E'], ['M', 'N', 'O','P', 'Q', 'R'])
print("Main DataFrame:")
print(df)
print("\ndf[df['Q']>0]['Q'] is:")
print(df[df['Q']>0]['Q'])
print('\nBoolen dataframe is:')

boolser = df['O']>0

print(boolser)
print("\ndf[(df['M']>0) & (df['P']>0)] is:")
print(df[(df['M']>0) & (df['P']>0)])
print("\ndf[(df['M']>0) | (df['P']>0)] is:")
print(df[(df['M']>0) | (df['P']>0)])
