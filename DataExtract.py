import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.arima_model import ARMA
from scipy.stats.distributions import chi2
from scipy import stats
import pyodbc
import  yfinance as yf
class StockSmiliar:

    def __init__(self):
        self.count = 0
        self.marker = 0
        self.lis = []
        self.i = 0
        self.start=0
        self.matched=0
        self.col=[]
        self.orgdata=pd.DataFrame()

    def extract_data(self):
        print('Extracting the data from the yfinance site')
        app = yf.Ticker("AAPL")
        dataset_org = pd.DataFrame(app.history(start="2021-01-25", end="2021-01-30", interval="1m"))
        self.col = dataset_org.columns
        self.orgdata=pd.DataFrame(dataset_org)



#
# raw_csv_data = pd.read_csv("Index2018.csv")
# df_comp = raw_csv_data.copy()
# df_comp.date = pd.to_datetime(df_comp.date, dayfirst=True)
# df_comp.set_index("date", inplace=True)
# df_comp = df_comp.asfreq('b')
# df_comp = df_comp.fillna(method='ffill')
# train_list = pd.DataFrame((df_comp.spx[4563:4567] - df_comp.spx[4563:4567].shift(1))).drop(pd.Timestamp('2011-07-06'))
# test_list = pd.DataFrame((df_comp.spx - df_comp.spx.shift(1)).drop(pd.Timestamp('1994-01-07')))
# print(train_list)
objsm = StockSmiliar()
# objsm.data_forward(train_list, test_list)
objsm.extract_data()
objsm.sql_data()
