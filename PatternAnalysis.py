import numpy as np
import pandas as pd
import datetime
import pyodbc


class Min_price_nxt:
    def __init__(self):
        self.df_or = pd.read_csv('StockDtaonminfoyweeklast.csv')
        self.mt_data  = pd.read_csv('StockMatchData,csv')
    def min_fp(self):
        # // to do analysis on the original table we have to covert the datetime table into datetime64
        self.date_time_cov()
        data_copy = self.df_or.copy()
        data_copy['Datetime'] = self.date_time_cov()
        print(data_copy)
    def date_time_cov(self):
        var_list = [i for i in self.df_or.Datetime]
        final_list = []
        for ls in var_list:
            y = int(ls.split(' ')[0].split('-')[0].strip("0"))
            m = int(ls.split(' ')[0].split('-')[1].strip("0"))
            d = int(ls.split(' ')[0].split('-')[2].strip("0"))
            h = int(ls.split(' ')[1].split(':')[0].strip("0"))
            if ls.split(' ')[1].split(':')[1].strip("0") == '':
                final_list.append(datetime.datetime(y, m, d, h))
            else:
                final_list.append(datetime.datetime(y, m, d, h, int(ls.split(' ')[1].split(':')[1].strip("0"))))
        return final_list




mpn=Min_price_nxt()
mpn.min_fp()