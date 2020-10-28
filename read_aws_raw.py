import pandas as pd
import datetime as dt
import os

pd.set_option('display.width', 1000, 'display.max_column', 1000, 'display.max_rows', 2000)
import warnings

warnings.filterwarnings('ignore')
import re

# df = pd.read_pickle('descriptive_aws_2019-11-01.p')

concated_df = []


def process_grouping(df):
    df['UsageStartDate'] = df['UsageStartDate'].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    df.set_index('UsageStartDate', inplace=True)
    df = df[['BlendedCost', 'UsageType', 'user:environment', 'user:Name', 'Normalized']].groupby(
        [pd.Grouper(freq='M'), 'UsageType', 'user:environment', 'user:Name', 'Normalized']).sum()

    concated_df.append(df)


for _, _, fnames in os.walk('.'):
    print(fnames)
    fnames = [f for f in fnames if 'descriptive_aws' in f]

for f in fnames:
    print(f'processing {f}')
    df = pd.read_pickle(f)
    process_grouping(df)



final_df = pd.concat(concated_df)
final_df.to_pickle('final_df.p')
print(final_df)
