a=["<class 'pandas._libs.tslibs.timestamps.Timestamp'>", "<class 'numpy.float64'>", "<class 'numpy.float64'>", "<class 'numpy.float64'>", "<class 'numpy.float64'>", "<class 'numpy.int64'>", "<class 'numpy.int64'>", "<class 'numpy.int64'>"]
for val in a:
    if (val.split('.')[-1]).find('int64')==0:
        print('pass')
