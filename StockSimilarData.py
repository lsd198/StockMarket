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
        self.start = 0
        self.matched = 0
        self.col = []
        self.orgdata = pd.DataFrame()
        self.strattest = 0



    def extract_pattern(self, orid_data, comp_data):
        for val in range(len(orid_data)):
            # print(round(orid_data.spx[val]),round(((orid_data.spx[val] * 10) / 100) - orid_data.spx[val], 3),round(comp_data.spx[val],2),round(orid_data.spx[val]+((orid_data.spx[val] * 10) / 100), 3))
            if orid_data.lag1[val] < 0:
                right = orid_data.lag1[val]-((orid_data.lag1[val] * 20) / 100)
                left = orid_data.lag1[val] + ((orid_data.lag1[val] * 20) / 100)
            else:
                right = orid_data.lag1[val] + ((orid_data.lag1[val] * 20) / 100)
                left = orid_data.lag1[val] - ((orid_data.lag1[val] * 20) / 100)
            if left <= comp_data.lag1[val] <= right:
                self.count = self.count + 1


            else:
                break
        if self.count == len((orid_data.lag1)):
            self.lis.append(comp_data.lag1)
            self.matched = self.matched + 1
            self.marker = 1

        self.count = 0
        self.start = self.start + 1
        self.i = self.i + 1

    def data_forward(self, data_or, data_comp):

        while (len(data_comp.lag1[self.i:]) >= len(data_or)):
            print('DataForward--->',self.i)
            self.extract_pattern(data_or, data_comp[(len(data_or)+self.start):(len(data_or)+self.start)-3])
        print('printing the common', self.matched)
        self.col.append(self.matched)
        self.i=0
        self.start=0

# Below fucntion will prepare the data that will later compared to that the whole data set
    def train_dat(self,df_comp):
        for i in range(len(df_comp)):
            comp_list = df_comp.iloc[i:i+3]
            self.data_forward(comp_list,df_comp)
            print('Loop run-->', i,'Matchged values for this loop', self.matched)
            self.matched=0
            self.strattest=i
        match=pd.DataFrame(self.col)
        match.to_csv('match.csv')
        return match




raw_csv_data = pd.read_csv("StockDtaonminfoyweeklast.csv")
raw_csv_data=raw_csv_data.set_index('Datetime')
df_comp = pd.DataFrame(raw_csv_data.Close)
df_comp['lag1'] = df_comp.Close-df_comp.Close.shift(1)
df_comp = df_comp.drop(['2021-01-11 09:30:00-05:00'], axis=0)
# df_comp.date = pd.to_datetime(df_comp.date, dayfirst=True)
# df_comp.set_index("date", inplace=True)
# df_comp = df_comp.asfreq('b')
# df_comp = df_comp.fillna(method='ffill')
train_list = df_comp.iloc[2:5]
print(train_list)
obj_sm = StockSmiliar()
obj_sm.train_dat(df_comp)
# obj_sm.data_forward(train_list, df_comp)


a=[2,3,4,5,5,6,7,74,3,2,4,5,76,7]

for i in reversed(range(len(a))):
    print(i)