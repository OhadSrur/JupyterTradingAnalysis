import os
from urllib.request import urlretrieve
import pandas as pd

apiPath = "source\\apiKey.txt"
with open(apiPath) as f:
	apiKey = f.read()

def get_data_adjusted(symbol='MSFT',filename='adjusted.csv',data_type='daily',force_download=False,outputsize='compact',start_date='2014-01-01'):
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
	outputsize : string (optional)
		'compact' = 100 data points, or 'full' = 20 years of data
	Returns
	-------
	pandas.DataFrame
		MSFT 100 daily tick of data
	"""
	if data_type == 'daily':
		url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+symbol+"&apikey="+apiKey+"&datatype=csv&outputsize="+outputsize
	elif data_type == 'weekly':
		url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol="+symbol+"&apikey="+apiKey+"&datatype=csv&outputsize="+outputsize

	if force_download or not os.path.exists(filename):
		urlretrieve(url, filename)
	data = pd.read_csv(filename, index_col='timestamp')
	
	#Specifying the date format can speed up the process of converting string to date
	try:
		#data.index = pd.to_datetime(data.index, format='%d/%m/%y')
		data.index = pd.to_datetime(data.index, format='%Y/%m/%d')
	except TypeError:
		data.index = pd.to_datetime(data.index)
	return data[data.index >= start_date]