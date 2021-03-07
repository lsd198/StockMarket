import pandas as pd
import numpy as np
import datetime
import StockSimilarData
import time


class s_analysis:
    def __init__(self):
        self.start_time = time.perf_counter()
        raw_csv_data = pd.read_csv("StockDtaonminfoyweeklast.csv")
        raw_csv_data = raw_csv_data.set_index('Datetime')
        df_comp = pd.DataFrame(raw_csv_data.Close)
        df_comp['lag1'] = df_comp.Close - df_comp.Close.shift(1)
        df_comp = df_comp.drop(['2021-01-11 09:30:00-05:00'], axis=0)
        self.df_comp = self.date_for_change(df_comp).copy()

    def load_data(self):
        obj_sm = StockSimilarData.StockSmiliar()
        obj_sm.train_dat(self.df_comp)
        finish_time = time.perf_counter()
        print(f'Finished in {round(finish_time - self.start_time) / 3600} hours(h)')

    def date_for_change(self, data):
        data.reset_index(inplace=True)
        data['Datetime'] = [str(i[:19]) for i in d.Datetime]
        return data
