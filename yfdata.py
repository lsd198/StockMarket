import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.arima_model import ARMA
from scipy.stats.distributions import chi2
from scipy import stats
import pyodbc
class getdata:
    def __init__(self):
        print('inside the init function')
        self.app = yf.Ticker("AAPL")
        self.dataset_org = pd.DataFrame(self.app.history(start="2021-01-11", end="2021-01-15", interval="1m"))
        self.col = self.dataset_org.columns

    # /check for the missing values
    def missing_val(self):
        print('Output the number of null values for all columns.')
        print('Null_Values            Column_Name')
        for key in self.col:
            print((self.dataset_org[key].isna().sum()) + ((self.dataset_org[key].isnull().sum())), '            ', str(key))

    def sql_load(self):
        # for col in self:
        #     self.dataset_copy.update(self.dataset_copy[col].fillna('00:00:00'))
        print('Loading the data into a table in SQL Server.')
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-NOKA9LP8;'
                              'Database=StockMarket;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        print('lal singh dhaila')
        print(self.dataset_org)
        data_new = pd.DataFrame(self.dataset_org.reset_index())
        data_new['Datetime'] = [i.strftime("%m/%d/%Y %H:%M:%S") for i in data_new['Datetime']]

        for records in range(len(data_new)):
            data = [list(data_new.iloc[records,:])]
            for lst in data:
                lst = [str(val) for val in lst]
                cursor.execute("""INSERT INTO Apple values(?,?,?,?,?,?,?,?)""", lst)
                cursor.commit()
            data.clear()
        cursor.commit()
        print('Test Check if the data is enterd in the table')
        cursor.execute("""SELECT TOP 10* FROM Apple""")
        for row in cursor:
            print(row)

# Creating the object for the class
gdata=getdata()
gdata.missing_val()
gdata.sql_load()