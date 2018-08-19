
import os
from urllib.request import urlretrieve
import pandas as pd

url_daily_adjust = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo&datatype=csv"

def get_daily_adjusted(filename='adjusted.csv',url=url_daily_adjust,force_download=false):
    """Donwload daily adjusted values from MSFT"""
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv(filename, index_col='timestamp',parse_dates=True)

    return data

