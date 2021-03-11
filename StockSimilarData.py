import pandas as pd
from LoadDatasql import loadsqlfile as lsf
import warnings
class StockSmiliar:

    def __init__(self):
        self.count = 0
        self.marker = 0
        self.lis = []
        self.i = 0
        self.start = 0
        self.matched = 0
        self.col = []
        self.temp_data = []
        self.orgdata = pd.DataFrame()
        self.final_list = []


    def extract_pattern(self, orid_data, comp_data, uniq):

        comp_data=comp_data.copy()
        comp_data.reset_index(inplace=True, drop=True)
        if self.table_comp(orid_data, comp_data) != True:
            for val in range(len(orid_data)):
                # updating the pattern match code
                if orid_data.lag1[val] == 0:
                    right = 0.01
                    left = -0.01
                elif orid_data.lag1[val] < 0:
                    right = orid_data.lag1[val]-((orid_data.lag1[val] * 10) / 100)
                    left = orid_data.lag1[val] + ((orid_data.lag1[val] * 10) / 100)
                else:
                    right = orid_data.lag1[val] + ((orid_data.lag1[val] * 10) / 100)
                    left = orid_data.lag1[val] - ((orid_data.lag1[val] * 10) / 100)
                if left <= comp_data.lag1[val] <= right:
                    self.count = self.count + 1
                else:
                    break
        if self.count == len((orid_data.lag1)):
            self.temp_data.append(comp_data)
            self.matched = self.matched + 1
            self.marker = 1
            warnings.warn('Running into the loadSql python file')
            lsf().load_data(orid_data, comp_data,self.orgdata, uniq)

        self.count = 0
        self.start = self.start + 1
        self.i = self.i + 1
    def table_comp(self,orid_data, comp_data):
        if orid_data.equals(comp_data):
            return True
        else:
            return  False

    def data_forward(self, data_or, data_comp, uniq):
        # extracting the 3 pairs and send it over to the above function for comparision
        while (len(data_comp.lag1[self.i:len(data_comp)])>= len(data_or)):
            # print('DataForward--->',self.i)
            self.extract_pattern(data_or, data_comp[self.i:self.i+3],uniq)
        # print('printing the common', self.matched)
        self.col.append(self.matched)
        self.i = 0
        self.start = 0

# Below fucntion will prepare the data that will later compared to that the whole data set
    def train_dat(self, df_comp):
        loop_list = []
        self.orgdata = df_comp.copy()
        for i in reversed(range(len(df_comp))):
            if i >= 3:

                comp_list = df_comp.iloc[i-2:i+1]
                comp_list.reset_index(inplace=True, drop=True)
                self.data_forward(comp_list, df_comp, (i-(len(df_comp)+1)))
                # print('Loop run-->', i,'Matchged values for this loop', self.matched)
                if self.matched > 0:
                    loop_list.append(comp_list)
                    loop_list.append(self.temp_data.copy())
                    self.final_list.append(loop_list.copy())
                    loop_list.clear()

                self.matched = 0
                self.temp_data.clear()


            # else:
            #     break
        match=pd.DataFrame(self.col)
        # match.to_csv('match.csv')
        # self.write_file()
        return match