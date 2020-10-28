import pandas as pd
import matplotlib.pyplot as plt

import datetime as dt
import os

pd.set_option('display.width', 1000, 'display.max_column', 1000, 'display.max_rows', 2000)
import warnings

warnings.filterwarnings('ignore')

df = pd.read_pickle('final_df.p')
df = df.reset_index()
df['user:environment'] = df['user:environment'].apply(lambda x: x.strip().replace('_', '-'))
print(df)
#
df = df.set_index('UsageStartDate').drop(['UsageType', 'user:Name', 'Normalized'], axis=1).groupby(
    [pd.Grouper(freq='M'), 'user:environment']).sum()
df = df.unstack(1)
df.columns = df.columns.get_level_values(1)

print(df)

df.to_clipboard()

from cycler import cycler

default_cycler = (cycler(
    color=['orange', 'skyblue', 'darkorchid', 'blue', 'brown', 'chartreuse', 'cyan', 'tomato', 'gold', 'green', 'grey','plum',
           'khaki', 'red','mediumblue','lavender',
           'orangered', 'lightgreen']) +
                  cycler(linestyle=['-','-', '-','-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-']))

plt.rc('lines', linewidth=4)
plt.rc('axes', prop_cycle=default_cycler)

fig, ax = plt.subplots(figsize=(15, 10))

df.plot(kind='bar', ax=ax, stacked=True)
# ax1.set_prop_cycle(custom_cycler)
plt.title('Seperated by Env Tag')
plt.tight_layout()
plt.show()
