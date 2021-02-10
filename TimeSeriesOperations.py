from time import strftime

import pandas as pd
from dateutil.parser import parse
from datetime import datetime, timedelta
from datetime import datetime as dt
# Dealing with time stamp
# Handling operations with days, weeks, months, years?
# Generating the date ranges
    # 1.Generating the sequential date range
    # 2.Generating the random date ranges
# Changing Date Format in a column DataFrame
# df['date'] = df['date'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
# df['date'] = df['date'].apply(lambda x: pd.Timestamp(x).strftime('%B-%d-%Y %I:%M %p'))

# Change column type — from Object/String to DateTime
# 1
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df['date'] = pd.to_datetime(df['date'])
print(df)
print(df.info())
# 2
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df['date'] = df['date'].astype('datetime64[ns]')
print(df)
print(df.info())
# 3
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df['date'] = df['date'].apply(lambda x: parse(x))
print(df)
print(df.info())
# 4
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df['date'] = df['date'].apply(lambda x: pd.Timestamp(x))
print(df)
print(df.info())

# Going from String to Date format, and from Date format to String
str_date = '2018-05-01'
# String to Date:
date_1 = parse(str_date)
print ('date_1: ',date_1, type(date_1))
# Date to String:
date_2 = date_1.strftime('%Y-%m-%d')
print ('date_2: ',date_2, type(date_2))

# From Unix/Epoch time to Readable date format
df = pd.DataFrame({'date': [1349720105,1349806505]})
print('Before the date time ')
print(df)
df['date'] = pd.to_datetime(df['date'],unit='s')
print('After the date time')
print(df)

# Add and subtract dates
print(parse('2019-04-07')-timedelta(days=3))

print((parse('2019-04-07')-timedelta(days=3)).strftime('%Y-%m-%d'))
# Get the difference between two dates
d1 = parse('2018-12-01')
d2 = parse('2018-12-08')
print(abs((d2 - d1).days))


# Operations with Days
# for a column in a DataFrame
from datetime import datetime as dt
print(df)
df['day'] = df['date'].dt.day
print(df['day'])

# Operations with Weeks
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-01-02 13:15:21']})
# if date column type is a string
df['week'] = pd.DatetimeIndex(df['date']).week


# if date column type is a datetime
# df['week'] = df['date'].dt.week

# To create a Week column, in the format yyyy-ww, use:
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
df['yyyy_ww'] = pd.DatetimeIndex(df['date']).strftime('%Y-%U')

# if column type is a datetime
# df['yyyy_ww'] = df['date'].dt.strftime('%Y-%U')


# And for an isolated variable:
date_1 = '2018-02-06'
parse(date_1).isocalendar()[1]

# Get weekday
df['weekday'] = df['date'].apply(lambda x: parse(str(x)).strftime("%A"))


# Go from Year-Week format to yyyy-mm-dd format (getting the first and last day o of the week)

# define this function
def get_start_end_dates(yyyyww):
    year = yyyyww[:4]
    week = yyyyww[-2:]
    first_day_year = str(year) + '-' +  '01' + '-' + '01'
    d = parse(first_day_year)
    if(d.weekday()<= 3):
        d = d - timedelta(d.weekday())
    else:
        d = d + timedelta(7-d.weekday())
    dlt = timedelta(days = (int(week)-1)*7)
    return (d + dlt).strftime('%Y-%m-%d'),  (d + dlt + timedelta(days=6)).strftime('%Y-%m-%d')
# run it
get_start_end_dates('201837')

# Get month number of the year
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
# if date column type is a string/object
df['month'] = pd.DatetimeIndex(df['date']).month
# if date column type is a datetime
# df['month'] = df['date'].dt.month

# And for an isolated variable:
import datetime
date_1 = '2018-02-06'
parse(date_1).month


# To create a month column, in the format YYYY-MM, use:
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
# if column type is a string/object
df['yyyy_mm'] = pd.DatetimeIndex(df['date']).strftime('%Y-%m')
# if column type is a datetime
# df['yyyy_mm'] = df['date'].dt.strftime('%Y-%m')

# Add or subtract months (go X months back or forward)

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    new_date = (date.replace(day=d,month=m, year=y))
    return new_date.strftime('%Y-%m-%d')

monthdelta(parse('2019-11-09'), -4)

# Operation with Years
# Get the year
# Example:
df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
# if date column type is a string/object
df['year'] = pd.DatetimeIndex(df['date']).year
# if date column type is a datetime
# df['year'] = df['date'].dt.year


# And for an isolated variable:
import datetime
date_1 = '2018-02-06'
parse(date_1).year


# Generate data ranges
# Generate Sequential date ranges
# Example: generating a date range from 01/01/2019 to 01/02/2019, with hourly frequency.
from datetime import datetime
import numpy as np
date_range = pd.date_range(start='01/01/2019', end='01/02/2019', freq='H')

# Generate Random date ranges









