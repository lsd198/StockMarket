import pandas as pd
import numpy as np
import pyodbc
import datetime
# import main_file
class loadsqlfile:


    def check_format(self, orid_data, comp_data, d_or):
        orid_data_p = orid_data.copy()
        comp_data_p = comp_data.copy()
        l_val = []
        if str(type(orid_data_p)).split('.')[-1].find('DataFrame') == 0 and \
                str(type(comp_data_p)).split('.')[-1].find('DataFrame') == 0:
            # orid_data_p['Datetime'] = [datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S") for i in orid_data_p.Datetime]
            # comp_data_p['Datetime'] = [datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S") for i in comp_data_p.Datetime]
            # have to remove this hardcoded in future to search for any random element
            ls = [orid_data_p.Datetime.loc[2],comp_data_p.Datetime.loc[2]]
            a = self.create_list(orid_data_p, comp_data_p) + self.search_dat(ls, d_or)
            return a


    def create_list(self,orid_data_p,comp_data_p):
        l_val = []
        # f_val=[]
        for i in range(len(orid_data_p)):
            l_val.extend(([i for i in orid_data_p.loc[i]]+[i for i in comp_data_p.loc[i]]))
        return l_val

    def format_modify(self, list_c):
        # have to remove the below hardcoded value in future for if condition
        for i in range(len(list_c)):
            if i == 0 or i == 3:
                list_c[i] = self.dateconversion(list_c[i], i)
            elif i > 3:
                break
        return list_c

    def search_dat(self, ls, d_or):
        val=[]
        for i in ls:
            val.append([i+(i for i in d_or.loc[i])])


        return val


    def dateconversion(self, list, i):
        val = datetime.datetime.strptime(list, "%Y-%m-%d %H:%M:%S")
        return val

    def load_data(self,orid_data, comp_data, d_or):
        d_or.set_index('Datetime',inplace=True)
        list_final = self.check_format(orid_data, comp_data, d_or)
        print('Loading the data into a table in SQL Server.')
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-NOKA9LP8;'
                              'Database=StockMarket;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        for ls in list_final:
            cursor.execute("""INSERT INTO StockMatchData values(?,?,?,?,?,?)""", ls)
            cursor.commit()
        cursor.close()




