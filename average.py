import pandas as pd
###########################################################################################################################

									#reads file created by the scraper to make an average of all the values.
									#values are addedd to a new file with a single average. 



def meaning(ebay, amazon,user_input):
	
	container = []												#create an empty array to store data

	data = pd.read_csv(ebay)									#read the data from the csv file

	price = data['Listing price'].mean()						#average of all the data in the csv
	date = data['Timestamp'][0]									#set 1 date since date-time format cannot be avegared

	averaged = {}
	averaged['Listing price'] = price							#set new column with the data
	averaged['Timestamp'] = date 								#set new column with the data

	container.append(averaged)													#adds the data to container

	finished = pd.DataFrame(container)													#create panda dataframe
	finished.to_csv(f'Ebay_averaged_{user_input}.csv', index=False)						#save dataframe to new file





###########################################################################################################################
	
	container = []												#create an empty array to store data

	data = pd.read_csv(amazon)									#read the data from the csv file	

	price = data['Listing price'].mean()						#average of all the data in the csv
	date = data['Timestamp'][0]									#set 1 date since date-time format cannot be avegared

	averaged = {}
	averaged['Listing price'] = price							#set new column with the data
	averaged['Timestamp'] = date 								#set new column with the data

	container.append(averaged)													#adds the data to container

	finished = pd.DataFrame(container)													#create panda dataframe
	finished.to_csv(f'Amazon_averaged_{user_input}.csv', index=False)					#save dataframe to new file




	return



