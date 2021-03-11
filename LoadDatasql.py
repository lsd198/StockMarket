import pandas as pd
import numpy as np
import pyodbc
import datetime
# import main_file
import warnings
class loadsqlfile:


    def check_format(self, orid_data, comp_data, d_or):
        orid_data_p = orid_data.copy()
        comp_data_p = comp_data.copy()
        l_val = []
        if str(type(orid_data_p)).split('.')[-1].find('DataFrame') == 0 and \
                str(type(comp_data_p)).split('.')[-1].find('DataFrame') == 0:
            # have to remove this hardcoded in future to search for any random element
            warnings.warn('Creating the list of next timestamp data ')
            ls = [orid_data_p.Datetime.loc[2],comp_data_p.Datetime.loc[2]]
            warnings.warn('Generating the list for the check format function')
            se_d = self.search_dat(ls, d_or)
            a = self.create_list(orid_data_p, comp_data_p) + se_d[0]
            return a, se_d[1]


    def create_list(self,orid_data_p,comp_data_p):
        o_val = []
        c_val=[]
        # f_val=[]
        for i in range(len(orid_data_p)):
            o_val.extend((i for i in orid_data_p.loc[i]))
            c_val.extend(i for i in comp_data_p.loc[i])
        return o_val+c_val

    def format_modify(self, list_c):
        # have to remove the below hardcoded value in futd  ure for if condition
        for i in range(len(list_c)):
            if i == 0 or i == 3:
                list_c[i] = self.dateconversion(list_c[i], i)
            elif i > 3:
                break
        return list_c

    def search_dat(self, ls, d_or):
        # adding the comment
        val = []
        warnings.warn('Creating the next time tamp data and storing in the list')
        for i in ls:
            a = d_or[d_or.Datetime == i+datetime.timedelta(minutes=1)]
            if len(a)!=0:
                a.reset_index(inplace=True, drop=True)
                val.extend([i for i in a.loc[0]])
                flag=1
            else:
                flag = 0
                break
        return val, flag


    def dateconversion(self, list, i):
        val = datetime.datetime.strptime(list, "%Y-%m-%d %H:%M:%S")
        return val

    def load_data(self,orid_data, comp_data, d_or, uniq):
        # d_or.set_index('Datetime',inplace=True)
        warnings.warn('Running the check_format function')
        list_final = self.check_format(orid_data, comp_data, d_or)

        if list_final[1] == 1:
            print('Loading the data into a table in SQL Server.')
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=LAPTOP-NOKA9LP8;'
                                  'Database=StockMarket;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()
            # for ls in list_final:
            cursor.execute("""INSERT INTO StockMatch2 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", [uniq]+list_final[0])
            cursor.commit()
            cursor.close()




