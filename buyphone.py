# -*- coding: utf-8 -*-
"""buyPhone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aq-9-OzEF2PZ1EHaKR_60qN1vLhu2oKA
"""

import pandas as pd
dfs = pd.read_html('https://www.cht.com.tw/home/campaign/samsunggalaxypromo')
df = dfs[0].iloc[:,[0,2,3,4,5,6,7,8]]
df.columns = ['機型', '$599', '$799', '$999', '$1199', '$1399', '$1599', '$1799']
df.head()

df['month'] = df['機型'].str.extract('(\d+)個月')
df['month'] = df['month'].ffill()
# df.dropna(inplace = True)
df.head()

df2 = df[~df['機型'].str.contains('個月')]
df2['month'] = df2['month'].fillna(48)
df2.head(10)

import pandas as pd
df3 = pd.wide_to_long(df2,['$'], i = ['機型','month'], j = 'monthly_price', suffix = '[\d,]+')
df3.reset_index(inplace = True)
df3.head()

df4 = df3[df3['$'] != '-']
df4.head()

df4.info()

df4['month'] = df4['month'].astype(int)

df4['$'] = df4['$'].astype(int)

df4['total'] = df4['month'] * df4['monthly_price'] + df4['$']

df4.sort_values('total')

