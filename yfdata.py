import yfinance as yf
import pandas as pd
import numpy as np
import datetime
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
        self.dataset_org = pd.DataFrame(self.app.history(start="2021-02-22", end="2021-02-27", interval="1m"))
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

        data_new = pd.DataFrame(self.dataset_org.reset_index())
        # data_new['Datetime'] = [[for i in ] for i in range(len(data_new))]

        for records in range(len(data_new)):
            data = [list(data_new.iloc[records,:])]
            # check datatype of all the variable
            # ConnectionErrorompare if the variables are of datetime or int64 type
            # if ye then change the datatype of the variable and store in the list
            list_val=[]
            for val in data[0]:
                if(str(type(val)).split('.')[-1]).find('int64') == 0:
                    list_val.append(int(val))
                elif (str(type(val)).split('.')[-1]).find('Timestamp') == 0:
                    list_val.append(datetime.datetime(val.year,val.month,val.day,val.hour,val.month,val.second))
                else:
                    list_val.append(val)
            cursor.execute("""INSERT INTO test values(?,?,?,?,?,?,?,?)""", list_val)
            cursor.commit()
            data.clear()
        cursor.commit()
        print('Test Check if the data is entered in the table')
        cursor.execute("""SELECT TOP 10* FROM Apple""")
        for row in cursor:
            print(row)


# Creating the object for the class
# gdata=getdata()
# gdata.missing_val()
# gdata.sql_load()