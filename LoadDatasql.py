import pandas as pd
import numpy as np
import pyodbc
import datetime
class loadsqlfile:


    def check_format(self,orid_data, comp_data):
        orid_data_p = orid_data.copy()
        comp_data_p = comp_data.copy()
        if str(type(orid_data_p)).split('.')[-1].find('DataFrame') == 0 and \
                str(type(comp_data_p)).split('.')[-1].find('DataFrame') == 0:
            orid_data_p.reset_index(inplace=True)
            comp_data_p.reset_index(inplace=True)
            a = self.create_list(orid_data_p, comp_data_p)
            return a


    def create_list(self,orid_data_p,comp_data_p):
        l_val = []
        f_val=[]
        for i in range(len(orid_data_p)):
            l_val.extend(i for i in orid_data_p.loc[i])
            l_val.extend(i for i in comp_data_p.loc[i])
            f_val.append(self.format_modify(l_val.copy()))
            l_val.clear()
        return f_val

    def format_modify(self, list_c):
        for i in range(len(list_c)):
            if i == 0 or i == 3:
                list_c[i] = self.dateconversion(list_c[i],i)
            elif i > 3:
                break
        return list_c



    def dateconversion(self, list, i):
        if list.find('2021-02-04 15:04:00')==0:
            print('test')
            y = int(list.split(' ')[0].split('-')[0].strip("0"))
            m = int(list.split(' ')[0].split('-')[1].strip("0"))
            d = int(list.split(' ')[0].split('-')[2].strip("0"))
            h = int(list.split(' ')[1].split(':')[0].strip("0"))
            mi = int(list.split(' ')[1].split(':')[1].strip("0"))
            val = datetime.datetime(y, m, d, h, mi)
        else:
            y = int(list.split(' ')[0].split('-')[0].strip("0"))
            m = int(list.split(' ')[0].split('-')[1].strip("0"))
            d = int(list.split(' ')[0].split('-')[2].strip("0"))
            h = int(list.split(' ')[1].split(':')[0].strip("0"))
            if list.split(' ')[1].split(':')[1].strip("0")=='':
                val = datetime.datetime(y, m, d, h)
            else:
                val = datetime.datetime(y, m, d, h, int(list.split(' ')[1].split(':')[1].strip("0")))

            # Seond is not calculate becasuse the data is extracted for every minute
            # .Becasue of which the second will always be 00
            # se = int(list[1].split(' ')[1].split(':')[2].split('-')[0].strip("0"))

        return val

    def load_data(self,orid_data, comp_data):
        list_final = self.check_format(orid_data, comp_data)
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




