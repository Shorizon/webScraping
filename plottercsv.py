from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import dates as mpl_dates

##########################################################################################################################
plt.style.use('seaborn')



##########################################################################################################################

												#read csv file and extract data to plot 

def graph_plotter(ebay,amazon):

	data_Ebay = pd.read_csv(ebay)									
	data_Amazon = pd.read_csv(amazon)

##########################################################################################################################

												
												#extract data that is needed in 

	data_Ebay['Timestamp'] = pd.to_datetime(data_Ebay['Timestamp'])
	data_Ebay.sort_values('Timestamp', inplace=True)

	data_Amazon['Timestamp'] = pd.to_datetime(data_Amazon['Timestamp'])
	data_Amazon.sort_values('Timestamp', inplace=True)

##########################################################################################################################

												#assign data to variables to be plotted

	price_Ebay = data_Ebay['Listing price']
	date_Ebay = data_Ebay['Timestamp']

	price_Amazon = data_Amazon['Listing price']
	date_Amazon = data_Amazon['Timestamp']

##########################################################################################################################
	
												#plots the graph with two lines 


	plt.plot_date(date_Ebay, price_Ebay, linestyle = 'solid', label = 'ebay')
	plt.plot_date(date_Amazon, price_Amazon, linestyle = 'solid', label = 'amazon')

##########################################################################################################################
	
												#set the format of the date value 
	plt.gcf().autofmt_xdate()
	date_format = mpl_dates.DateFormatter('%b, %d %Y')
	plt.gca().xaxis.set_major_formatter(date_format)

												#label the x and y axis
	plt.ylabel('Price')
	plt.xlabel('Date')
												#create a legend to show which line is which
	plt.legend(loc="upper right")
	plt.tight_layout()
	plt.show()									#show the graph

	return plt.gcf()


  