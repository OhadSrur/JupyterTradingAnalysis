import os
from urllib.request import urlretrieve
import pandas as pd

apiPath = "source\\apiKey.txt"
with open(apiPath) as f:
	apiKey = f.read()

def get_data_adjusted(symbol='MSFT',filename='adjusted.csv',data_type='daily',force_download=False):
	"""Donwload daily/ weekly adjusted values from MSFT

	Parameters
	----------
	symbol : stirng (optional)
		Required symbol
	filename : string (optional)
		location to save the file
	data_type : string (optional)
		return 'daily' or 'weekly' data
	force_downlaod : bool (optional)
		if True, force redownload of data

	Returns
	-------
	pandas.DataFrame
		MSFT 100 daily tick of data
	"""
	if data_type == 'daily':
		url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+symbol+"&apikey="+apiKey+"&datatype=csv"
	elif data_type == 'weekly':
		url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol="+symbol+"&apikey="+apiKey+"&datatype=csv"

	if force_download or not os.path.exists(filename):
		urlretrieve(url, filename)
	data = pd.read_csv(filename, index_col='timestamp',parse_dates=True)

	return data