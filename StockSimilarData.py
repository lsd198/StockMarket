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
        self.temp_data=[]
        self.orgdata = pd.DataFrame()
        self.strattest = 0
        self.final_list=[]
# vARIABLE ASSIGNMENT TO STORE THE INDEX NUMBER WITH VALUES  OF THE MATCHED VALUES
# cRETAE LIST INSISDE LIST. INSIDE LIST WILL CONSIST OF SERIES THAT WILL HAVE THE VALUES AND INDEX NUMBER OF MATCHED ONE

    def extract_pattern(self, orid_data, comp_data):
        # Below function will run to check if we are comparing the same part of the table
        # if the case is yes then skip the comparision and exit the for loop
        if self.table_comp(orid_data, comp_data) != True:
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
            # Modify the code here
            # add the mathced data in the table in the list
            # Below create the list and add the data
            # create if condtion to check if the data to be entered is similar to the compared one or if both of them  are
            # same in this case skip that and do not add else adda the code into the list
            self.temp_data.append(comp_data)
            self.matched = self.matched + 1
            self.marker = 1

        self.count = 0
        self.start = self.start + 1
        self.i = self.i + 1
    def table_comp(self,orid_data, comp_data):
        if orid_data.equals(comp_data):
            return True
        else:
            return  False

    def data_forward(self, data_or, data_comp):
        # extracting the 3 pairs and send it over to the above function for comparision
        while (len(data_comp.lag1[self.i:len(data_comp)])>= len(data_or)):
            print('DataForward--->',self.i)
            self.extract_pattern(data_or, data_comp[self.i:self.i+3])
        print('printing the common', self.matched)
        self.col.append(self.matched)
        self.i=0
        self.start=0

# Below fucntion will prepare the data that will later compared to that the whole data set
    def train_dat(self,df_comp):
        loop_list=[]
        for i in reversed(range(len(df_comp))):
            if i >=3:
                comp_list = df_comp.iloc[i-2:i+1]
                self.data_forward(comp_list,df_comp)
                # print('Loop run-->', i,'Matchged values for this loop', self.matched)
                if self.matched>0:
                    loop_list.append(comp_list)
                    loop_list.append(self.temp_data.copy())
                    self.final_list.append(loop_list.copy())
                    loop_list.clear()

                self.matched=0
                self.temp_data.clear()
                self.strattest=i

            # else:
            #     break
        match=pd.DataFrame(self.col)
        match.to_csv('match.csv')
        # self.write_file()
        return match

    # def write_file(self):
    #     f = open("myfile.txt", "x")
    #     f.write(self.final_list)
raw_csv_data = pd.read_csv("StockDtaonminfoyweeklast.csv")
raw_csv_data=raw_csv_data.set_index('Datetime')
df_comp = pd.DataFrame(raw_csv_data.Close)
df_comp['lag1'] = df_comp.Close-df_comp.Close.shift(1)
df_comp = df_comp.drop(['2021-01-11 09:30:00-05:00'], axis=0)
len_df=len(df_comp)
# df_comp.date = pd.to_datetime(df_comp.date, dayfirst=True)
# df_comp.set_index("date", inplace=True)
# df_comp = df_comp.asfreq('b')
# df_comp = df_comp.fillna(method='ffill')
# train_list = df_comp.iloc[2:5]
# print(train_list)
obj_sm = StockSmiliar()
obj_sm.train_dat(df_comp)
# obj_sm.data_forward(train_list, df_comp)

