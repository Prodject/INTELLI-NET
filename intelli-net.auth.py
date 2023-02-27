# Decision-making system in the management of heat technology facilities
import numpy as np, time, requests, os, pandas as pd, re
from numpy import array
from fuzzywuzzy import fuzz, process
from datetime import datetime
# emulate server device
server = ''.join(format(ord(i), '08b') for i in str(time.time())+'DE13G')
# emulate client device
client = ''.join(format(ord(i), '08b') for i in str(time.time())+'DE13G')
data = {'THIS DEVICE (SERVER)': [server], 'EMULATE DEVICE (CLIENT)': [client]}
title = ['THIS DEVICE (SERVER)', 'EMULATE DEVICE (CLIENT)']
df = pd.DataFrame(data, columns = title)
df.to_csv (r'data_fuzzy.csv', index = False, header = True)
aread = pd.read_csv('data_fuzzy.csv', delimiter = ',', index_col = False, skiprows = 1, names = title)
# Get partial ration output
df['Math rate'] = df.apply(lambda aread: fuzz.partial_ratio(aread['THIS DEVICE (SERVER)'], aread['EMULATE DEVICE (CLIENT)']), axis = 1)
# Regular expression comparsion to get access
match = re.search(r'0*[8-9]\d', str(fuzz.partial_ratio(server, client)), re.M | re.I)
if match:
    print('Grant access')
else:
    print('Access denied')
df