import pandas as pd
from numpy.random import randint
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time

# create a random dataframe with datetimeindex
dateRange = pd.date_range('1/1/2011', '3/30/2011', freq='D')
randomInts = randint(1, 50, len(dateRange))
df = pd.DataFrame({'RandomValues' : randomInts}, index=dateRange)

# plot with pandas own matplotlib wrapper
df.plot()

# plot directly with matplotlib pyplot
plt.plot(df.index.to_pydatetime(), df.RandomValues)

plt.show()



n=20
duration=1000
now=time.mktime(time.localtime())
timestamps=np.linspace(now,now+duration,n)
dates=[dt.datetime.fromtimestamp(ts) for ts in timestamps]
values=np.sin((timestamps-now)/duration*2*np.pi)
plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )
ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
plt.plot(dates,values)
plt.show()