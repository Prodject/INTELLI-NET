# Decision-making in case of traffic congestio
import numpy as np, time, requests, os, pandas as pd, re, time, threading, sys, scrapy.all as scrapy
from numpy import array
from fuzzywuzzy import fuzz, process
from datetime import datetime
# example data
######
ip = '10.7.5.100' # target ip addr
server_host = '10.7.5.1' # gateway ip addr
normal = '1100' # normal download speed / mbps
client = '1730' # current client download speed / mbps
######
data = {'normal download speed': [normal], 'current download speed': [client]}
title = ['normal download speed', 'current download speed']
df = pd.DataFrame(data, columns = title)
df.to_csv (r'data_fuzzy.csv', index = False, header = True)
aread = pd.read_csv('data_fuzzy.csv', delimiter = ',', index_col = False, skiprows = 1, names = title)
print(df)
# if else expression
if (client > normal):
    print('Disable client')
    de_auth = scapy.ARP(psrc = server_host, op = 2, pdst = ip, hwdst = scapy.getmacbyip(ip))
    scapy.send(de_auth, verbose = False)
    de_auth = scapy.ARP(psrc = ip, op = 2, pdst = server_host, hwdst = scapy.getmacbyip(server_host))
    scapy.send(de_auth, verbose = False)
    time.sleep(500)
else:
        print('Speed normal')