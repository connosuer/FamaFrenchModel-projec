# -*- coding: utf-8 -*-
"""Fama.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p4GXDaGkHJN6pZjPDgqZDZX2ouzKLsll
"""

import pandas_datareader
import matplotlib.pyplot as plt

pandas_datareader.famafrench.get_available_datasets()

start = '1926-01-01'

ff = pandas_datareader.famafrench.FamaFrenchReader('F-F_Research_Data_Factors', freq = 'M', start = start).read()

ff

ff_df = ff[0]

ff_df.plot(subplots = True, figsize = (12,4))

ff_df.rolling(72).mean().plot(subplots=True, figsize=(12,4))

ff_mom_df = pandas_datareader.famafrench.FamaFrenchReader('F-F_Momentum_Factor',freq = 'M', start = start).read()[0]

ff_mom_df.rolling(72).mean().plot(subplots = True, figsize=(12,4))

ff_df

ff_mom_df

import pandas as pd
ffac_merged_df = pd.merge(ff_df,ff_mom_df,on = 'Date', how='inner',sort=True, copy= True,indicator=False, validate ='one_to_one')

ffac_merged_df

import yfinance as yf

AAPL_data = yf.download('AAPL', start=start)['Adj Close'].resample('M').ffill().pct_change()

AAPL_data

AAPL_df = AAPL_data.to_frame()

AAPL_df

AAPL_df.index.dtype

ffac_merged_df.index.dtype

AAPL_df['str_date'] = AAPL_df.index.astype(str)
AAPL_df['dt_date'] = pd.to_datetime(AAPL_df['str_date']).dt.strftime('%Y-%m')

AAPL_df.dt_date.dtype

ffac_merged_df['str_date']= ffac_merged_df.index.astype(str)
ffac_merged_df['dt_date'] = pd.to_datetime(ffac_merged_df['str_date']).dt.strftime('%Y-%m')
ffac_merged_df.dt_date.dtype

AAPL_ffac_merge_df = pd.merge(AAPL_df,ffac_merged_df, how='inner',on='dt_date',sort=True, copy=True,indicator=False,validate='one_to_one')

AAPL_ffac_merge_df

AAPL_ffac_merge_df.drop(columns=['str_date_x','str_date_y'],inplace=True)

AAPL_ffac_merge_df.rename(columns={'Adj Close':'AAPL'},inplace=True)

AAPL_ffac_merge_df['AAPL_RF'] = AAPL_ffac_merge_df['AAPL']*100 - AAPL_ffac_merge_df['RF']

AAPL_ffac_merge_df.dropna(axis=0,inplace=True)

list(AAPL_ffac_merge_df)

AAPL_ffac_merge_df.rename(columns={'Mom   ': 'MOM'},inplace=True)

from statsmodels.api import OLS
results = OLS(AAPL_ffac_merge_df['AAPL_RF'],AAPL_ffac_merge_df[['Mkt-RF','SMB','HML','MOM']],missing='drop').fit()

results.summary()

import statsmodels.tools
AAPL_ffac_merge_df_c = statsmodels.tools.add_constant(AAPL_ffac_merge_df,prepend=True)

AAPL_ffac_merge_df_c

results = OLS(AAPL_ffac_merge_df_c['AAPL_RF'],AAPL_ffac_merge_df_c[['const','Mkt-RF','SMB','HML','MOM']],missing='drop').fit()
results.summary()

x