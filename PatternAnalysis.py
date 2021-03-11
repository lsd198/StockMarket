import numpy as np
import pandas as pd
import datetime
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt

class c_analysis:
    # dump all the files that are generated into some location which will be easy to reload
    def load_analyze(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-NOKA9LP8;'
                          'Database=StockMarket;'
                          'Trusted_Connection=yes;')
        l_data = pd.read_sql('Select * from StockMatch2',conn)
        l_data.to_csv('l_data.csv')
        c_data = pd.DataFrame({'Pattern_ID':[i for i in l_data.Pattern_ID.value_counts().index], 'p_count':
                               [l_data.Pattern_ID.value_counts()[i] for i in l_data.Pattern_ID.value_counts().index]})
        # Selecting the maximum count for the pattern
        c_data.to_csv('c_data.csv')
        max_data = l_data[l_data.Pattern_ID == c_data[c_data.p_count == c_data.p_count.max()].Pattern_ID[0]]
        max_data.reset_index(inplace=True, drop=True)
    def plot_trend(self,index):
        # c_data = pd.read_csv('c_data.csv')
        l_data = pd.read_csv('l_data.csv')
        max_data = l_data[l_data.Pattern_ID == index]
        max_data.reset_index(inplace=True, drop=True)
        for i in range(len(max_data)):
            if i == 0:
                a = [max_data.loc[i].lag_1_c, max_data.loc[i].lag_2_c, max_data.loc[i].lag_3_c,max_data.loc[i].Lag_1_sv]
                plt.plot(a)
                a = [max_data.loc[i].Lag_1_m, max_data.loc[i].Lag_2_m, max_data.loc[i].Lag_3_m,max_data.loc[i].Lag_2_sv]
                plt.plot(a)
            else:
                a = [max_data.loc[i].Lag_1_m, max_data.loc[i].Lag_2_m, max_data.loc[i].Lag_3_m,max_data.loc[i].Lag_2_sv]
                plt.plot(a)






        # // create a column containg the all the patternID and with their repetetions


c_ob = c_analysis()

# c_ob.load_analyze()
c_ob.plot_trend(-4151)
print(c_ob)
