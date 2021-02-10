class loaddata:
    def __init__(self):
        pass
    def sql_load(self ):
        for col in self.dataset_copy.columns:
            self.dataset_copy.update(self.dataset_copy[col].fillna('00:00:00'))
        print('Loading the data into a table in SQL Server.')
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-NOKA9LP8;'
                              'Database=StockMarket;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()

        for records in range(len(self.dataset_copy)):
            data = [list(self.dataset_copy.loc[records])]
            for lst in data:
                cursor.execute("""INSERT INTO Apple values(?,?,?,?,?,?,?,?)""", lst)
                cursor.commit()
            data.clear()
        cursor.commit()
        print('Test Check if the data is enterd in the table')
        cursor.execute("""SELECT TOP 10* FROM FireBrigade""")
        for row in cursor:
            print(row)

ldata=loaddata
