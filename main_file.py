import pandas as pd
import StockSimilarData
import time


class start_analysis:

    def load_data(self):
        start_time=time.perf_counter()
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
        obj_sm = StockSimilarData.StockSmiliar()
        obj_sm.train_dat(df_comp)
        finish_time=time.perf_counter()
        print(f'Finished in {round(finish_time-start_time)/3600} hours(h)')



sa=start_analysis()
sa.load_data()